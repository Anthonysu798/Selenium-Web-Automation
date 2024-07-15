from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(excutable_path="chromedriver.exec")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# Get element className
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# Type the text and hit enter key
input_element.send_keys("Anthony Su.me" + Keys.ENTER)

# Close Chrome in 10 second
time.sleep(10) # Sleep for 10 sec

driver.quit()