from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@given(u'Chrome browser is Launched')
def laucnhChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open NP Website')
def openNPPage(context):
    context.driver.get('https://www.np.edu.sg/home')

@then(u'Select navigation bar search button')
def navSearch(context):
    context.driver.find_element(By.XPATH,"//*[@id='navbarNavDropdown']/ul/li[8]/button/em").click()

@then(u'Input search query "fees"')
def inputQuery(context):
    context.driver.find_element(By.XPATH,"//*[@id='fsearch']").send_keys("fees")

@then(u'Select form search button')
def clickSearch(context):
    context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/button/em").click()
    sleep(5)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'Select course fees search result')
def clickCourseFees(context):
    context.driver.find_element(By.XPATH,"//*[@id='sitesearch-result']/div[2]/a[1]").click()
    sleep(5)


@then(u'Verify if able to Search')
def verifySearch(context):
    context.driver.find_element(By.XPATH,"/html/body/main/section/div/div[2]/div[2]/div")
    sleep(2)
    

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()


