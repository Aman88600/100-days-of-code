from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime

# Launch the browser
driver = webdriver.Chrome()

# Load local Cookie Clicker
driver.get("http://127.0.0.1:8000")  # ✅ your local server

# wait 5 seconds
sleep(5)

# Clicking the english language
english_language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
english_language.click()
sleep(5)
cookie = driver.find_element(By.ID, value="bigCookie")
i = 0
time_1 = datetime.now()

def get_big(element_list: list) -> int:
    high = element_list[0]
    for i in element_list:
        if i > high:
            high = i
    return high

def remove_comma(number):
    numbers = number.split(',')
    true_number = 0
    for i in numbers:
        true_number += int(i)
    return true_number
while True:
    cookie.click()
    if i % 1_00 == 0 and i != 0:
        time_2 = datetime.now()
        time_elapsed = int((str(time_2 - time_1).split('.')[0].split(':'))[1])
        print(time_elapsed)
        if time_elapsed % 5 == 0 and time_elapsed != 0:
            products = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
            # Getting the highest price
            # highest_price = str(products[0]).split("\n")[1]
            element_list = []
            for product in products:
                element = int(remove_comma(product.text.split('\n')[1]))
                print(element)
                element_list.append(element)
            big_element = get_big(element_list)
            for product in products:
                element = int(remove_comma(product.text.split('\n')[1]))
                if element == big_element:
                    try:
                        consent_btn = driver.find_element(By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all")
                        consent_btn.click()
                        print("Cookie consent dismissed.")
                    except:
                        pass
                    finally:
                        product.click()
                        print("Clicked....")
    # Increment
    i += 1

# closing all tabs
# driver.quit()