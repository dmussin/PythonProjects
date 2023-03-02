from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

EMAIL = "dan4ik377@gmail.com"
PASSWORD = "dony37713071991lks"

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3501762878&f_AL=true&f_E=2%2C3%2C4&f_PP=106978326&keywords=python%20developer&sortBy=R")
# driver.get("https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3501762878%26f_AL%3Dtrue%26f_E%3D2%252C3%252C4%26f_PP%3D106978326%26keywords%3Dpython%2520developer%26sortBy%3DR&trk=public_jobs_nav-header-signin")
sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')

sign_in.click()
time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "#username")
password = driver.find_element(By.CSS_SELECTOR, "#password")
submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

username.send_keys(EMAIL)
password.send_keys(PASSWORD)
submit_button.click()

all_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_elements(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone_code = driver.find_element(By.XPATHCLASS_NAME, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3399729042-9-phoneNumber-country"]')
        phone_code.send_keys("Czech")

        print("submit_button is pressed")
        #submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            print("submit_button is pressed because there was no next button")
            # submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)

while True:
    pass

