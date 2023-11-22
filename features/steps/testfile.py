from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
        context.driver.save_screenshot("error_screenshot.png")
        
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
        context.driver.save_screenshot("error_screenshot.png")
        
@then(u'Select Sports')
def selectSportsCCA(context):
    try:   
        sports_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[2]/div/div/a/div"))
        )

        # Click on the "Student Life" button (Using JS)
        context.driver.execute_script("arguments[0].click();", sports_button)

    except Exception as e:  
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot.png")
        
@then(u'Select Badminton')
def selectBadmintonCCA(context):
    try:   
        badminton_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/section[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]"))
        )

        # Click on the "Student Life" button (using JS)
        context.driver.execute_script("arguments[0].click();", badminton_button)
        sleep(5)

    except Exception as e:  
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot.png")
        
@then(u'Verify if selected Badminton')
def verifySelection(context):
    title = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="member-profile-2327021f-6ac0-4834-ace3-b5b69f77987bLabel"]'))
    )
    assert title.text == "Badminton"

            
# @then(u'Filter to Infocomm Techonology')
# def filterCourse(context):
#     select = Select(context.driver.findElement(By.XPATH("//*[@id='jobIndustry']")))
#     select.select_by_value('Infocomm Technology')

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()