from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


from selenium.common.exceptions import NoSuchElementException

EMAIL = "python.musin@gmail.com"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://tinder.com/")
PW = "Dony1319LKS5/"

# language = driver.find_element(By.XPATH, '//*[@id="c-60880778"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
# language.click()

time.sleep(2)

sign_in = driver.find_element(By.XPATH, '//*[@id="c-60880778"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
sign_in.click()

time.sleep(3)

more_options = driver.find_element(By.XPATH, '//*[@id="c160459658"]/main/div/div/div[1]/div/div/div[3]/span/button')
more_options.click()
print("Button more_options is clicked")

time.sleep(3)

fb_login = driver.find_element(By.XPATH, '//*[@id="c160459658"]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button')
fb_login.click()
print("Button facebook is clicked")

#Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]')
cookies.click()
print("Button cookies is clicked")

time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PW)
password.send_keys(Keys.ENTER)

# time.sleep(2)
# continue_fb = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div')
# continue_fb.click()
#
# driver.switch_to.window(base_window)
# print(driver.title)
#
# #revert back to the base_window and verify by printing the title
#
# time.sleep(5)
# location = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]')
# location.click()
# time.sleep(5)
# notification = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[2]')
# notification.click()
# time.sleep(5)
# night_version = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div[2]/button')
# night_version.click()
#
# for n in range(3):
#     time.sleep(10)
# try:
#     print("Disliked")
#     time.sleep(10)
#     body = driver.find_element(By.CSS_SELECTOR, value="body")
#     body.send_keys(Keys.LEFT)
#
# except ElementClickInterceptedException:
#     time.sleep(2)
#     pass


while True:
    pass