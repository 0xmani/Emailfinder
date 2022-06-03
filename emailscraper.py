from ctypes.wintypes import tagRECT
from click import option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from PIL import Image
import pytesseract
import sys

domain = "https://phonebook.cz/"

try:
    target = sys.argv[1]
except:
    print("Usage: python3 emailscraper.py <target>")
    sys.exit()

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get(domain)
driver.find_element(By.XPATH, '//*[@id="domain"]').send_keys(target)
driver.find_element(By.XPATH, '//*[@id="submit1"]').send_keys(Keys.ENTER)
test = driver.find_element(By.XPATH, '//*[@id="result"]')
time.sleep(10)
test.screenshot("test.png")
driver.close()
#image to txt convertion

image = "test.png"
text = str(pytesseract.image_to_string(Image.open(image), lang="eng")).split("\n")
for i in text:
    for s in i:
        if s == "@":
            k = i.replace(" ","")
            k = k+"\n"
            print(k)
            file = open(f"{target}.txt", "a")
            file.write(k)