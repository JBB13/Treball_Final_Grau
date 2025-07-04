
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = "https://www.istockphoto.com/es/search/more-like-this/1096372258?assettype=image&phrase=metal%20nut"
driver.get(url)
time.sleep(5)  


output_folder = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//femelles"
os.makedirs(output_folder, exist_ok=True)

images = driver.find_elements(By.TAG_NAME, "img")
descargadas = 0

for i, img in enumerate(images):
    img_url = img.get_attribute("src")
    
    if img_url and "media.istockphoto" in img_url:
        try:
            img_data = requests.get(img_url).content
            img_path = os.path.join(output_folder, f"tuerca_{i+1}.jpg")
            with open(img_path, "wb") as handler:
                handler.write(img_data)
            print(f"Imatge descarregada: {img_path}")
            descargadas += 1
        except Exception as e:
            print(f"Error en descarregar la imatge: {e}")

print(f"Descàrrega completa. Total imatges descarregades: {descargadas}")
driver.quit()
