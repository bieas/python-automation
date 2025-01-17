from selenium import webdriver
from behave import given, when, then
from locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

@given('user directs to url page "{url}"')
def direct_to_url(context, url):
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)

@then('{element} should be displayed')
def is_displayed(context, element):
    field_locator = globals().get(element)
    if driver.find_element(*field_locator):
        print("element exist")
    else:
        print("element not exist")


@when('user fill in {element} with "{text}"')
def user_fill(context, element, text):
    field_locator = globals().get(element)
    element = driver.find_element(*field_locator)
    element.send_keys(text)

@when('user click {element}')
def user_click(context, element):
    field_locator = globals().get(element)
    element = driver.find_element(*field_locator)
    element.click()

@when('user wait {time} seconds')
def user_wait(context, time):
    wait_time = int(time)
    driver.implicitly_wait(wait_time)

@when('user wait {time} seconds until "{text}" visible in {element}')
def user_wait_until(context, time, text, element):
    wait_time = int(time)
    field_locator = globals().get(element)
    waiting = WebDriverWait(driver, wait_time)
    waiting.until(EC.text_to_be_present_in_element(field_locator, text))

@then('verify should be contain "{text}"')
def is_regex_text_contain(context, text):
    driver.page_source.__contains__(text)

