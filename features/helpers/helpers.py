from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def find_element_by(wait, by, element):
    if by == 'ID':
        element = wait.until(lambda s: s.find_element(By.ID, element))
    elif by == 'CSS_SELECTOR':
        element = wait.until(lambda s: s.find_element(By.CSS_SELECTOR, element))
    elif by == 'CLASS_NAME':
        element = wait.until(lambda s: s.find_element(By.CLASS_NAME, element))
    return element

def clear_input(wait, by, element):
    input_to_clear = find_element_by(wait, by, element)
    input_to_clear.clear()