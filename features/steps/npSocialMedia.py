from behave import *
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#NP Social Media Check
@given(u'Chrome Browser is launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()

    #Maximize Webpage to have follow standard screen size
    context.driver.maximize_window()

@when(u'Open NP page')
def openNPpage(context):
    context.driver.get("https://www.np.edu.sg/home")
    

## Differrent Social Media Link 
@then(u'Click "{socialicon}" link')
def clickSociallink(context,socialicon):
    #Finding social media icon
    socialLink = context.driver.find_element(By.XPATH, socialicon)
    
    #Click social media link
    context.driver.execute_script("arguments[0].click();",socialLink)

@then(u'Verify new tab is "{socialmediaPage}"')
def correctSocialMediaPage(context,socialmediaPage):

    #Wait for new tab to load and verify two tabs created
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in context.driver.window_handles:
        if window_handle != context.driver.current_window_handle:
            context.driver.switch_to.window(window_handle)
            break

    #Check if link is correct
    assert context.driver.current_url == socialmediaPage

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()