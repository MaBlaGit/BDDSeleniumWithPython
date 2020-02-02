from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.helpers import find_element_by


class MainPage:

    def __init__(self, context):
        self.wait = WebDriverWait(context.driver, 10)
        self.sign_in_button = 'login'
        self.email_input_field = 'email_create'

    def get_sign_in_button_name(self):
        sign_in = find_element_by(self.wait, 'CLASS_NAME', self.sign_in_button)
        return sign_in.text


    def click_on_sign_in_button(self):
        sign_in = find_element_by(self.wait, 'CLASS_NAME', self.sign_in_button)
        sign_in.click()
