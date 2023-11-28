from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Chrome browser is Launched')
def laucnhChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open NP Website')
def openNPPage(context):
    context.driver.get('https://www.np.edu.sg/home')

# Test Case: Search for Badminton CCA Details 
@then(u'Select Student Life Tab')
def studentLife(context):
    try:
        student_life_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[4]"))
        )

        # Click on the "Student Life" button
        student_life_button.click()

    except Exception as e:  
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot_studentLife.png")
        
@then(u'Select Clubs and Society')
def selectCCA(context):
    try:
        club_or_society_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div/div[3]/div[2]/a"))
        )

        # Click on the club or society button (using JS)
        context.driver.execute_script("arguments[0].click();", club_or_society_button)
        sleep(5)
    except Exception as e:
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot_clubsSociety.png")

@then(u'Select "{ccaTypePath}"')
def selectMultipleCcaType(context, ccaTypePath):
    try:
        cca_type_button = WebDriverWait(context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, ccaTypePath))
            )
        
        context.driver.execute_script("arguments[0].click();", cca_type_button)
        sleep(5)
        
    except Exception as e:  
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot_ccaType.png")
    
@then(u'Select a "{ccaNamePath}"')
def selectMultipleCcaCard(context, ccaNamePath):
    try:
        cca_name_button = WebDriverWait(context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, ccaNamePath))
            )
        
        context.driver.execute_script("arguments[0].click();", cca_name_button)
        sleep(5)
    
    except Exception as e:  
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot_ccaCard.png")
    
@then(u'Verify if selected "{ccaName}" text is same as "{ccaTitlePath}"')
def verifySelection(context, ccaTitlePath, ccaName):
    title = WebDriverWait(context.driver, 60).until(
        EC.presence_of_element_located((By.XPATH, ccaTitlePath))
    )
    assert title.text == ccaName 

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()