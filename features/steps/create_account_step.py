from behave import given, when, then, step
from pages.MainPage import MainPage
from pages.AuthenticationPage import AuthenticationPage
from pages.AccountPage import AccountPage
from data.data import get_main_page_url, random_email_generator
from faker import Faker
from hamcrest import *
import time

@given('User is on the "automationpractice.com" website')
def navigate_to_selected_webpage(context):
    context.user = random_email_generator()
    context.faker = Faker('en_US')
    context.driver.get(get_main_page_url())
    context.main_page = MainPage(context)
    context.authentication_page = AuthenticationPage(context)
    context.account_page = AccountPage(context)


@when('User click on the "Sign In" button')
def click_on_the_sign_in_button(context):
    context.main_page.click_on_sign_in_button()


@step('User provide valid email')
def sign_in_provide_valid_email(context):
    context.authentication_page.enter_user_email(context.user)


@step('User click on the "Create Account" button')
def create_account_button_click(context):
    context.authentication_page.click_on_create_an_account_button()

@step('User select "{title}" radio button')
def select_person_title(context, title):
    context.authentication_page. select_user_title(title)

@step('User enter "{first_name}" as a first name')
def enter_first_name(context, first_name):
    context.f_name = first_name
    context.authentication_page.enter_first_name(first_name)

@step('User enter "{last_name}" as a last name')
def enter_last_name(context, last_name):
    context.l_name = last_name
    context.authentication_page.enter_last_name(last_name)

@step('User enter "{password}" as a password')
def enter_user_password(context, password):
    context.authentication_page.enter_user_password(password)

@step('User select "{date_of_birth}" as a date of birth')
def select_date_of_birth(context, date_of_birth):
    context.authentication_page.select_date_of_birth(date_of_birth)

@step('User select "{address}" as my address')
def user_address(context, address):
    context.authentication_page.enter_user_address(address)

@step('User select city as my city')
def user_random_city(context):
    context.authentication_page.enter_user_city(context.faker.city())

@step('User select state')
def user_random_state(context):
    context.authentication_page.select_country_state(context.faker.state())

@step('User enter postal code')
def user_random_postal_code(context):
    context.authentication_page.enter_postal_code(context.faker.zipcode())

@step('User enter "{phone_number}" as phone number')
def user_home_phone_number(context, phone_number):
    context.authentication_page.enter_phone_home_number(phone_number)

@step('User enter "{mobile_phone}" as mobile number')
def user_mobile_phone_number(context, mobile_phone):
    context.authentication_page.enter_mobile_home_number(mobile_phone)

@step('User enter address alias for future reference')
def enter_additional_email_address(context):
    context.authentication_page.enter_address_alias(context.user)

@step('User click on the "Register" button')
def register(context):
    context.authentication_page.click_on_register_button()

@then('User account will be created')
def assert_user_name(context):
    username_to_assert = context.account_page.get_logged_user_name()
    user_name_from_step = '{} {}'.format(context.f_name, context.l_name)
    assert_that(user_name_from_step, username_to_assert)
