from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def step_impl(context):
   context.driver= webdriver.Chrome()
   context.driver.implicitly_wait(30) 
   context.driver.maximize_window()


@when('I open orange HRM Homepage')
def step_impl(context):
   context.driver.get("https://opensource-demo.orangehrmlive.com/")
   


@when('Enter Username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
   context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
   context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)

@when('click on login button')
def step_impl(context):
      context.driver.find_element(By.XPATH, "//button[@type='submit']").click()



@then('User must successfully login to the Dashboard page')
def step_impl(context):
   try:
       text=context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
   except:
       context.driver.close()
       assert False, "Test Failed"
   if text=="Dashboard":
    context.driver.close()
    assert True,"Test Passed"

 