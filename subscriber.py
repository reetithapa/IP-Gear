from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def create_subscriber(driver):
    wait = WebDriverWait(driver, 10)
    subscriber = driver.find_element(By.XPATH, "//a[normalize-space()='Subscribers']")
    subscriber.click()

    create_subscriber = driver.find_element(By.XPATH, "//button[contains(@data-testid,'button')]")
    create_subscriber.click()
    time.sleep(1)

    connection_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='connection-type']"))
    connection_type.select_by_visible_text("FTTH")
    time.sleep(1)

    FTTH_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='ftth-type']"))
    FTTH_type.select_by_visible_text("Wlink FTTH")
    time.sleep(1)


    interested_product_group = driver.find_element(By.XPATH, "//div[@class='react-select__input-container css-19bb58m']")
    interested_product_group.click()
    time.sleep(1)
    interested_product_option = driver.find_element(By.XPATH, "//div[text()='package group']")
    interested_product_option.click()
    time.sleep(1)

    package = driver.find_element(By.XPATH, "//div[contains(@class,'react-select__value-container css-hlgwow')]")
    package.click()
    time.sleep(1)
    package_option = driver.find_element(By.XPATH, "//div[text()='fup 50 mbps 1 mnth  (Price:1806.363/Renew:421.408)']")
    package_option.click()
    time.sleep(1)

    continue_button = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
    continue_button.click()
    time.sleep(1)

    username = driver.find_element(By.XPATH, "//input[@placeholder='Username (Use only lowercase letters, underscores (_), periods (.), and numbers)']")
    username.send_keys("Rose")
    time.sleep(1)

    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name.send_keys("Rose")
    time.sleep(1)

    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("Mary")
    time.sleep(1)

    mobile = driver.find_element(By.XPATH, "//input[@placeholder='Mobile']")
    mobile.send_keys("9800112233")
    time.sleep(1)

    email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    email.send_keys("rose@gmail.com")
    time.sleep(1)

    branch = driver.find_element(By.XPATH, "//div[@class='css-1xc3v61-indicatorContainer']//*[name()='svg']")
    branch.click()
    time.sleep(3)
    branch_option = driver.find_element(By.XPATH, "//div[text()='Bagdole Branch']")
    branch_option.click()
    time.sleep(4)


    account_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='account-type']"))
    account_type.select_by_visible_text("Personal")
    time.sleep(1)

    subscriber_category = Select(driver.find_element(By.XPATH, "//select[@data-testid='subscriber-category']"))
    subscriber_category.select_by_visible_text("PAYING")
    time.sleep(1)

    supplier = Select(driver.find_element(By.XPATH, "//select[@data-testid='supplier']"))
    supplier.select_by_visible_text("Test Supplier")
    time.sleep(1)

    supplier_customer_id = driver.find_element(By.XPATH, "//input[@placeholder='Supplier Customer ID']")
    supplier_customer_id.send_keys("123")
    time.sleep(1)

    partner = Select(driver.find_element(By.XPATH, "//select[@data-testid='partner']"))
    partner.select_by_visible_text("Partner_1")
    time.sleep(1)

    customer_id = driver.find_element(By.XPATH, "//input[@placeholder='Customer ID']")
    customer_id.send_keys("10983")
    time.sleep(1)

    billing_id = driver.find_element(By.XPATH, "//input[@placeholder='Billing ID']")
    billing_id.send_keys("1212")
    time.sleep(1)

    nationality = driver.find_element(By.XPATH, "//input[@placeholder='Enter nationality']")
    nationality.send_keys("Nepali")
    time.sleep(1)

    account_type_test = driver.find_element(By.XPATH, "//input[@placeholder='Enter account type test']")
    account_type_test.send_keys("Test")
    time.sleep(1)

    address = driver.find_element(By.XPATH, "//input[@placeholder='Search Maps']")
    address.send_keys("Baneshwor")
    time.sleep(2)
    driver.find_element(By.XPATH, "//li[@class='bg-white rounded py-1 font-medium px-2 cursor-pointer'][1]").click()
    time.sleep(1)

    #continue_button = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
    #continue_button.click()

    ONU_device_serial = driver.find_element(By.XPATH, "//div[contains(@data-testid,'onu-device-serial')]//div[contains(@class,'react-select__input-container css-19bb58m')]")
    ONU_device_serial.click()
    ONU_device_serail_option = driver.find_element(By.XPATH, "//div[text()='K4V8Z7928LY9D667']")
    ONU_device_serail_option.click()

    additional_inventory_items = driver.find_element(By.XPATH, "//div[@data-testid='additional-inventory']//div[@class='react-select__input-container css-19bb58m']")
    additional_inventory_items.click()
    additional_inventory_items_options = driver.find_element(By.XPATH, "//div[text()='K4V8Z7928LY9D667']")
    additional_inventory_items_options.click()

    continue_button = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
    continue_button.click()


    band_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='band-type']"))
    band_type.select_by_visible_text("Single band")

    splitters = driver.find_element(By.XPATH, "//span[contains(@class,'shrink-0 grow-0')]")
    splitters.click()
    search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search.click()
    splitters_options = driver.find_element(By.XPATH, "//button[normalize-space()='splitter-22 (73)']")
    splitters_options.click()

    splitter_port = Select(driver.find_element(By.XPATH, "//select[@data-testid='splitter-port']"))
    splitter_port.select_by_visible_text("2")

    cable_lengths = driver.find_element(By.XPATH, "//input[@placeholder='Cable Length (metres)']")
    cable_lengths.send_keys("30")

    current_power_level = Select(driver.find_element(By.XPATH, "//select[@data-testid='power-label']"))
    current_power_level.select_by_visible_text("-25")

    bridge_mode_ports = driver.find_element(By.XPATH, "//input[@placeholder='Enter port numbers, e.g: 1,2,5']")
    bridge_mode_ports.send_keys("1")

    continue_ftth = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
    continue_ftth.click()

    success = driver.find_element(By.XPATH, "//div[@role='alert']")
    if success.is_displayed():
        print("FTTH successful")

    upload_document = driver.find_element(By.XPATH, "//input[@placeholder='Select Upload Document']")
    upload_document.click()

    citizen_format = driver.find_element(By.XPATH, "//label[@for=':r93:']//span[@class='box ']")
    citizen_format.click()

    upload_citizen_front = driver.find_element(By.XPATH, "//div[@class='border p-3 rounded-md cursor-pointer text-xs flex items-center justify-center']")
    upload_citizen_front.click()

    continue_ftth = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")
    continue_ftth.click()

    submit = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit.click()

def subscriber_dashboard(driver):
    wait = WebDriverWait(driver, 10)
    subscriber = driver.find_element(By.XPATH, "//a[normalize-space()='Subscribers']")
    subscriber.click()

    dashboard = driver.find_element(By.XPATH, "//a[contains(text(),'Subscriber Dashboard')]")
    dashboard.click()

    assert "/subscriber/list" in driver.current_url, "Not redirected to subscriber dashboard"

    username_dashboard = driver.find_element(By.XPATH, "//a[normalize-space()='qysyd_wfn']")
    print(username_dashboard.text)















