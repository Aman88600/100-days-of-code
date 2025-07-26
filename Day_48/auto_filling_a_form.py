from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# getting the chrome driver
driver = webdriver.Chrome(options=chrome_options)
# Going to app brewery website
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Filling the form

def fill_form(xpath, value):
    # Getting the element
    first_name = driver.find_element(By.XPATH, value=xpath)
    # Filling the element
    first_name.send_keys(value, Keys.ENTER)

# Filling the First Name input element
fill_form(xpath="/html/body/form/input[1]", value="Aman")
# Filling the Last Name input element
fill_form(xpath="/html/body/form/input[2]", value="Basoya")
# Filling the email
fill_form(xpath="/html/body/form/input[3]", value="aman@gmail.com")

sleep(5)
driver.quit()