from picamera2 import Picamera2
import cv2
import numpy as np
import time
import tflite_runtime.interpreter as tflite
import sqlite3
from datetime import datetime

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

idx_to_class = {0: "arandela", 1: "clau", 2: "femella", 3: "cargol"}
image_size = (128, 128)

conn = sqlite3.connect("/home/pi/deteccions.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS deteccions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        classe TEXT,
        probabilitat REAL
    )
''')
conn.commit()
conn.close()

def detectar_peces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contorns, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    peces = []
    for cnt in contorns:
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > 500:
            roi = frame[y:y+h, x:x+w]
            peces.append((x, y, w, h, roi))
    return peces

def guardar_a_base_de_dades(classe, probabilitat):
    timestamp = datetime.now().isoformat()
    conn = sqlite3.connect("/home/pi/deteccions.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO deteccions (timestamp, classe, probabilitat)
        VALUES (?, ?, ?)
    ''', (timestamp, classe, probabilitat))
    conn.commit()
    conn.close()


while True:
    frame = picam2.capture_array()
    imatge = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    peces = detectar_peces(imatge)
    for (x, y, w, h, roi) in peces:
        roi_redimensionat = cv2.resize(roi, image_size)
        input_data = roi_redimensionat.astype('float32') / 255.0
        input_data = np.expand_dims(input_data, axis=0)

        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])

        pred_index = np.argmax(output_data)
        pred_prob = np.max(output_data)
        etiqueta = idx_to_class.get(pred_index)

        guardar_a_base_de_dades(etiqueta, pred_prob)

        cv2.rectangle(imatge, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(imatge, f"{etiqueta} ({pred_prob:.2f})", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow("Classificació de Peces", imatge)

    time.sleep(0.3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
