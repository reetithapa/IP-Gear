import csv
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def crm_displayed(driver):
    wait = WebDriverWait(driver, 10)

    CRM = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='CRM']")))
    CRM.click()
    time.sleep(2)

    assert "https://app-ispaas.dev.geniussystems.com.np/crm/" in driver.current_url

    print("CRM page is visible")
    time.sleep(5)
    #driver.find_element(By.XPATH, "//a[normalize-space()='Rose Mary']").click()

    New_Lead = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button']")))
    New_Lead.click()
    assert "/crm/lead/add" in driver.current_url
    time.sleep(1)

def internet_sales(driver):
    wait = WebDriverWait(driver, 10)

    with open ("testdata/lead.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:

         service_type = row["service_type"]
         first_name = row["first_name"]
         last_name = row["last_name"]
         preferred_username = row["preferred_username"]
         secondary_mobile = row["secondary_mobile"]
         landline = row["landline"]
         interested_product_group = row["interested_product_group"]
         interested_product = row["interested_product"]
         entry_source = row["entry_source"]
         lead_source = row["lead_source"]
         assign_to_me = row["assign_to_me"]
         lead_Status = row["lead_status"]
         existing_isp = row["existing_isp"]
         customer_id = row["customer_id"]
         profession = row["profession"]
         account_type = row["account_type"]
         test_select = row["test_select"]
         lead_type = row["lead_type"]
         address = row["address"]

         unique_primary_number = f"98{int(time.time()) % 100000000}"
         unique_number = print(unique_primary_number)
         Primary_mobile = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Primary Mobile']")))
         Primary_mobile.send_keys(unique_primary_number)
         time.sleep(1)

         #Service_type = Select(driver.find_element(By.XPATH, "(//select[@name='connection_type'])[1]"))
         #Service_type.select_by_visible_text(row["service_type"])
         time.sleep(1)

         First_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
         First_name.send_keys(row["first_name"])
         time.sleep(1)

         Last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
         Last_name.send_keys(row["last_name"])
         time.sleep(1)

         unique_emaill = f"test{int(time.time())}@gmail.com"
         unique_email = print(unique_emaill)
         Email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
         Email.send_keys(unique_emaill)
         time.sleep(1)

         unique_username = f"user{int(time.time()) % 100}"
         Preferred_username = driver.find_element(By.XPATH, "//input[@placeholder='Preferred Username']")
         Preferred_username.send_keys(unique_username)
         time.sleep(1)

         unique_secondary_number = f"984{int(time.time()) % 10000000}"
         Secondary_mobile = driver.find_element(By.XPATH, "//input[@placeholder='Secondary Mobile']")
         Secondary_mobile.send_keys(unique_secondary_number)
         time.sleep(1)

         unique_landline = f"43{int(time.time()) % 10000000}"
         Landline = driver.find_element(By.XPATH, "(//input[@placeholder='Landline'])")
         Landline.send_keys(unique_landline)
         time.sleep(1)

         Interested_product_group = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m")))
         Interested_product_group.click()
         Interested_product_option = driver.find_element(By.XPATH, "//div[text()='business-50 mbs']")
         Interested_product_option.click()
         # interested_product_group = driver.find_element(By.XPATH, "//div[text()='50 mbps packages']")
         # interested_product_group.select_by_visible_text("50 mbps packages")
         time.sleep(2)

         Interested_product_option = driver.find_element(By.CSS_SELECTOR, "div.react-select__control.css-1t1xqq")
         Interested_product_option.click()
         Interested_product = driver.find_element(By.XPATH, "//div[text()='Business - 50 mbps (Price:4444.711/Renew:3371.26)']")
         Interested_product.click()
         time.sleep(1)

         Entry_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='entry_source']"))
         Entry_source.select_by_visible_text(row["entry_source"])
         time.sleep(1)

         Lead_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_source']"))
         Lead_source.select_by_visible_text(row["lead_source"])
         time.sleep(1)

         Assigned = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'w-[9px] h-[9px] rounded-full absolute top-0.5 transition-transform duration-100 shadow-md translate-x-0.5 bg-white')])[2]")))
         Assigned.click()
         time.sleep(2)

         #assigned = Select(driver.find_element(By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m"))
         #assigned.select_by_visible_text(row["Assign_to_me"])
         #time.sleep(1)

         Lead_status = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_status']"))
         Lead_status.select_by_visible_text(row["lead_status"])
         time.sleep(1)

         Existing_isp = Select(driver.find_element(By.XPATH, "//select[@data-testid='existing_isp']"))
         Existing_isp.select_by_visible_text(row["existing_isp"])
         time.sleep(1)

         Unique_customer_ID = f"{int(time.time())%100}"
         Customer_ID = driver.find_element(By.XPATH, "(//input[@placeholder='Customer ID'])[1]")
         Customer_ID.send_keys(Unique_customer_ID)

         Profession = driver.find_element(By.XPATH, "(//input[@placeholder='Enter profession'])[1]")
         Profession.send_keys(row["profession"])
         time.sleep(1)

         Account_type = driver.find_element(By.XPATH, "//input[@placeholder='Enter account_type']")
         Account_type.send_keys(row["account_type"])

         Test_select = Select(driver.find_element(By.XPATH, "//select[@name='test_select']"))
         Test_select.select_by_visible_text(row["test_select"])
         time.sleep(1)

         #Lead_type = (driver.find_element(By.XPATH, "//div[@class='css-1xc3v61-indicatorContainer']//*[name()='svg']")).click()
         #time.sleep(2)
         #Lead_type_option = driver.find_element(By.XPATH, "//div[@class='css-1p3m7a8-multiValue']").click()
         #time.sleep(1)

         Remarks = driver.find_element(By.XPATH, "//textarea[contains(@placeholder,'Remarks')]")
         Remarks.send_keys(row["remarks"])

         #Address = driver.find_element(By.XPATH, "//input[@placeholder='Address']")
         #Address.send_keys(row["address"])
         Address = driver.find_element(By.XPATH, "//input[@placeholder='Search Maps']")
         Address.send_keys(row["address"])
         time.sleep(2)
         driver.find_element(By.XPATH, "//li[@class='bg-white rounded py-1 font-medium px-2 cursor-pointer'][2]").click()
         time.sleep(5)

         #Proceed = driver.find_element(By.XPATH, "(//button[normalize-space()='Proceed'])[1]")
         #Proceed.click()
         driver.find_element(By.XPATH, "//button[@data-info='submit-btn'][position()=2]").click()
         time.sleep(1)

         Success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
         if Success:
             print("New lead has been successfully created")

        #return unique_number, service_type, first_name, last_name, unique_email, unique_username, entry_source, lead_source, assign_to_me, existing_isp, address


def IPTV_sales(driver):
    username = driver.find_element(By.XPATH, "//div[@class='css-wa6cd9']")
    username.click()

    entry_source = Select(driver.find_element(By.XPATH, "//select[@name='entry_source']"))
    entry_source.select_by_visible_text("Digital")

    lead_source = Select(driver.find_element(By.XPATH, "//select[@name='lead_source']"))
    lead_source.select_by_visible_text("Advertisements")

    profession = driver.find_element(By.XPATH, "//input[@placeholder='Enter profession']")
    profession.send_keys("Scientist")

    account_type = driver.find_element(By.XPATH, "//input[@placeholder='Enter account_type']")
    account_type.send_keys("Testing")

    test_select = Select(driver.find_element(By.XPATH, "//select[@name='test_select']"))
    test_select.select_by_visible_text("opt1")

    lead_type = driver.find_element(By.XPATH, "opt1")
    lead_type.click()

    lead_options = driver.find_element(By.XPATH, "//div[@class='css-9jq23d']")
    lead_options.click()

    proceed = driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']")
    proceed.click()

def internet_iptv(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH,"//p[normalize-space()='Internet+IPTV']").click()

    with open ("testdata/lead.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            unique_primary_number = f"98{int(time.time()) % 100000000}"
            unique_number = print(unique_primary_number)
            Primary_mobile = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Primary Mobile']")))
            Primary_mobile.send_keys(unique_primary_number)
            time.sleep(1)

            # Service_type = Select(driver.find_element(By.XPATH, "(//select[@name='connection_type'])[1]"))
            # Service_type.select_by_visible_text(row["service_type"])
            time.sleep(1)

            First_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
            First_name.send_keys(row["first_name"])
            time.sleep(1)

            Last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
            Last_name.send_keys(row["last_name"])
            time.sleep(1)

            unique_emaill = f"test{int(time.time())}@gmail.com"
            unique_email = print(unique_emaill)
            Email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
            Email.send_keys(unique_emaill)
            time.sleep(1)

            unique_username = f"user{int(time.time()) % 100}"
            Preferred_username = driver.find_element(By.XPATH, "//input[@placeholder='Preferred Username']")
            Preferred_username.send_keys(unique_username)
            time.sleep(1)

            unique_secondary_number = f"984{int(time.time()) % 10000000}"
            Secondary_mobile = driver.find_element(By.XPATH, "//input[@placeholder='Secondary Mobile']")
            Secondary_mobile.send_keys(unique_secondary_number)
            time.sleep(1)

            unique_landline = f"43{int(time.time()) % 10000000}"
            Landline = driver.find_element(By.XPATH, "(//input[@placeholder='Landline'])")
            Landline.send_keys(unique_landline)
            time.sleep(1)

            Interested_product_group = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m")))
            Interested_product_group.click()
            Interested_product_option = driver.find_element(By.XPATH, "//div[text()='business-50 mbs']")
            Interested_product_option.click()
            # interested_product_group = driver.find_element(By.XPATH, "//div[text()='50 mbps packages']")
            # interested_product_group.select_by_visible_text("50 mbps packages")
            time.sleep(5)

            Interested_product_option = driver.find_element(By.CSS_SELECTOR, "div.react-select__control.css-1t1xqq")
            Interested_product_option.click()
            time.sleep(2)
            Interested_product = driver.find_element(By.XPATH,
                                                     "//div[text()='Business - 50 mbps (Price:4444.711/Renew:3371.26)']")
            Interested_product.click()
            time.sleep(1)

            Entry_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='entry_source']"))
            Entry_source.select_by_visible_text(row["entry_source"])
            time.sleep(1)

            Lead_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_source']"))
            Lead_source.select_by_visible_text(row["lead_source"])
            time.sleep(1)

            Assigned = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "(//div[contains(@class,'w-[9px] h-[9px] rounded-full absolute top-0.5 transition-transform duration-100 shadow-md translate-x-0.5 bg-white')])[2]")))
            Assigned.click()
            time.sleep(2)

            # assigned = Select(driver.find_element(By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m"))
            # assigned.select_by_visible_text(row["Assign_to_me"])
            # time.sleep(1)

            Lead_status = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_status']"))
            Lead_status.select_by_visible_text(row["lead_status"])
            time.sleep(1)

            Existing_isp = Select(driver.find_element(By.XPATH, "//select[@data-testid='existing_isp']"))
            Existing_isp.select_by_visible_text(row["existing_isp"])
            time.sleep(1)

            Unique_customer_ID = f"{int(time.time()) % 100}"
            Customer_ID = driver.find_element(By.XPATH, "(//input[@placeholder='Customer ID'])[1]")
            Customer_ID.send_keys(Unique_customer_ID)

            Profession = driver.find_element(By.XPATH, "(//input[@placeholder='Enter profession'])[1]")
            Profession.send_keys(row["profession"])
            time.sleep(1)

            Account_type = driver.find_element(By.XPATH, "//input[@placeholder='Enter account_type']")
            Account_type.send_keys(row["account_type"])

            Test_select = Select(driver.find_element(By.XPATH, "//select[@name='test_select']"))
            Test_select.select_by_visible_text(row["test_select"])
            time.sleep(1)

            # Lead_type = (driver.find_element(By.XPATH, "//div[@class='css-1xc3v61-indicatorContainer']//*[name()='svg']")).click()
            # time.sleep(2)
            # Lead_type_option = driver.find_element(By.XPATH, "//div[@class='css-1p3m7a8-multiValue']").click()
            # time.sleep(1)

            Remarks = driver.find_element(By.XPATH, "//textarea[contains(@placeholder,'Remarks')]")
            Remarks.send_keys(row["remarks"])

            # Address = driver.find_element(By.XPATH, "//input[@placeholder='Address']")
            # Address.send_keys(row["address"])
            Address = driver.find_element(By.XPATH, "//input[@placeholder='Search Maps']")
            Address.send_keys(row["address"])
            time.sleep(2)
            driver.find_element(By.XPATH,
                                "//li[@class='bg-white rounded py-1 font-medium px-2 cursor-pointer'][2]").click()
            time.sleep(5)


def lead_details(driver):
    wait = WebDriverWait(driver, 10)
    #driver.find_element(By.XPATH, "//a[normalize-space()='Vanna Nixon']").click()
    opportunity = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() ='Opportunity']")))
    opportunity.click()
    opportunity_convert = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() ='Convert']")))
    opportunity_convert.click()
    success = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Lead is converted to Opportunity.']")))
    if success:
        print("Lead is converted to opportunity")


    installation = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Installation']")))
    installation.click()
    time.sleep(2)
    installation_branch_selection = driver.find_element(By.CLASS_NAME, "css-1xc3v61-indicatorContainer")
    installation_branch_selection.click()
    driver.find_element(By.XPATH, "//div[text()='Central Branch']").click()
    time.sleep(2)
    create = driver.find_element(By.XPATH, "//button[text()='Create']")
    create.click()
    installatiton_success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
    if installatiton_success:
        print("Ticket assigned")


    stage = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Opportunity']")))
    assert stage.is_displayed(), "Stage is not updated to opportunity"

    status = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Installation']")))
    assert status.is_displayed(), "Status is not updated to installation"
    print("Successful")

    back_arrow = driver.find_element(By.XPATH, "//i[@class='ri-arrow-left-line mr-2']")
    back_arrow.click()
    assert "/crm/lead/?sort_order%5Bid%5D=desc&filter_q%5B%5D=" in driver.current_url, "User not directed to CRM page"
    time.sleep(2)


def crm_leads(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.relative.tableWrapper")))
    time.sleep(1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//table[contains(@class,'text-left text-sm overflow-auto')]")))
    user_list = driver.find_elements(By.XPATH, "(//tbody)[1]//tr//td[2]")
    all_usernames = [user.text.strip() for user in user_list]
    print("All Usernames: ", all_usernames)
    time.sleep(2)
    with open ("testdata/lead.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:

          expected_name = (row["first_name"] + " " + row["last_name"]).strip()
          assert expected_name in all_usernames, f"Username {expected_name} not found"
          print(f"New user {expected_name} is visible in CRM page")
    time.sleep(2)

def lead_details_page(driver):

    wait = WebDriverWait(driver, 10)

    new_user = driver.find_element(By.XPATH, "//a[normalize-space()='Annie Mayor']")
    new_user.click()
    assert "/crm/lead/25" in driver.current_url, "New user not opened"

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@class='text-lg font-semibold text-gray-500 mb-0']")))
    new_user_detail = driver.find_element(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-500 mb-0']")

    new_user_name = new_user_detail.text.strip()
    print("New user name: ", new_user_name)
    time.sleep(2)

    with (open ("testdata/lead.csv") as file):
        reader = csv.DictReader(file)
        for row in reader:
            expected_name = (row["first_name"] + " " + row["last_name"]).strip()
            assert expected_name in new_user_name, f"Username {expected_name} not found"
            print(f"New user {expected_name} detail page is opened")
            time.sleep(2)

            primary_number_displayed = driver.find_element(By.XPATH, "//a[@class=' flex items-center gap-1  text-primary hover:!text-gray-600']").text
            service_type_displayed = driver.find_element(By.CSS_SELECTOR, "p[class='uppercase ']").text
            name_displayed = driver.find_element(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-500 mb-0']").text
            #last_name_displayed = driver.find_element(By.CSS_SELECTOR, "h3.text-lg.font-semibold.text-gray-500.mb-0").text
            email_displayed = driver.find_element(By.CSS_SELECTOR, "a[class=' flex items-center gap-1 text-primary hover:!text-gray-600 lowercase']").text
            #preferred_username_displayed = driver.find_element(By.CSS_SELECTOR, "a[class='text-primary hover:text-primary-dark !text-sm block font-semibold lowercase']").text
            interested_product_option_displayed = driver.find_element(By.XPATH, "(//p[contains(@class,'')])[24]").text
            entry_source_displayed = driver.find_element(By.XPATH, "(//p[contains(@class,'')])[30]").text
            lead_source_displayed = driver.find_element(By.XPATH, "(//p[contains(@class,'')])[33]").text
            assigned_option_displayed = driver.find_element(By.XPATH, "(//p[contains(@class,'')])[21]").text
            existing_isp_displayed = driver.find_element(By.XPATH, "(//p[contains(@class,'infoLabelValue w-full capitalize')])[2]").text
            time.sleep(1)

            with (open("testdata/lead.csv") as file):
                reader = csv.DictReader(file)
                for row in reader:
                    #assert primary_number_displayed == (unique_number), "Primary number is wrong"
                    assert service_type_displayed == row.get("service_type"), "Service type is wrong"
                    assert name_displayed == row.get("first_name") + " " + row.get("last_name"), "Name is wrong"
                    #assert last_name_displayed == row.get("last_name"), "Last name is wrong"
                    #assert email_displayed == row.get("unique_email"), "Email is wrong"
                    #assert preferred_username_displayed == row.get("unique_username"), "Preferred username is wrong"
                    assert entry_source_displayed == row.get("entry_source"), "Entry source is wrong"
                    assert lead_source_displayed == row.get("lead_source"), "Lead source is wrong"
                    assert existing_isp_displayed == row.get("existing_isp"), "Existing ISP is wrong"
                    print("Details verified")

            time.sleep(2)
            back_arrow = driver.find_element(By.XPATH, "//a[@href='/crm/lead/?sort_order%5Bid%5D=desc&filter_q%5B%5D=']")
            back_arrow.click()
            time.sleep(5)

def leads_import(driver):
    wait = WebDriverWait(driver, 10)
    import_button = driver.find_element(By.XPATH, "//a[normalize-space()='Import']")
    import_button.click()

    upload_csv = driver.find_element(By.XPATH, "//input[@type='file']")
    upload_csv.click()


def my_leads(driver):
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

    wait = WebDriverWait(driver, 10)
    lead_stage = driver.find_elements(By.XPATH, "//tbody//tr//td[5]")
    row_texts = []
    for i in range(len(lead_stage)):
        row = lead_stage[i]
        row_texts.append(row.text.strip())

    select_stage = wait.until(EC.element_to_be_clickable((By.XPATH, "//body//div//div[contains(@data-testid,'child')]//div//div//div//div//div[1]//div[2]//select[1]")))

    select = Select(select_stage)
    time.sleep(2)

    stage_options = [option.text.strip() for option in select.options]
    print(stage_options)
    time.sleep(2)

    for stage_option_text in stage_options:
        select_stage = wait.until(EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/select[1]")))
        select = Select(select_stage)
        time.sleep(2)

        select.select_by_visible_text(stage_option_text)
        time.sleep(2)

        displayed_element = driver.find_elements(By.XPATH, "//tbody//tr//td[5]")
        time.sleep(2)
        displayed_texts = [elem.text.strip() for elem in displayed_element]
        print(displayed_texts)

        if stage_option_text == "Select Stage":
            assert displayed_texts == row_texts, f"Expected all, but got '{displayed_texts}'"
            print(f"Verified: {stage_option_text} is displayed correctly")
            time.sleep(2)

        else:
            assert all(text == stage_option_text for text in
                       displayed_texts), f"Expected all rows to be '{stage_option_text}', but got {displayed_texts}"
            print(f"Verified: {stage_option_text} is displayed correctly")
            time.sleep(2)


            lead_state = driver.find_elements(By.XPATH, "//tbody//tr//td[6]")
            state_texts = []
            for i in range(len(lead_state)):
                row = lead_state[i]
                state_texts.append(row.text.strip())
                print(state_texts)

            select_state = wait.until(EC.element_to_be_clickable((By.XPATH,
                "//select[@class='placeholder:text-gray-300  !border-gray-200  slimbox   !text-gray-600 font-normal '][contains(.,'Select State')]")))
            select = Select(select_state)
            time.sleep(2)

            state_options = [option.text.strip() for option in select.options]
            print(state_options)
            time.sleep(2)

            for state_option_text in state_options:
                select.select_by_visible_text(state_option_text)
                time.sleep(3)

                displayed_element_state = driver.find_elements(By.XPATH, "//tbody//tr//td[6]")

                displayed_texts_state = [elem.text.strip() for elem in displayed_element_state]
                print(displayed_texts_state)
                time.sleep(2)

                if state_option_text == "Select State":
                    assert displayed_texts_state == state_texts, f"Expected all, but got '{displayed_texts_state}'"
                    print(f"Verified: {state_option_text} is displayed correctly")
                    time.sleep(2)

                else:
                    assert all(text == state_option_text for text in
                               displayed_texts_state), f"Expected all rows to be '{state_option_text}', but got {displayed_texts_state}"
                    print(f"Verified: {state_option_text} is displayed correctly")
                    time.sleep(2)

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
        # select_sales_process = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[3]//div[2]//select[1]")))
        # select = Select(select_sales_process)
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
            assert all(text == options_sales_process_text for text in
                       displayed_texts), f"Expected all rows to be '{options_sales_process_text}', but got {displayed_texts}"
            print(f"Verified: {options_sales_process_text} is displayed correctly")

        driver.find_element(By.XPATH, "//button[normalize-space()='Clear']").click()


def entry_source(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-filter']//*[name()='svg']")))

    driver.find_element(By.XPATH, "//button[@class='btn-filter']//*[name()='svg']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//span[contains(@class,'box')])[14]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()

    # wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//tbody//tr//td[14]")))
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
            assert all(text == options_entry_source_text for text in
                       displayed_texts), f"Expected '{options_entry_source_text}', but got '{displayed_texts}'"
            print(f"Verified: {options_entry_source_text} is displayed correctly")
            time.sleep(3)

def search_leads(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-filter']//*[name()='svg']")))

    driver.find_element(By.XPATH, "//button[@class='btn-filter']//*[name()='svg']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//span[contains(@class,'box')])[1]").click()
    driver.find_element(By.XPATH, "(//span[contains(@class,'box')])[3]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[normalize-space()='Apply']").click()
    time.sleep(3)

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

        elif options_search_lead_text == "Name":
            input_box_name = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Name']")))

            test_value_name = "Rose"
            input_box_name.clear()
            time.sleep(2)
            print(test_value_name)
            input_box_name.send_keys(test_value_name)
            input_box_name.send_keys(Keys.ENTER)
            time.sleep(3)

            result = driver.find_element(By.XPATH, "//tbody//tr//td[2]").text
            assert test_value_name in result, "Search by Name failed"
            print("Search by Name working correctly")

        elif options_search_lead_text == "Lead ID":
            print("Successful")

        elif options_search_lead_text == "Phone Number":
            input_box_number = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Phone Number']")))

            test_value_number = "9873144486"
            input_box_number.clear()
            input_box_number.send_keys(test_value_number)
            input_box_number.send_keys(Keys.ENTER)

            result = driver.find_element(By.XPATH, "//tbody//tr//td[3]").text
            assert test_value_number in result, "Search by Number failed"
            print("Search by Number working correctly")
            time.sleep(2)







