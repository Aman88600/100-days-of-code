from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# getting the chrome driver
driver = webdriver.Chrome(options=chrome_options)
# Going to wiki
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Getting the number
number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(number.text)
driver.quit()