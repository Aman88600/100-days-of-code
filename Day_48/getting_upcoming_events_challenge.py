from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# getting the chrome driver
driver = webdriver.Chrome(options=chrome_options)
# Going to python website
driver.get("https://www.python.org/")

# Getting the dates and the names
dates = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

# Final dictionary
event_dictionary = {}
event_list  = []
# Iterating over it
for date in dates:
    element_list = (date.text).split("\n")
    event_list.append(element_list)

i = 0
while i < len(event_list):
    event_dictionary[i] = {"time" : event_list[i][0], "name" : event_list[i][1]}
    i += 1
    

print(event_dictionary)

driver.quit()