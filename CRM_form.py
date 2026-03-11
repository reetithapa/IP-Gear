import csv
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def crm_displayed(driver):
    wait = WebDriverWait(driver, 10)

    CRM = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='CRM']")))
    CRM.click()
    time.sleep(2)

    assert "https://app-ispaas.dev.geniussystems.com.np/crm/" in driver.current_url

    print("CRM page is visible")
    time.sleep(2)

def crm_form(driver):
    wait = WebDriverWait(driver, 10)

    New_Lead = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button']")))
    New_Lead.click()
    assert "/crm/lead/add" in driver.current_url
    time.sleep(1)

    with open ("testdata/lead.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:

         service_type = row["service_type"]
         first_name = row["first_name"]
         last_name = row["last_name"]
         preferred_username = row["preferred_username"]
         interested_product_group = row["interested_product_group"]
         interested_product = row["interested_product"]
         entry_source = row["entry_source"]
         lead_source = row["lead_source"]
         assign_to_me = row["assign_to_me"]
         lead_Status = row["lead_status"]
         existing_isp = row["existing_isp"]
         address = row["address"]

         unique_primary_number = f"98{int(time.time()) % 100000000}"
         unique_number = print(unique_primary_number)
         Primary_mobile = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Primary Mobile']")))
         Primary_mobile.send_keys(unique_primary_number)
         time.sleep(1)

         Service_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='service_type']"))
         Service_type.select_by_visible_text(row["service_type"])
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

         unique_username = f"user{int(time.time())}"
         Preferred_username = driver.find_element(By.XPATH, "//input[@placeholder='Preferred Username']")
         Preferred_username.send_keys(unique_username)
         time.sleep(1)

         Interested_product_group = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m")))
         Interested_product_group.click()
         Interested_product_option = driver.find_element(By.XPATH, "//div[text()='business-50 mbs']")
         Interested_product_option.click()
         # interested_product_group = driver.find_element(By.XPATH, "//div[text()='50 mbps packages']")
         # interested_product_group.select_by_visible_text("50 mbps packages")
         time.sleep(2)

         Interested_product_option = driver.find_element(By.ID, "react-select-5-input")
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

         Assigned = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
         Assigned.click()
         Assigned_option = driver.find_element(By.XPATH, "//div[text()=' (ias@geniussystems.com.np) ']")
         Assigned_option.click()
         time.sleep(1)

         #assigned = Select(driver.find_element(By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m"))
         #assigned.select_by_visible_text(row["Assign_to_me"])
         #time.sleep(1)

         Lead_status = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_status']"))
         Lead_status.select_by_visible_text(row["lead_status"])
         time.sleep(1)

         Existing_isp = Select(driver.find_element(By.XPATH, "//select[@data-testid='existing_isp']"))
         Existing_isp.select_by_visible_text(row["existing_isp"])
         time.sleep(1)

         Address = driver.find_element(By.XPATH, "//input[@placeholder='Address']")
         Address.send_keys(row["address"])
         time.sleep(1)

         #Proceed = driver.find_element(By.XPATH, "//button[text()='Proceed']")
         #Proceed.click()
         time.sleep(1)

         Success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
         if Success:
             print("New lead has been successfully created")

        return unique_number, service_type, first_name, last_name, unique_email, unique_username, entry_source, lead_source, assign_to_me, existing_isp, address


def lead_details(driver):
    wait = WebDriverWait(driver, 10)
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

    new_user = driver.find_element(By.XPATH, "//a[normalize-space()='Rose Mary']")
    new_user.click()
    assert "/crm/lead/25" in driver.current_url, "New user not opened"

    wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@class='text-lg font-semibold text-gray-500 mb-0']")))
    new_user_detail = driver.find_element(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-500 mb-0']")
    if new_user_detail:
      print("New user detail")

    new_user_name = new_user_detail.text.strip()
    print("New user name: ", new_user_name)
    time.sleep(2)

    with (open ("testdata/lead.csv") as file):
        reader = csv.DictReader(file)
        for row in reader:
            expected_name = (row["first_name"] + " " + row["last_name"]).strip()
            print("expected_username is:", expected_name)
            assert expected_name in new_user_name, f"Username {expected_name} not found"
            print(f"New user {expected_name} detail page is opened")
            time.sleep(2)

            primary_number_displayed = driver.find_element(By.XPATH, "//a[@class=' flex items-center gap-1  text-primary hover:!text-gray-600']").text
            service_type_displayed = driver.find_element(By.CSS_SELECTOR, "p[class='uppercase ']").text
            name_displayed = driver.find_element(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-500 mb-0']").text
            #last_name_displayed = driver.find_element(By.CSS_SELECTOR, "h3.text-lg.font-semibold.text-gray-500.mb-0").text
            email_displayed = driver.find_element(By.CSS_SELECTOR, "a[class=' flex items-center gap-1 text-primary hover:!text-gray-600 lowercase']").text
            preferred_username_displayed = driver.find_element(By.XPATH, "//span[contains(@class,'!text-sm text-gray-400 block font-semibold lowercase')]").text
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
                    assert name_displayed == row.get(["first_name"] + " " + ["last_name"]), "First name is wrong"
                    #assert last_name_displayed == row.get("last_name"), "Last name is wrong"
                    #assert email_displayed == row.get("unique_email"), "Email is wrong"
                    #assert preferred_username_displayed == row.get("unique_username"), "Preferred username is wrong"
                    assert entry_source_displayed == row.get("entry_source"), "Entry source is wrong"
                    assert lead_source_displayed == row.get("lead_source"), "Lead source is wrong"
                    assert existing_isp_displayed == row.get("existing_isp"), "Existing ISP is wrong"
                    print("Details verified")

            back_arrow = driver.find_element(By.CSS_SELECTOR, "i.ri-arrow-left-line.mr-2")
            time.sleep(1)











