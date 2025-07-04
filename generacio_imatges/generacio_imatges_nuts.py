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

urls = ["https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:Cdqt_1nI9X83BYSWcqKMlSwzdsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBoQuIIBahcKEwjY7cC27piMAxUAAAAAHQAAAAAQBg&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:CbknuwFGCxAnYVMWkYXO9buMsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBwQuIIBahcKEwiA7p-t7piMAxUAAAAAHQAAAAAQBw&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:CcRpkmiC9MVRYcfDqPT8zi7-sgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBwQuIIBahcKEwi45b7C7piMAxUAAAAAHQAAAAAQBw&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:CRAqZxp9tETlYQbX8918CjsLsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBwQuIIBahcKEwiQ-NOb-piMAxUAAAAAHQAAAAAQBw&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:CZx3rn8pIIBlYdP0E9anHesPsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CB4QuIIBahcKEwiYvOP0-piMAxUAAAAAHQAAAAAQBw&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:Cdqt_1nI9X83BYSWcqKMlSwzdsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBoQuIIBahcKEwi43NW--5iMAxUAAAAAHQAAAAAQBg&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&hl=ca&tbs=rimg:CUIC9oBw67ZdYWx1RWqSxJ4DsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBsQuIIBahcKEwjgpa7L-5iMAxUAAAAAHQAAAAAQBg&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&hl=ca&tbs=rimg:CU5VUDap5lwaYY5uKo1V-xVPsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiguPLV-5iMAxUAAAAAHQAAAAAQGA&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&udm=2&tbs=rimg:CVGRnZQb-nK2YXnm3F8wBF5psgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBoQuIIBahcKEwiA4Ib2_piMAxUAAAAAHQAAAAAQBw&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&hl=ca&tbs=rimg:CSKqV-8kIs-dYXzjnbKSjGf9sgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwj43-f7_piMAxUAAAAAHQAAAAAQEA&biw=1707&bih=811&dpr=1.13",
        "https://www.google.com/search?q=one%20metal%20nut&hl=ca&tbs=rimg:CW0FZ79O4epPYZnspQWTSm4psgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CCEQuIIBahcKEwiYrtiJ_5iMAxUAAAAAHQAAAAAQEA&biw=1707&bih=811&dpr=1.13", 
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

output_folder = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//imatges//femelles"

os.makedirs(output_folder, exist_ok=True)


for i, img_url in enumerate(img_urls):
        try:
            response = requests.get(img_url, stream=True, timeout=10)
            if response.status_code == 200:
                image_path = os.path.join(output_folder, f"femella_{i+1}.jpg")
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