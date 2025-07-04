import os
import cv2
import numpy as np
from tqdm import tqdm

carpeta_entrada = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//imatges//arandelas_final"
output_folder = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//imatges//arandelas_final_1"
os.makedirs(output_folder, exist_ok=True)

mida_estandard_imatge = (256, 256)

for nom_imatge_original in tqdm(os.listdir(carpeta_entrada)):
    if not nom_imatge_original.lower().endswith(".jpg"):
        continue

    ruta_imatge = os.path.join(carpeta_entrada, nom_imatge_original)

    imatge = cv2.imread(ruta_imatge)
    if imatge is None:
        print(f"No s'ha pogut llegir la imatge: {ruta_imatge}")
        continue

    imatge_redimensionada = cv2.resize(imatge, mida_estandard_imatge)

    imatge_grisos = cv2.cvtColor(imatge_redimensionada, cv2.COLOR_BGR2GRAY)

    _, imatge_binaria = cv2.threshold(imatge_grisos, 240, 255, cv2.THRESH_BINARY_INV)

    nucli = np.ones((3, 3), np.uint8)
    imatge_binaria = cv2.morphologyEx(imatge_binaria, cv2.MORPH_CLOSE, nucli)

    edges_canny = cv2.Canny(imatge_binaria, 50, 150, apertureSize=3)

    contorns, _ = cv2.findContours(edges_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, contorn in enumerate(contorns):
        if contorn is None or len(contorn) < 3:
            continue

        contorn_array = np.squeeze(contorn).astype(np.float32)
        if contorn_array.ndim != 2 or contorn_array.shape[0] < 3 or contorn_array.shape[1] != 2:
            continue

        area = cv2.contourArea(contorn_array)
        if area <= 500:
            continue 

        mascara = np.zeros_like(imatge_grisos)
        cv2.drawContours(mascara, [contorn], -1, 255, thickness=cv2.FILLED)

        b, g, r = cv2.split(imatge_redimensionada)
        alfa = mascara
        resultat = cv2.merge([b, g, r, alfa])

        coordenades = cv2.findNonZero(mascara)
        if coordenades is not None:
            x, y, w, h = cv2.boundingRect(coordenades)
            imatge_retallada = resultat[y:y+h, x:x+w]
        else:
            imatge_retallada = resultat

        nom_sortida = f"{os.path.splitext(nom_imatge_original)[0]}_{i}.png"
        ruta_sortida = os.path.join(output_folder, nom_sortida)
        cv2.imwrite(ruta_sortida, imatge_retallada)
