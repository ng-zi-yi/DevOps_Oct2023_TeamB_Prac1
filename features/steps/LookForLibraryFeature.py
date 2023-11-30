from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Chrome browser is launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open NP homepage')
def openNPHomePage(context):
    context.driver.get("https://www.np.edu.sg/home")


@then(u'Click on Library')
def clickOnLibrary(context):
    link = context.driver.find_element(By.LINK_TEXT, 'Library')
    context.driver.execute_script("arguments[0].scrollIntoView();", link)
    sleep(1)
    scroll_distance = 50
    context.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    link.click()
    sleep(2)

@then(u'Verify Library is accessed')
def verifyLibary(context):
    title = context.driver.title
    requiredWord = "Library"
    assert requiredWord.lower() in title.lower()

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close() 