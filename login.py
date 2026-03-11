import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def homepage(driver):
    wait = WebDriverWait(driver, 10)
    Home = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='Home']")))
    if Home:
        print("Home page visible")
    time.sleep(1)


def login(driver):
    driver.maximize_window()
    driver.get("https://app-ispaas.dev.geniussystems.com.np")


    wait = WebDriverWait(driver, 10)
    #assert "login" in driver.current_url, "User is not directed to login page"

    login_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Sign in to your account']")))
    if login_page:
        print("Sign in to your account visible")

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()=' Clear']"))).click()

    with open ("testdata/users.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:

            company_code = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter code']")))
            company_code.send_keys("ctn")
            time.sleep(1)

            username = driver.find_element(By.ID, ":r1:")
            username.send_keys(row["username"])
            time.sleep(1)

            password = driver.find_element(By.ID, ":r2:")
            password.send_keys(row["password"])
            time.sleep(1)

            login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
            login_button.click()
            time.sleep(1)



