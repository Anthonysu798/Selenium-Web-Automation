from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(excutable_path="chromedriver.exec")
driver = webdriver.Chrome(service=service)

# Open chrome and go to this link
driver.get("https://orteil.dashnet.org/cookieclicker/")

# The id of cookie button
cookie_id = "bigCookie"

# The amount of cookies id
cookies_id = "cookies"

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, cookie_id)))

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", "")) # Replace all cookies command with an empty string
    print(cookies_count)
