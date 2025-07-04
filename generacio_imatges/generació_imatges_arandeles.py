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

urls = ["https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CeOvj4dp-qeVYThPrfEq9-q9sgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB4QuIIBahcKEwj4x9mByZOMAxUAAAAAHQAAAAAQBg&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CYL5Ai4qr0rFYdoa8QnyIrSwsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB0QuIIBahcKEwj4x9mByZOMAxUAAAAAHQAAAAAQDg",
        "https://www.google.com/search?q=one%20metal%20washer&hl=ca&tbs=rimg:Cc41_1yKvII4JYf2EkN-jBPfQsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CCAQuIIBahcKEwiQ156gyZOMAxUAAAAAHQAAAAAQBg&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&hl=ca&tbs=rimg:CT6o958VMTBLYemsqqX4o4xPsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CB8QuIIBahcKEwj4uOaoyZOMAxUAAAAAHQAAAAAQDw",
        "https://www.google.com/search?q=one%20metal%20washer&hl=ca&tbs=rimg:Cftanov8r6gLYQItvCZfw4iDsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CB0QuIIBahcKEwjwi82xyZOMAxUAAAAAHQAAAAAQBw",
        "https://www.google.com/search?q=one%20metal%20washer&hl=ca&tbs=rimg:CSk6nynf1jvuYd_1LwENmb6YVsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwi4qpq8yZOMAxUAAAAAHQAAAAAQFw",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CeOvj4dp-qeVYThPrfEq9-q9sgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBwQuIIBahcKEwjQibCD7ZOMAxUAAAAAHQAAAAAQBg&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CYL5Ai4qr0rFYdoa8QnyIrSwsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CCEQuIIBahcKEwjA_ZaE7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CVJiI9yhS6XwYYSKJ_19YYfDqsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB4QuIIBahcKEwjYgLqF7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CWbVTRSBpGZZYQy-hURf1wbgsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CCEQuIIBahcKEwiIu8iG7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one+metal+washer&udm=2&tbs=rimg:CV6EvrIZvJmFYWlvXFa84yNPsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB4QuIIBahcKEwiw5s6H7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25&sxsrf=AHTn8zrtycDQrrFYTDbrkaZwdhyODN4Q1Q:1742308575336&sec_act=sr",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CZglMbmPsSp6Yffk3RsublKOsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB8QuIIBahcKEwjY4eSI7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CbeDOF5c8b3BYUil2EdPZQfNsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB0QuIIBahcKEwiAhpeK7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CbgVsO0fg70bYXM5lcqDqX41sgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB4QuIIBahcKEwjQ9JiN7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one%20metal%20washer&udm=2&tbs=rimg:CT2ijtL8cjccYZpr7zZQmyYBsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CCAQuIIBahcKEwjQnbKO7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25",
        "https://www.google.com/search?q=one+metal+washer&udm=2&tbs=rimg:CUfv20hOLYf-YXKrPj95U3KksgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CCEQuIIBahcKEwj41t2P7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25&sxsrf=AHTn8zoEgA_WNsYIenaBtbT6INAY0NGppg:1742308590550&sec_act=sr",
        "https://www.google.com/search?q=one+metal+washer&udm=2&tbs=rimg:CSIaZ8nITizUYbQQ8ArmOneXsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB0QuIIBahcKEwjAmbST7ZOMAxUAAAAAHQAAAAAQBw&biw=1536&bih=730&dpr=1.25&sxsrf=AHTn8zrEzrHnBgXT45a5XvTGw_mR_52ZlA:1742308593375&sec_act=sr",
            ]

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

output_folder = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//imatges//arandeles"

os.makedirs(output_folder, exist_ok=True)


for i, img_url in enumerate(img_urls):
        try:
            response = requests.get(img_url, stream=True, timeout=10)
            if response.status_code == 200:
                image_path = os.path.join(output_folder, f"arandela_{i+1}.jpg")
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