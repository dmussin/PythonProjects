from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from random import randint

# Const
INST_ACCOUNT = "python.learning"
USERNAME = "python.musin"
PASSWORD = "*bgPWpwW9@v$keN"

CHROME_DRIVER_PATH = "ChromeDriverManager().install()"
S = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=S)

class InstaFollower:
    def __int__(self):
        self.driver = webdriver.Chrome(service=S)


    def login(self):
        driver.get("https://www.instagram.com/")
        time.sleep(7)

        privacy = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        privacy.click()
        print("Privacy clicked")

        time.sleep(6)

        username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        print("Username entered")

        password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        print("Password entered + Enter")

        time.sleep(20)

        not_now = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        not_now.click()
        print("Not now clicked")

        time.sleep(10)

        not_now_again = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now_again.click()
        print("Not now clicked again")

        time.sleep(1)


    def find_followers(self):

        time.sleep(6)

        search = driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a')
        search.click()
        print("Search button clicked")

        time.sleep(6)

        search_input = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search_input.click()
        search_input.send_keys(INST_ACCOUNT)
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        print("Search Input Typed")
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # Get follower count
        list_items = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span')
        follower_count = list_items.text
        print(f"{INST_ACCOUNT} has {follower_count} followers")

        time.sleep(12)

        # Scroll the followers
        # scrollable = driver.find_element(by=By.CLASS_NAME, value="_aano")
        # print("scrollable")
        # for i in range(10):
        #     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable)
        #     time.sleep(2)
        #     print("scroll - scroll")


    def follow(self):

        followers = driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        print("Followers Clicked")

        followers.click()

        time.sleep(12)

        for i in range(1, 15):
            print(f"Round ({i})")
            if self.click_tag_exact("button", "Follow") == -1:
                print("Checking for cancel button")
                if self.click_tag_exact("button", "Cancel") == -1:
                    print("Scrolling!")
                    self.scroll_followers()



        # for i in range(1, 15):
        #     # Random time for a follow.
        #     delay = randint(2, 8)
        #     time.sleep(delay)
        #     follow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/button')
        #     print("Button found")
        #     if follow_button.text == "Follow":
        #         follow_button.click()
        #         print("Followed")
        #     else:
        #         pass



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

while True:
    pass