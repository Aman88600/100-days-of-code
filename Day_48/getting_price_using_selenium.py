from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# getting the chrome driver
driver = webdriver.Chrome(options=chrome_options)
# Going to amazon website
driver.get("https://www.amazon.in/Acer-Ryzen5-6600H-Windows-Graphics-AN515-46/dp/B081V7SM83/ref=sr_1_2?nsdOptOutParam=true&sr=8-2")

try :
    # Getting and clicking the continue button
    driver.find_element(By.CLASS_NAME, value='a-button-text').click()
except :
    print("No continue button")
finally:
    # Getting the price
    price2 = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[5]/div[4]/div[14]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]')
    print(price2.get_attribute("innerText"))

# Waiting for 5 seconds
# sleep(5)

# closing the browser
# driver.close() # close only closes one tab
# driver.quit() closes the web browser entriely
driver.quit()