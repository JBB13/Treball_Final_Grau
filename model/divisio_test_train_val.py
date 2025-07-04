import os
import shutil
from sklearn.model_selection import train_test_split
import tqdm as tqdm

clases = ["arandelas","claus","femelles","tornillos"]

for i in tqdm.tqdm(clases):


    dataset_original = f"C:\\Users\\janbi\\Desktop\\pen\\SanDisk\\documentos\\Universitat\\UPC\\Q8\\TFG\\imatges\\imatges_soles\\{i}_sols"


    dataset_path = r"C:\Users\janbi\Desktop\pen\SanDisk\documentos\Universitat\UPC\Q8\TFG\imatges\imatges_algoritme_class"

  
    train_path = os.path.join(dataset_path, 'train', i)
    val_path = os.path.join(dataset_path, 'val', i)
    test_path  = os.path.join(dataset_path, 'test',i)
    
    # Crear carpetas si no existen
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)


    # Obtener lista de archivos de imágenes
    imagenes = [f for f in os.listdir(dataset_original) if os.path.isfile(os.path.join(dataset_original, f))]

    # Dividir la lista de archivos en entrenamiento y validación
    train_imgs, temp_imgs = train_test_split(imagenes, test_size=0.3, random_state=42)
    test_imgs, val_imgs = train_test_split(temp_imgs, test_size=0.5, random_state=42)


    for img in train_imgs:
        origen = os.path.join(dataset_original, img)
        destino = os.path.join(train_path, img)
        shutil.copy(origen, destino)

    # Mover imágenes de validación
    for img in test_imgs:
        origen = os.path.join(dataset_original, img)
        destino = os.path.join(test_path, img)
        shutil.copy(origen, destino)

    for img in val_imgs:
        origen = os.path.join(dataset_original, img)
        destino = os.path.join(val_path, img)
        shutil.copy(origen, destino)

    print(f"Imatges dividides")