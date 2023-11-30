from behave import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@then(u'Select About NP')
def aboutNP(context):
    try:
        abtNP_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[1]"))
        )
        abtNP_button.click()

    except Exception as e:  
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot.png")

@then(u'Select Directions')
def clickDirections(context):
    context.driver.find_element(By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[1]/div/div/div/div[2]/div/div[7]/ul/li[2]/a").click()


@then(u'Select View Virtual Tour')
def virtualTour(context):
    try:
        virtualTour_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/section[2]/div/p[5]/a"))
        )

        context.driver.execute_script("arguments[0].click();", virtualTour_button)
        sleep(2)
        context.driver.switch_to.window(context.driver.window_handles[1])

    except Exception as e:
        print(f"Exception: {e}")
        context.driver.save_screenshot("error_screenshot.png")

@then(u'Select Explore')
def startExplore(context):
    #start virtual tour
    context.driver.find_element(By.XPATH, "//*[@id='krpanoSWFObject']/div[1]/div[2]/div[3]").click()
    sleep(2)
    #click explore button
    context.driver.find_element(By.XPATH, "//*[@id='krpanoSWFObject']/div[1]/div[2]/div[5]/div[1]").click()
    sleep(2)

@then(u'Select Start Here')
def selectStartHere(context):
    context.driver.find_element(By.XPATH, "//*[@id='krpanoSWFObject']/div[1]/div[2]").click()
    sleep(2)

@then(u'Select School of ICT')
def selectStartHere(context):
    context.driver.find_element(By.XPATH, "//*[@id='krpanoSWFObject']/div[1]/div[2]").click()
    sleep(2)
