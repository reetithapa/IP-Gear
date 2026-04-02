import csv
from driver_setup import setup_driver
from login import homepage, login
from CRM_form import crm_displayed, internet_sales, lead_details, crm_leads, lead_details_page, my_leads, entry_source, search_leads, IPTV_sales, internet_iptv
from all_leads import all_leads, entry_sources, sales_process, search_lead, select_date
from subscriber import create_subscriber, subscriber_dashboard
from tickets import tickets_page
from inventory import add_product, product_search
from selenium.webdriver.common.by import By
import time

def complete_test():
    driver = setup_driver()

    try:
        login(driver)

        homepage(driver)

        crm_displayed(driver)

        #internet_sales(driver)

        #IPTV_sales(driver)

        internet_iptv(driver)

        lead_details(driver)

        crm_leads(driver)

        lead_details_page(driver)

        #my_leads(driver)

        #all_leads(driver)

        #entry_source(driver)

        #sales_process(driver)

        #entry_sources(driver)

        #search_lead(driver)

        #search_leads(driver)

        #select_date(driver)

        #tickets_page(driver)
        #create_subscriber(driver)
        #add_product(driver)
        #product_search(driver)
        #subscriber_dashboard(driver)

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    complete_test()





