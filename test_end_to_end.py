import csv
from driver_setup import setup_driver
from login import homepage, login
from CRM_form import crm_displayed, crm_form, lead_details, crm_leads, lead_details_page
from selenium.webdriver.common.by import By
import time

def complete_test():
    driver = setup_driver()

    try:
        login(driver)

        homepage(driver)

        crm_displayed(driver)

        crm_form(driver)

        lead_details(driver)

        crm_leads(driver)

        lead_details_page(driver)

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    complete_test()





