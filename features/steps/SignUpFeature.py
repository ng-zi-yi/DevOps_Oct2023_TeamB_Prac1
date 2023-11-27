from behave import *
from selenium import webdriver
from time import sleep

@given(u'Chrome browser is launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open NP homepage')
def openNPHomePage(context):
    context.driver.get("https://www.np.edu.sg/home")


@then(u'Input Email "{email}"')
def step_impl(context, email):
    context.driver.find_element("id", "subscribeEmail").send_keys(email)
    element = context.driver.find_element("id", "button-signup")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    context.driver.execute_script("arguments[0].click();", element)
    sleep(5)

@then(u'Verify Successful Subcription')
def verifySuccessfulSubcription(context):
    title = context.driver.title
    assert title == "Subscription Successful"

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close() 