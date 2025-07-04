import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


a = 0


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

urls = ["https://www.google.com/search?q=one%20metal%20screw&udm=2&tbs=rimg:CZJRR7vXO5XgYRgURgH6NGJtsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBsQuIIBahcKEwiopJS8k86MAxUAAAAAHQAAAAAQBw&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CRP6qct8iGqRYQemdH286iINsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBwQuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQBw#vhid=BHz7QHf2hToM8M&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CQEHj-jx3QiDYYFj5IJ4GbFRsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBwQuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQNA",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CdujMj0AqSpiYYvYV-vioOblsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CCAQuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQPQ",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CR5GCkhpPg0eYeZ4rFLUjllbsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBwQuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQRg",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CXZTKKhlHQZ8YdUjYjWAQKzZsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CB0QuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQTw",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CQeQGqasIKfMYZhjevi6jveKsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CB0QuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQWA",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CQY1OblnfS-yYcIfWNFv1oJHsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CB0QuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQYQ",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CXIOtJ2aHRg8Ybx5_1AE_1xjXqsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBwQuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQag",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&tbs=rimg:CQR8-0B39oU6YVzJOCFPIPUMsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiw1c7tk86MAxUAAAAAHQAAAAAQBw",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CZ-5jYWfLaMlYRxuTf1IjxAOsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBsQuIIBahcKEwjA79rTk86MAxUAAAAAHQAAAAAQcg",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:Cc9QjcaHzowgYXqGamWkSeBMsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahgKEwjA79rTk86MAxUAAAAAHQAAAAAQgwE",
        "https://www.google.com/search?q=one%20metal%20screw&hl=ca&udm=2&tbs=rimg:CX6l6h9JGHkwYay7e2a8r7mPsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBwQuIIBahgKEwjA79rTk86MAxUAAAAAHQAAAAAQiwE"]
img_urls = []



for url in tqdm(urls, desc="Descrregant Imatges", unit="url"):
    driver.get(url)
    time.sleep(1)

    for _ in range(3):
        driver.execute_script("window.scrollBy(0,4000)")  
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    image_tags = soup.find_all("img")

     
    with open("links.txt", "a") as f:
        for img in image_tags:
            img_url = img.get("src") or img.get("data-src")
            if img_url and img_url.startswith("http"):
                f.write(img_url + ",")  
                time.sleep(1)
                img_urls.append(img_url)
                print("foto")

output_folder = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//imatges//tornillos"

os.makedirs(output_folder, exist_ok=True)


for i, img_url in enumerate(img_urls):
        try:
            response = requests.get(img_url, stream=True, timeout=10)
            if response.status_code == 200:
                image_path = os.path.join(output_folder, f"tornillo_{i+1}.jpg")
                with open(image_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            file.write(chunk)
                            time.sleep(1)
            else:
                print(f" No sha pogut descarregar: {img_url}.")
        except requests.exceptions.RequestException as e:
            print(f"Error descarregar {img_url}: {str(e)}")
        except Exception as e:
            print(f"Error amb {img_url}: {str(e)}")