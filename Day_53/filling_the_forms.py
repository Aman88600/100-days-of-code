from get_zillio_listings import get_values

# Getting the required values
values = get_values()
addresses = values[0]
prices = values[1]
links = values[2]

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


# Filling the form and click the button
def fill_and_click(address, price, link):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfeR7PFJ3GJmyn2_KLo-Wo74wfr5H-RVJtescA9evfR_jGB-A/viewform?usp=header")
    def fill_form(xpath, value):
        # Getting the element
        first_name = driver.find_element(By.XPATH, value=xpath)
        # Filling the element
        first_name.send_keys(value, Keys.ENTER)
    # Filling the Address
    fill_form(xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', value=address)
    # Filling the Price
    fill_form(xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input', value=price)
    # Filling Link
    fill_form(xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', value=link)
    # Click the submit button
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
iteration_number = len(addresses) - 1
i = 0 
while i <= iteration_number:
    fill_and_click(address=addresses[i], price=prices[i], link=links[i])
    i += 1

# sleep(5)s
driver.quit()

