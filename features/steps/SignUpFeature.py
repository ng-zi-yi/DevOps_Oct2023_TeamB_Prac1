from behave import *
from selenium import webdriver
from time import sleep

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
