from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    context.driver= webdriver.Chrome()
    context.driver.implicitly_wait(30) 
    context.driver.maximize_window()

@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    
@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-branding']").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()

# @then('verify logo present on the homepage')
# def verifyLogo(context):
#     #status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
#     #status=context.find_element(By.XPATH,"//img[@alt='OrangeHRM']")
#     status=context.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']").is_displayed()
#     assert status is True
# Tests being passed




