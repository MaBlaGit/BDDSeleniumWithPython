from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from helpers.helpers import find_element_by

class AccountPage:

    def __init__(self, context):
        self.wait = WebDriverWait(context.driver, 10)
        self.logged_user_name = '.account > span'

    def get_logged_user_name(self):
        logged_user = find_element_by(self.wait, 'CSS_SELECTOR', self.logged_user_name)
        return logged_user.text