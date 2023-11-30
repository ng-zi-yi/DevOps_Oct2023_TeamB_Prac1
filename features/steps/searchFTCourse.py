from behave import *
from selenium import webdriver
import logging
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@then(u'Navigate to Full-Time Courses')
def navToFTPage(context):
    context.driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div/div/div[1]/ul/li[2]/a").click()
    
@then(u'FTCourse: Verify correct location and title')
def verifyLocation(context):
    supposed_url = "https://www.np.edu.sg/schools-courses/full-time-courses"
    current_url = context.driver.current_url
    supposed_title = "Full-Time Courses"
    current_title = context.driver.title
    assert supposed_url==current_url and supposed_title==current_title
    
@then(u'Input "{course}"')
def inputCourse(context, course):
    context.driver.find_element(By.ID,"courseListingSearch").send_keys(course)
    
@then(u'Verify if able to Search parameter: "{courseName}","{nameElement}"')
def verifySearch(context, courseName, nameElement):
    try:
        title = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, nameElement))
        )
    except:
        context.driver.save_screenshot("error_screenshot_Verify.png")
    assert title.text == courseName
    
@then(u'Select Search button')
def clickSearch(context):
    context.driver.find_element(By.ID,"btn-search").click()

def clickReset(context):
    context.driver.find_element(By.ID,"btn-reset").click()
    
@then(u'Click Dropdown List')
def dropdownList(context):
    select = Select(context.driver.find_element(By.ID,"courseListingSchool"))
    options = select.options
    for index in range(1, len(options) - 1):
        select.select_by_index(index)
        selected_option_text = select.all_selected_options
        clickSearch(context)
        sleep(3)
        courseClass = WebDriverWait(context.driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"course-school-name"))
        ).text
        print(courseClass, "\n")
        print(selected_option_text[0].text,'\n')
        clickReset(context)
        assert selected_option_text[0].text in courseClass
    
@then(u'Select School dropdown')
def selectSchoolFilter(context):
    context.driver.find_element(By.XPATH,"/html/body/main/section/div/div[2]/div[1]/div/div[2]/select").click()