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



