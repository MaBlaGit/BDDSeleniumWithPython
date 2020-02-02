from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from helpers.helpers import find_element_by, clear_input


class AuthenticationPage:

 
    def __init__(self, context):
        self.wait = WebDriverWait(context.driver, 10)
        self.email_input_field = 'email_create'
        self.create_an_account_button = 'SubmitCreate'
        self.title_mr_radio_button = 'id_gender1'
        self.title_mrs_radio_button = 'id_gender2'
        self.first_name_input_field = 'customer_firstname'
        self.last_name_input_field = 'customer_lastname'
        self.password_input_field = 'passwd'
        self.day_select_dropdown = 'days'
        self.month_select_dropdown = 'months'
        self.years_select_dropdown = 'years'
        self.address = 'address1'
        self.city = 'city'
        self.country_state = 'id_state'
        self.postal_code = 'postcode'
        self.phone_home_number = 'phone'
        self.mobile_phone_number = 'phone_mobile'
        self.address_alias = 'alias'
        self.register_button = 'submitAccount'


    def enter_user_email(self, email):
        email_input = find_element_by(self.wait, 'ID', self.email_input_field)
        email_input.send_keys(email)


    def click_on_create_an_account_button(self):
        create_an_account = find_element_by(self.wait, 'ID', self.create_an_account_button)
        create_an_account.click()

    def select_user_title(self, title):
        if title == 'Mr':
            mr = find_element_by(self.wait, 'ID', self.title_mr_radio_button)
            mr.click()
        elif title == 'Mrs':
            mrs = find_element_by(self.wait, 'ID', self.title_mrs_radio_button)
            mrs.click()
    

    def enter_first_name(self, first_name):
        first = find_element_by(self.wait, 'ID', self.first_name_input_field)
        first.send_keys(first_name)


    def enter_last_name(self, last_name):
        last = find_element_by(self.wait, 'ID', self.last_name_input_field)
        last.send_keys(last_name)


    def enter_user_password(self, password):
        passwd = find_element_by(self.wait, 'ID', self.password_input_field)
        passwd.send_keys(password)

    def select_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth.split('-')
        self.select_day(day)
        self.select_month(month)
        self.select_year(year)

    def select_day(self, day):
        select_day = Select(find_element_by(self.wait, 'ID', self.day_select_dropdown))
        select_day.select_by_value(day)


    def select_month(self, month):
        select_month = Select(find_element_by(self.wait, 'ID', self.month_select_dropdown))
        select_month.select_by_value(month)

    def select_year(self, year):
        select_year = Select(find_element_by(self.wait, 'ID', self.years_select_dropdown))
        select_year.select_by_value(year)

    def enter_user_address(self, address):
        user_address = find_element_by(self.wait, 'ID', self.address)
        user_address.send_keys(address)

    def enter_user_city(self, city):
        user_city = find_element_by(self.wait, 'ID', self.city)
        user_city.send_keys(city)

    def select_country_state(self, state):
        country_state = Select(find_element_by(self.wait, 'ID', self.country_state))
        country_state.select_by_visible_text(state)

    def enter_postal_code(self, code):
        postal_code = find_element_by(self.wait, 'ID', self.postal_code)
        postal_code.send_keys(code)

    def enter_phone_home_number(self, phone_number):
        home_phone = find_element_by(self.wait, 'ID', self.phone_home_number)
        home_phone.send_keys(phone_number)

    def enter_mobile_home_number(self, mobile_phone):
        mobile = find_element_by(self.wait, 'ID', self.mobile_phone_number)
        mobile.send_keys(mobile_phone)

    def enter_address_alias(self, address_alias):
        address = find_element_by(self.wait, 'ID', self.address_alias)
        clear_input(self.wait, 'ID', self.address_alias)
        address.send_keys(address_alias)

    def click_on_register_button(self):
        register = find_element_by(self.wait, 'ID', self.register_button)
        register.click()