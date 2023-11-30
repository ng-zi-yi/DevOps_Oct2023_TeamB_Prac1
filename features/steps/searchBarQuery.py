from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@then(u'Select navigation bar search button')
def navSearch(context):
    context.driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul/li[8]/button/em").click()

@then(u'Input search "{query}"')
def inputQuery(context, query):
    context.driver.find_element(By.XPATH,"//*[@id='fsearch']").send_keys(query)

@then(u'Select form search button')
def clickSearch(context):
    context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/button/em").click()
    sleep(2)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then(u'Select query search result')
def clickCourseFees(context):
    context.driver.find_element(By.XPATH,"//*[@id='sitesearch-result']/div[2]/a[1]/p[2]").click()
    sleep(5)

@then(u'Select sort by most recent')
def sortByRecent(context):
    context.driver.find_element(By.XPATH,"//*[@id='filterRadioDefault2']").click()

@then(u'Filter "{filterSelection}"')
def sortByRecent(context,filterSelection):
    context.driver.find_element(By.XPATH,filterSelection).click()

