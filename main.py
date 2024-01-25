from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url=URL)

store_dict = {}

cookie = driver.find_element(By.ID, value="cookie")
timeout = time.time() + 5

while True:
    cookie.click()
    if time.time() > timeout:
        our_money_str = driver.find_element(By.CSS_SELECTOR, value="#money")
        our_money = int(our_money_str.text)

        id_list = []
        store_ids = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for ids in store_ids:
            here = ids.get_attribute("id")
            id_list.append(here)

        money_list =[]
        store_monies = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

        for item in store_monies:
            # item_id = item.get_attribute("id")
            element_text = item.text
            if element_text != "":
                store_money = int(element_text.split("-")[1].replace(",", ""))
                money_list.append(store_money)

        for n in range(len(money_list)):
            store_dict[money_list[n]] = id_list[n]

        affordable_upgrades = {}
        for cost, id in store_dict.items():
            if our_money > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()
        timeout = time.time() + 5
        # time.sleep(5)


# driver.quit()