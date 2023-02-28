import manager as manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver.get("https://www.amazon.de/-/en/Cobear-Customisable-Leather-Non-Slip-Waterproof/dp/B0BKFQRJ9V/ref=psdc_79899031_t3_B0BLRTVTZV")
# # price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# #
# # print(price.text)
#
# driver.get("https://www.python.org")
# # search_bar = driver.find_element(By.NAME, "q")
# # print(search_bar.get_attribute("placeholder"))
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# bug = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug.text)



# ------------------------------------------------------------------------- #
# driver.get("https://www.python.org")
#
# events_dict = {}
#
# events_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# # for event in events_time:
# #     print(event.text)
# #
# # for event in event_names:
# #     print(event.text)
#
# for n in range(len(events_time)):
#     events_dict[n] = {
#         "time": events_time[n].text,
#         "name": event_names[n].text
#     }
#
# print(events_dict)


# ------------------------------------------------------------------------- #

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Clicking on link using xpath
# statistic = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# statistic = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# statistic.click()

# Clicking on link using the link name
# all_portals = driver.find_element(By.LINK_TEXT, "Wikibooks")
# all_portals.click()

# Typing in form
# search_button = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
# search_button.click()

# Importing keys
# from selenium.webdriver.common.keys import Keys
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
#
# while True:
#     pass


# -------------------------------------------- #
import time

# timeout = time.time() + 5
# five_min = time.time() + 60*5 # 5minutes
#
# driver.get("http://orteil.dashnet.org/experiments/cookie/")
#
# cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
#
# #Get upgrade item ids.
# items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
# money = driver.find_element(By.XPATH, '//*[@id="money"]')
# money_form = int(money.text)
# print(money_form)

# while True:
#     cookie.click()
#
#     # Check every 5 sec
#     if time.time() > timeout:
#
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_price = []
#
#         # Convert <b> text into int price
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_price.append(cost)
#
#         # Create dict of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_price)):
#             cookie_upgrades[item_price[n]] = item_ids
#
#         # Get current cookie count
#         money_element = driver.find_element(By.ID, "money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element(By.ID, to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#         # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#         print(cookie_per_s)
#         break

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

game_is_on = True
count = 1
time_out = time.time() + 5
i_want_30 = time.time() + (60 * 30)

def click():
    cookie.click()


def buy_items():
    item_prices = driver.find_elements(By.CSS_SELECTOR, "#store b ")
    for item in reversed(item_prices):

        if item.text != "":

            price = int(item.text.replace(",", "").split("-")[1].replace(" ", ""))
            item_id = item.text.split("-")[0].replace(" -  ", "").rstrip()
            final_id = f"buy{item_id}"

            if money >= price:
                store_item = driver.find_element(By.ID, final_id)
                store_item.click()
                print(f"buying {item_id}")
                return


while game_is_on:
    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    click()
    if time.time() > time_out:
        buy_items()
        time_out = time.time() + 5
        if time.time() > i_want_30:
            game_is_on = False
            cookie_per_min = driver.find_element(By.ID, "cps")
            print(cookie_per_min)

driver.close()()