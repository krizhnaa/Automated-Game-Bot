from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url=URL)

# while True:
cookie = driver.find_element(By.ID, value="cookie")
cookie.click()

our_money = driver.find_element(By.CSS_SELECTOR, value="#money")
print(our_money.text)

store_monies = driver.find_elements(By.CSS_SELECTOR, value="#store")


driver.quit()