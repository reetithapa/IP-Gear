from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def add_product(driver):
    inventory = driver.find_element(By.XPATH, "//a[contains(text(),'Inventory')]")
    inventory.click()

    assert "/inventory/product/list" in driver.current_url, "Not redirected to inventory page"

    add_product = driver.find_element(By.XPATH, "//a[normalize-space()='Add Product']")
    add_product.click()
    time.sleep(1)

    assert "/inventory/product/add" in driver.current_url, "Not redirected to add product page"

    product_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter the product name']")
    product_name.send_keys("Router")
    time.sleep(1)

    product_code = driver.find_element(By.XPATH, "//input[@placeholder='Enter the product code']")
    product_code.send_keys("1234")
    time.sleep(1)

    warranty = driver.find_element(By.XPATH, "//input[@placeholder='Enter the period']")
    warranty.send_keys("4")
    time.sleep(1)

    warranty_select = Select(driver.find_element(By.XPATH, "//select[@name='warranty_period_type']"))
    warranty_select.select_by_value("month")
    time.sleep(1)

    purchase_price = driver.find_element(By.XPATH, "//input[@data-testid='purchase_price']")
    purchase_price.send_keys("400")
    time.sleep(1)

    sales_price = driver.find_element(By.XPATH, "//input[@data-testid='sales_price']")
    sales_price.send_keys("500")
    time.sleep(1)

    vendor = Select(driver.find_element(By.XPATH, "//select[@data-testid='vendors']"))
    vendor.select_by_visible_text("Huawei")
    time.sleep(1)

    vendor_model = Select(driver.find_element(By.XPATH, "//select[@data-testid='vendors_model']"))
    vendor_model.select_by_visible_text("Huawei V1.0")
    time.sleep(1)

    category = Select(driver.find_element(By.XPATH, "//select[@data-testid='categories']"))
    category.select_by_visible_text("ONU Router")
    time.sleep(1)

    product_custom_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter product custom field']")
    product_custom_field.send_keys("abcd")
    time.sleep(1)

    description = driver.find_element(By.XPATH, "//textarea[@placeholder='You can add the description here.']")
    description.send_keys("abcdjhgfds")
    time.sleep(1)

    #save = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    #save.click()





