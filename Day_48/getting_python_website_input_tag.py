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
# Getting the search bar
search_bar = driver.find_element(By.NAME, value="q")
# Getting the place holder attribute's value
print(search_bar.get_attribute("placeholder"))

# Getting the submit button using id
button = driver.find_element(By.ID, value="submit")
# Getting button size
print(button.size)

# Getting the link
link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(link.text)

driver.quit()