import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time

from webdriver_manager.core import driver


def all_leads(driver):
    wait = WebDriverWait(driver, 10)

    leads = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='button']")))
    leads.click()
    time.sleep(2)

    all_leads = driver.find_element(By.XPATH, "//div[text()='All Leads']")
    all_leads.click()
    time.sleep(1)

    all_leads_list = driver.find_elements(By.XPATH, "//tbody/tr")
    number_of_leads = len(all_leads_list)
    print("Number of leads: " + str(number_of_leads))
    time.sleep(1)

    wait = WebDriverWait(driver, 10)
    lead_stage = driver.find_elements(By.XPATH, "//tbody//tr//td[5]")
    row_texts = []
    for i in range(len(lead_stage)):
        row = lead_stage[i]
        row_texts.append(row.text.strip())

    select_stage = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//body//div//div[contains(@data-testid,'child')]//div//div//div//div//div[1]//div[2]//select[1]")))

    select = Select(select_stage)
    time.sleep(1)

    stage_options = [option.text.strip() for option in select.options]
    print(stage_options)
    time.sleep(1)

    for stage_option_text in stage_options:
        select_stage = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "//body//div//div[contains(@data-testid,'child')]//div//div//div//div//div[1]//div[2]//select[1]")))

        select = Select(select_stage)
        time.sleep(2)

        select.select_by_visible_text(stage_option_text)
        time.sleep(2)

        displayed_element = driver.find_elements(By.XPATH, "//tbody//tr//td[5]")

        displayed_texts = [elem.text.strip() for elem in displayed_element]
        print(displayed_texts)

        if stage_option_text == "Select Stage":
            assert displayed_texts == row_texts, f"Expected all, but got '{displayed_texts}'"
            print(f"Verified: {stage_option_text} is displayed correctly")
            time.sleep(1)

        else:
            assert all(text == stage_option_text for text in
                       displayed_texts), f"Expected all rows to be '{stage_option_text}', but got {displayed_texts}"
            print(f"Verified: {stage_option_text} is displayed correctly")

            lead_state = driver.find_elements(By.XPATH, "//tbody//tr//td[6]")
            state_texts = []
            for i in range(len(lead_state)):
                row = lead_state[i]
                state_texts.append(row.text.strip())

            select_state = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  "//select[@class='placeholder:text-gray-300  !border-gray-200  slimbox   !text-gray-600 font-normal '][contains(.,'Select State')]")))
            select = Select(select_state)
            time.sleep(1)

            state_options = [option.text.strip() for option in select.options]
            print(state_options)
            time.sleep(1)

            for state_option_text in state_options:
                select.select_by_visible_text(state_option_text)
                time.sleep(3)

                displayed_element_state = driver.find_elements(By.XPATH, "//tbody//tr//td[6]")

                displayed_texts_state = [elem.text.strip() for elem in displayed_element_state]
                print(displayed_texts_state)
                time.sleep(2)

                if state_option_text == "Select State":
                    assert displayed_texts_state == state_texts, f"Expected all, but got '{state_texts}'"
                    print(f"Verified: {state_option_text} is displayed correctly")
                    time.sleep(2)

                else:
                    assert all(text == state_option_text for text in
                               displayed_texts_state), f"Expected all rows to be '{state_option_text}', but got {displayed_texts_state}"
                    print(f"Verified: {state_option_text} is displayed correctly")
                    time.sleep(2)
            driver.find_element(By.XPATH, "(//button[normalize-space()='Clear'])[1]").click()

def sales_process(driver):
    lead_sales_process = driver.find_elements(By.XPATH, "//tbody//tr//td[13]")
    row_text = []
    for i in range(len(lead_sales_process)):
        row = lead_sales_process[i]
        row_text.append(row.text.strip())

    wait = WebDriverWait(driver, 10)
    select_sales_process = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]//div[2]//select[1]")))

    select = Select(select_sales_process)
    time.sleep(2)

    options_sales_process = [option.text.strip() for option in select.options]
    print(options_sales_process)
    time.sleep(2)

    for options_sales_process_text in options_sales_process:
        #select_sales_process = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]//div[2]//select[1]")))
        #select = Select(select_sales_process)
        select.select_by_visible_text(options_sales_process_text)
        print(options_sales_process_text)
        time.sleep(3)

        displayed_element = driver.find_elements(By.XPATH, "//tbody//tr//td[13]")

        displayed_texts = [elem.text.strip() for elem in displayed_element]
        print(displayed_texts)
        time.sleep(3)

        if options_sales_process_text == "Select Sales Process":
            assert displayed_texts == row_text, f"Expected all, but got '{displayed_texts}'"
            print(f"Verified: {options_sales_process_text} is displayed correctly")
            time.sleep(3)
        else:
            assert all(text == options_sales_process_text for text in displayed_texts), f"Expected all rows to be '{options_sales_process_text}', but got {displayed_texts}"
            print(f"Verified: {options_sales_process_text} is displayed correctly")


def entry_sources(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-filter']//*[name()='svg']")))

    driver.find_element(By.XPATH, "//button[@class='btn-filter']//*[name()='svg']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//span[contains(@class,'box')])[14]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()

    #wait = WebDriverWait(driver, 10)

    leads = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='button']")))
    leads.click()
    time.sleep(2)

    all_leads = driver.find_element(By.XPATH, "//div[text()='All Leads']")
    all_leads.click()
    time.sleep(2)

    lead_sales_process = driver.find_elements(By.XPATH, "//tbody//tr//td[14]")
    row_text = []
    for i in range(len(lead_sales_process)):
        row = lead_sales_process[i]
        row_text.append(row.text.strip())

    entry_source = driver.find_element(By.XPATH, "(//select[contains(@class,'!text-gray-600 font-normal')])[4]")
    select = Select(entry_source)

    options_entry_source = [option.text.strip() for option in select.options]
    print(options_entry_source)
    time.sleep(2)

    for options_entry_source_text in options_entry_source:
        select.select_by_visible_text(options_entry_source_text)
        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//tbody//tr//td[14]")))
        displayed_element = driver.find_elements(By.XPATH, "//tbody//tr//td[14]")

        displayed_texts = [elem.text.strip() for elem in displayed_element]
        print(displayed_texts)
        time.sleep(3)

        if options_entry_source_text == "Select Entry Source":
            assert displayed_texts == row_text, f"Expected all, but got '{displayed_texts}'"
            print(f"Verified: {options_entry_source_text} is displayed correctly")
            time.sleep(3)

        else:
            assert all(text == options_entry_source_text for text in displayed_texts), f"Expected '{options_entry_source_text}', but got '{displayed_texts}'"
            print(f"Verified: {options_entry_source_text} is displayed correctly")
            time.sleep(3)

def search_lead(driver):
    wait = WebDriverWait(driver, 10)
    search_lead = driver.find_element(By.XPATH, "(//select)[5]")

    select = Select(search_lead)

    options_search_lead = [option.text.strip() for option in select.options]
    print(options_search_lead)
    time.sleep(2)

    for options_search_lead_text in options_search_lead:
        select.select_by_visible_text(options_search_lead_text)
        time.sleep(3)

        if options_search_lead_text == "Search Lead":
            print(f"Verified: {options_search_lead_text} is displayed correctly")
            time.sleep(3)

        else:
            enter_lead_id = driver.find_element(By.XPATH, "//input[@class='... placeholder:text-gray-300  font-normal newbox    ']")
            assert enter_lead_id.is_displayed(), "Enter lead id is not visible"
            assert driver.find_element(By.XPATH, "//input[@class='... placeholder:text-gray-300  font-normal newbox    ']").is_displayed()

            if driver.find_element(By.XPATH, "//input[@placeholder='Enter Lead ID']").is_displayed:
                  driver.find_element(By.XPATH, "//input[@placeholder='Enter Lead ID']").send_keys("25343")

            elif driver.find_element(By.XPATH, "//input[@placeholder='Enter Name']").is_displayed:
                driver.find_element(By.XPATH, "//input[@placeholder='Enter Name']").send_keys("Rose Mary")

            else:
                driver.find_element(By.XPATH, "//input[@placeholder='Enter Phone Number']").sned_keys("9873144486")

            print(f"{options_search_lead_text} is displayed correctly")
            time.sleep(3)

def select_date(driver, date_input_xpath, target_date):
    wait = WebDriverWait(driver, 10)
    date_obj = datetime.strptime(target_date, "%Y-%m-%d")

    date_input = wait.until(EC.element_to_be_clickable((By.XPATH, date_input_xpath)))
    date_input.click()

    year = date_obj.strftime("%Y")
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[contains(@class,'year')]//option[text()='{year}']"))).click()

    month = date_obj.strftime("%B")
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='react-datepicker__current-month']//option[text()='{month}']"))).click()

    day = date_obj.strftime("%d").lstrip("0")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//a[text()='{day}']")
    )).click()

#FROM_DATE = "2026-03-01"
#TO_DATE = "2026-03-20"

#select_date("//input[@name='from_date']", FROM_DATE)
#select_date("//input[@name='to_date']", TO_DATE)

#wait = WebDriverWait(driver, 10)
#search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]")))
#search_btn.click()







