from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.remote.webelement import WebElement

@given(u'Chrome browser is Launched')
def laucnhChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open NP Website')
def openNPPage(context):
    context.driver.get('https://www.np.edu.sg/home')

@then(u'Navigate to Full-Time Courses')
def navToFTPage(context):
    context.driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div/div/div[1]/ul/li[2]/a").click()
    
@then(u'Input Course Title')
def inputCourse(context):
    context.driver.find_element(By.XPATH,"//*[@id='courseListingSearch']").send_keys("Information Technology")

@then(u'Select Search button')
def clickSearch(context):
    context.driver.find_element(By.XPATH,"//*[@id='btn-search']").click()

@then(u'Verify if able to Search')
def verifySearch(context):
    context.driver.find_element(By.XPATH,"/html/body/main/section/div/div[2]/div[2]/div")
            
# @then(u'Filter to Infocomm Techonology')
# def filterCourse(context):
#     select = Select(context.driver.findElement(By.XPATH("//*[@id='jobIndustry']")))
#     select.select_by_value('Infocomm Technology')

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()