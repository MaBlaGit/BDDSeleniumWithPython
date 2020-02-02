import os
from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome(os.environ['CHROMEDRIVER'])
    context.driver.set_page_load_timeout(10)
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()
