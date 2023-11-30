from behave import *
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#NP School Contact Details

@then(u'Hover over Schools and Courses')
def hoverSchoolsandCourses(context):
    # Find the navigation pane element and hover over it
    pane_navigation = context.driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[2]')
    actions = webdriver.ActionChains(context.driver)
    actions.move_to_element(pane_navigation).perform()

    # Check if the navigation pane options are visible
    nav_pane_options = context.driver.find_elements(By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[2]/div/div/div')
    assert len(nav_pane_options) > 0

@then(u'Go to "{schoolPath}" page')
def clickSchoolPath(context,schoolPath):
    try:
        school_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, schoolPath))
        )

        # Click on the School button (using JS)
        context.driver.execute_script("arguments[0].click();", school_button)
        sleep(5)
        
    except Exception as e:
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot.png")

@then(u'Go to Contact Details')
def toContactDetails(context):
    #Find Contact in School Page - Navigation Pane
    schoolpage_navigation = context.driver.find_element(By.XPATH,"/html/body/main/section[2]/div/div[2]/div[1]/div[1]")
    contact_btn = schoolpage_navigation.find_element(By.XPATH,f'//a[@href="#contact"]')
    
    #Click Contact Button
    context.driver.execute_script("arguments[0].click();", contact_btn)
    sleep(2)

