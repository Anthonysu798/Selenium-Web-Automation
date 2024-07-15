from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(excutable_path="chromedriver.exec")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10) # Sleep for 10 sec

driver.quit()