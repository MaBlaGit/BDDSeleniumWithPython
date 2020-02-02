from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:

    def __init__(self, context):
        self.wait = WebDriverWait(context.driver, 10)
        self.sign_in_button = 'login'
        self.email_input_field = 'email_create'


    def click_on_sign_in_button(self):
        sign_in = self.wait.until(lambda s: s.find_element(By.CLASS_NAME, self.sign_in_button))
        sign_in.click()
