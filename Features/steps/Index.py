from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from behave import *
from helpers import values

driver = webdriver.Chrome()
use_step_matcher("re")


@given("I am on the saloodo web page.")
def step_impl(context):
    """

    """
    driver.maximize_window()
    driver.get(values.url)



@when("I clicked on the Register button.")
def step_impl(context):
    """
    Due to poor internet, an implicit wait is
    introduced to allow the page to load before moving to the next step
    """
    driver.find_element_by_css_selector(values.regBtn).click()
    driver.implicitly_wait(5)


@step("I click on the Register Your Company Option.")
def step_impl(context):
    driver.find_element_by_link_text("Register Your Company").click()


@step("I filled my details in the form that is displayed.")
def step_impl(context):
    driver.find_element_by_css_selector(values.company_field).send_keys(values.company_name)
    driver.find_element_by_css_selector(values.email_field).send_keys(values.email)
    driver.find_element_by_css_selector(values.field_fname).send_keys(values.first_name)
    driver.find_element_by_css_selector(values.field_lname).send_keys(values.last_name)
    driver.find_element_by_css_selector(values.phone_field).send_keys(values.phone)
    driver.find_element_by_css_selector(values.newsletter).click()
    driver.find_element_by_css_selector(values.terms).click()


@step("I click create account button.")
def step_impl(context):
    driver.find_element_by_css_selector(values.crBtn).click()


@then("It should NOT be successful.")
def step_impl(context):
    form = driver.find_element_by_css_selector(values.formChk)

    try:
        assert "CREATE YOUR SALOODO! ACCOUNT" in form.text

    except Exception as e:
        print(f"Assertion failed , {e}")


@when("I click on the login button.")
def step_impl(context):
    driver.find_element_by_link_text(values.lgBtn).click()


@step("I insert my email and password.")
def step_impl(context):
    driver.find_element_by_name(values.username).send_keys(values.email)
    driver.find_element_by_name(values.pwd_field).send_keys(values.password)


@step("I click the login button.")
def step_impl(context):
    driver.find_element_by_css_selector(values.stBtn).click()


@then("I should be directed to the dashboard.")
def step_impl(context):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,values.popUp))).click()

    try:
        assert driver.current_url == values.new_url

    except Exception as e:
        print(f"Assertion failed , {e}")




@when("I click my profile name.")
def step_impl(context):
    driver.find_element_by_css_selector(values.prOpt).click()



@step("I click the general option.")
def step_impl(context):
    driver.find_element_by_link_text(values.prGnl).click()


@step("I click the edit option under company.")
def step_impl(context):
    driver.find_element_by_css_selector(values.editBtn).click()


@step("I fill in the valid details.")
def step_impl(context):
    driver.find_element_by_name(values.vatFld).send_keys(values.vatId)
    driver.find_element_by_name(values.strtFld).send_keys(values.strt)
    driver.find_element_by_name(values.strtNoFld).send_keys(values.strtNo)
    driver.find_element_by_name(values.strNoAdFld).send_keys(values.strNoAd)
    driver.find_element_by_name(values.postFld).send_keys(values.postCode)
    driver.find_element_by_name(values.cityFld).send_keys(values.city)
    driver.execute_script("window.scrollTo(0,450)")
    driver.find_element_by_css_selector(values.drp_down).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, values.cntent))).click()


@step("I click on update profile.")
def step_impl(context):
    driver.find_element_by_css_selector(values.stBtn).click()



@then("It should be successful.")
def step_impl(context):
    content = driver.find_element_by_css_selector(values.updated)

    try:
        assert "Automotive" in content.text

    except Exception as e:
        print(f"Assertion failed , {e}")