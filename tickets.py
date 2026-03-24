import csv
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def tickets_page(driver):
    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    tickets = driver.find_element(By.CSS_SELECTOR, "a[data-testid='Tickets']")
    tickets.click()
    time.sleep(3)
    assert "/tickets/support/all/" in driver.current_url, "Not redirected to ticket page"
    time.sleep(2)
    Installation = driver.find_element(By.XPATH, "//p[normalize-space()='Installation']")
    Installation.click()
    time.sleep(2)
    assert "/tickets/installation/all" in driver.current_url, "Installation not clicked"

    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class='text-sm font-semibold']")))

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                 "div[class='p-4 border-b hover:bg-gray-50 cursor-pointer bg-blue-50'] span[class='font-medium text-sm']")))
    ticket_id = driver.find_element(By.CSS_SELECTOR,
                                    "div[class='p-4 border-b hover:bg-gray-50 cursor-pointer bg-blue-50'] span[class='font-medium text-sm']")
    assert ticket_id.is_displayed(), "Ticket id not displayed"
    print("Ticket id is displayed")
    ticket_id.click()

    search_tickets = driver.find_element(By.XPATH, "//input[@placeholder='Search ticket']")
    search_tickets.send_keys("IN-4471")
    search_tickets_list = driver.find_elements(By.CSS_SELECTOR, ".h-auto")

    for i in range(len(search_tickets_list)):
        row = search_tickets_list[i]
        row_text = row.text
        print(row_text)

    assert "IN-4471" in row_text, "Not found"

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class='text-sm font-semibold']")))
    ticket_name = driver.find_element(By.CSS_SELECTOR, "h1[class='text-sm font-semibold']")
    assert "Margaret Gentry" in ticket_name.text, "Not matched"
    print("Name is visible")



