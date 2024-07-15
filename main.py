from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(excutable_path="chromedriver.exec")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# Get element className
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# Now send the key to that element
input_element.send_keys("Tech with Anthony Su")

time.sleep(4) # Sleep for 10 sec

driver.quit()