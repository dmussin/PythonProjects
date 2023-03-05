from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Const
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "ChromeDriverManager().install()"
S = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=S)
class InternetSpeedTwitterBot:
    def __int__(self):
        self.driver = webdriver.Chrome(service=S)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        driver.get("https://www.speedtest.net")
        time.sleep(7)

        self.privacy = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[2]/div/div/button[2]')
        self.privacy.click()
        print("privacy")
        time.sleep(6)

        self.go = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go.click()
        print("go")
        time.sleep(50)

        self.back_to_test = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        self.back_to_test.click()
        print("back to test")
        time.sleep(5)

        self.down = float(driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(f"Download: {self.down}")

        self.up = float(driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f"Upload: {self.up}")



    def tweet_at_provider(self):
        driver.get("https://www.twitter.com")
        print("twitter")

        time.sleep(10)

        self.log_in = driver.find_element(By.XPATH,
                                     '/html/body/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        self.log_in.click()
        print("login clicked")

        time.sleep(5)

        self.username = driver.find_element(By.XPATH,
                                       '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.username.send_keys("python.musin@gmail.com")
        self.username.send_keys(Keys.ENTER)
        print("username")

        time.sleep(3)

        username_2 = driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_2.send_keys("pythonmusin")
        username_2.send_keys(Keys.ENTER)
        print("username_2")

        time.sleep(3)

        password = driver.find_element(By.XPATH,
                                       '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys("Dony1319LKS")
        password.send_keys(Keys.ENTER)
        print("password typed")

        time.sleep(15)

        # whats_happening = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        # whats_happening.click()
        # print("whats happening")

        message = driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        message.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up when I pay for 500mb?")
        print("message drafted")

        time.sleep(3)

        tweet = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet.click()
        print("Tweeted")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

while True:
    pass