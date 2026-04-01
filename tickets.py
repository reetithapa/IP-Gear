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

    tickets_dropdown = driver.find_element(By.XPATH, "//select[contains(@class,'w-full')]")
    tickets_dropdown.click()

    select = Select(tickets_dropdown)

    assign_to_me = driver.find_element(By.XPATH, "(//option[contains(@value,'assigned')])[1]")
    assign_to_me.click()
    time.sleep(3)

    searched_ticket = driver.find_element(By.XPATH, "//span[contains(@class,'font-medium text-sm')]").text

    assert "SU-4480" in searched_ticket
    print("SU-4480 found")
    time.sleep(2)

    all_tickets = driver.find_element(By.XPATH,"(//option[contains(@value,'all')])[1]")
    all_tickets.click()
    time.sleep(3)

    Installation = driver.find_element(By.XPATH, "(//p[normalize-space()='Installation'])[1]")
    Installation.click()
    time.sleep(3)
    assert "/tickets/installation/all" in driver.current_url, "Installation not clicked"
    print("Installation is clicked")

    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class='text-sm font-semibold']")))

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                 "div[class='p-4 border-b hover:bg-gray-50 cursor-pointer bg-blue-50'] span[class='font-medium text-sm']")))
    ticket_id = driver.find_element(By.CSS_SELECTOR,
                                    "div[class='p-4 border-b hover:bg-gray-50 cursor-pointer bg-blue-50'] span[class='font-medium text-sm']")
    assert ticket_id.is_displayed(), "Ticket id not displayed"
    print("Ticket id is displayed")
    ticket_id.click()
    time.sleep(2)

    search_tickets = driver.find_element(By.XPATH, "//input[@placeholder='Search ticket']")
    time.sleep(2)
    search_tickets.send_keys("IN-4471")
    time.sleep(2)
    tickets = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='IN-4471'])[1]")))
    search_tickets_list = driver.find_element(By.XPATH, "//span[@class='font-medium text-sm']")
    print(search_tickets_list.text)

    #for i in range(len(search_tickets_list)):
     #   print(len(search_tickets_list))
      #  row = search_tickets_list[i]
       # row_text = row.text

    #assert "4471" in search_tickets_list.text, "Ticket not found"


    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class='text-sm font-semibold']")))
    #ticket_name = driver.find_element(By.CSS_SELECTOR, "h1[class='text-sm font-semibold']")
    #assert "harry xyz" in ticket_name.text, "Not matched"
    #print("Name is visible")



