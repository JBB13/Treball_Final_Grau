from picamera2 import Picamera2
import cv2
import numpy as np
import time
import tflite_runtime.interpreter as tflite
import sqlite3
from datetime import datetime
import uuid

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
time.sleep(2)

interpreter = tflite.Interpreter(model_path="modelo_cnn_clasificacion_objetos_kaggle.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

idx_to_class = {0: "arandela", 1: "clavo", 2: "tuerca", 3: "tornillo"}
image_size = (128, 128)


def detectar_piezas_por_contornos(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    piezas = []
    for cnt in contornos:
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > 500:
            roi = frame[y:y+h, x:x+w]
            piezas.append((x, y, w, h, roi))
    return piezas

trackers = dict()  
labels = dict()    
frame_count = 0
scan_interval = 30

conn = sqlite3.connect("/home/pi/detecciones.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS detecciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        clase TEXT,
        probabilidad REAL
    )
''')
conn.commit()
conn.close()

while True:
    frame = picam2.capture_array()
    imagen = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame_count += 1

    ids_to_delete = []
    for obj_id, tracker in trackers.items():
        success, bbox = tracker.update(imagen)
        if success:
            x, y, w, h = [int(v) for v in bbox]
            label = labels.get(obj_id, "desconegut")
            cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imagen, f"ID {obj_id[:5]}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            cv2.putText(imagen, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        else:
            ids_to_delete.append(obj_id)

    for obj_id in ids_to_delete:
        trackers.pop(obj_id)
        labels.pop(obj_id)

    if frame_count % scan_interval == 0:
        piezas = detectar_piezas_por_contornos(imagen)
        for (x, y, w, h, roi) in piezas:
            nueva_roi = imagen[y:y+h, x:x+w]

            overlapped = False
            for tracker in trackers.values():
                success, tbox = tracker.update(imagen)
                if success:
                    tx, ty, tw, th = [int(v) for v in tbox]
                    iou_x1 = max(x, tx)
                    iou_y1 = max(y, ty)
                    iou_x2 = min(x + w, tx + tw)
                    iou_y2 = min(y + h, ty + th)
                    if iou_x1 < iou_x2 and iou_y1 < iou_y2:
                        overlapped = True
                        break
            if overlapped:
                continue

            roi_resized = cv2.resize(nueva_roi, image_size)
            input_data = roi_resized.astype('float32') / 255.0
            input_data = np.expand_dims(input_data, axis=0)
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            pred_index = np.argmax(output_data)
            prob = float(np.max(output_data))
            label = idx_to_class.get(pred_index, "desconegut")
            labels_text = f"{label} ({prob:.2f})"

            tracker = cv2.TrackerCSRT_create()
            tracker.init(imagen, (x, y, w, h))
            obj_id = str(uuid.uuid4())
            trackers[obj_id] = tracker
            labels[obj_id] = labels_text

            timestamp = datetime.now().isoformat()
            conn = sqlite3.connect("/home/pi/detecciones.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO detecciones (timestamp, clase, probabilidad)
                VALUES (?, ?, ?)
            ''', (timestamp, label, prob))
            conn.commit()
            conn.close()

            print(f"[{timestamp}] Detectat: {label} ({prob:.2f})")


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
