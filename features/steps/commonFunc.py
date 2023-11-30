from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Chrome browser is Launched')
def laucnhChromeBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)

@when(u'Open NP Website')
def openNPPage(context):
    context.driver.get('https://www.np.edu.sg/home')

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()
