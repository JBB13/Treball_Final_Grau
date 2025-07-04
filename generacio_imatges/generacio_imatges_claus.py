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

urls = ["https://www.google.com/search?q=one%20metal%20nail%20photo&udm=2&tbs=rimg:CRgJMRf-kQ1PYcSq8JremHzRsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBoQuIIBahcKEwjQzafsp86MAxUAAAAAHQAAAAAQDw&biw=1707&bih=811&dpr=1.13#vhid=I5f8fABLQNueeM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CQnLfV9-MVwsYSLocmM97POdsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQBg",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:Cft9-GFOCCyNYVfS0Dkm87YmsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQDw",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CdL2dm3WLPzZYUvumRMUBvk_1sgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQGA",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:Cfvd0oDRc3OBYSvySGKlwTMNsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQIQ",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CT4pM0cKFU4AYbXxdD3VxwVFsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQKg",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CRUWWlgu-txXYTwpfV9a9F8zsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQPA",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CTZX3uI4FeGDYW4-WmAwCjmDsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQRQ",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CT7HzXYvsJrBYbXxdD3VxwVFsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQTg",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CT6nPRG_1c6pZYcSq8JremHzRsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIw6_0p86MAxUAAAAAHQAAAAAQaQ",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CemxvhTQERKHYUJ5Da7WodSOsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahgKEwjIw6_0p86MAxUAAAAAHQAAAAAQhAE",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CemxvhTQERKHYUJ5Da7WodSOsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahgKEwjIw6_0p86MAxUAAAAAHQAAAAAQhAE",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&udm=2&tbs=rimg:CRgJMRf-kQ1PYcSq8JremHzRsgIAwAIA2AIA4AIA&rlz=1C1UEAD_esES1124ES1124&hl=ca&sa=X&ved=0CBoQuIIBahcKEwjQzafsp86MAxUAAAAAHQAAAAAQDw&biw=1707&bih=811&dpr=1.13#vhid=Cct9X34xXCxXiM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CQnLfV9-MVwsYSLocmM97POdsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjAteqN1s-MAxUAAAAAHQAAAAAQBg#vhid=jmeWQ1S20wqemM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CY5nlkNUttMKYbE2V_16VXlCAsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiI4MuQ1s-MAxUAAAAAHQAAAAAQBg#vhid=eidwHOKsJwrOnM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CXoncBzirCcKYfpCmyRX9PCNsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwionOOT1s-MAxUAAAAAHQAAAAAQBg#vhid=-pYWrgALBWDoUM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CfqWFq4ACwVgYUJ5Da7WodSOsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiwpI6X1s-MAxUAAAAAHQAAAAAQBw#vhid=f8hBHvc5LMXkKM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CX_1IQR73OSzFYREBjgB1C6dbsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiQrPuY1s-MAxUAAAAAHQAAAAAQBw#vhid=9vJInN_QibvpBM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CfbySJzf0Im7YSSZBOWpTDwdsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiwna6b1s-MAxUAAAAAHQAAAAAQDw#imgrc=qo1RrHS_R1fJyM&imgdii=1_Fd9q02HfA7wM",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CdfxXfatNh3wYQSn-S8wqoTCsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjIv4ui1s-MAxUAAAAAHQAAAAAQJg#vhid=brO4rk6PnggHmM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CW6zuK5Oj54IYQSn-S8wqoTCsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjAi56r1s-MAxUAAAAAHQAAAAAQBg#vhid=dd5nDfCW_yUcYM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CXXeZw3wlv8lYSTXaGuLFIpXsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBwQuIIBahcKEwigysOw1s-MAxUAAAAAHQAAAAAQBw#vhid=QsdJhA6CZcZhBM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CULHSYQOgmXGYYy6D4LOUnvpsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjAyvGy1s-MAxUAAAAAHQAAAAAQFw#vhid=9rhKnf8MEeFTyM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:Cfa4Sp3_1DBHhYTP25GnQYppLsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjQ4NWE2M-MAxUAAAAAHQAAAAAQBw#vhid=18Qs8OHIqXSyiM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CdfELPDhyKl0YdbkXTG5PX9PsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwi42PuH2M-MAxUAAAAAHQAAAAAQCA#vhid=0FleJhLTyM9VYM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CdBZXiYS08jPYXsRYapziq8ksgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwj41d6K2M-MAxUAAAAAHQAAAAAQDw#vhid=9CAGoTZb01UWjM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CfQgBqE2W9NVYUmgaRTMukaLsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwjon8qO2M-MAxUAAAAAHQAAAAAQKg#vhid=HcXIg123m9kSKM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CR3FyINdt5vZYRq-F3BXsNb9sgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwi48MOX2M-MAxUAAAAAHQAAAAAQBw#vhid=BWvprHiShfUQoM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CQVr6ax4koX1YZMgb5mfHPMssgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwj45tWZ2M-MAxUAAAAAHQAAAAAQBw#vhid=c2ZqmSsBLF4foM&vssid=mosaic",
        "https://www.google.com/search?q=one%20metal%20nail%20photo&hl=ca&tbs=rimg:CXNmapkrASxeYRuuj9-BHetRsgIAwAIA2AIA4AIA&udm=2&rlz=1C1UEAD_esES1124ES1124&sa=X&ved=0CBoQuIIBahcKEwiI3MOb2M-MAxUAAAAAHQAAAAAQBw",
        
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

output_folder = "C://Users//janbi//Desktop//pen//SanDisk//documentos//Universitat//UPC//Q8//TFG//imatges//clavos"

os.makedirs(output_folder, exist_ok=True)


for i, img_url in enumerate(img_urls):
        try:
            response = requests.get(img_url, stream=True, timeout=10)
            if response.status_code == 200:
                image_path = os.path.join(output_folder, f"clau_{i+1}.jpg")
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