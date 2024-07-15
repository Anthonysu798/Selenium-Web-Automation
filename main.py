from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(excutable_path="chromedriver.exec")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

# For slow internet connection
# Wait 5 sec for the element to exists
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
)

# Get element className
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# Clear element then send the key
input_element.clear()

# Type the text and hit enter key
input_element.send_keys("Anthony Su.me" + Keys.ENTER)

# For slow internet connection
# Wait 5 sec for the element to exists
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Anthony Su"))
)

# Clicked on the link
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Anthony Su")
link.click()


# Close Chrome in 10 second
time.sleep(10) # Sleep for 10 sec

driver.quit()