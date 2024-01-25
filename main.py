from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url=URL)

# while True:
cookie = driver.find_element(By.ID, value="cookie")
cookie.click()

our_money_str = driver.find_element(By.CSS_SELECTOR, value="#money")
our_money = int(our_money_str.text)
# print(our_money)

store_dict = {}

store_monies = driver.find_elements(By.CSS_SELECTOR, value="#store div")
for item in store_monies[:len(store_monies)-1]:
    item_id = item.get_attribute("id")
    # print(item.text)
    parts1 = item.text.split('-')
    parts2 = parts1[1].split('\n')
    store_money = int(parts2[0].replace(',', ''))
    print(store_money)

    store_dict[item] = {
        item_id: store_money
    }

    # if our_money >= store_money:
    #
    #
    # time.sleep(5)

print(store_dict)

driver.quit()