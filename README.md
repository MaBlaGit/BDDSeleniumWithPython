# BDD Selenium with Python (WIP)

## Description 

This repo contains small implementation of e2e tests written in Python, Selenium and Gherkin syntax.
Tests were written for __http://automationpractice.com/__ 

## How to setup local environment and run tests (Linux / Mac users)

Project was written in Python 3.7.6 but any version of Python 3.x should be fine.

As a default browser Chrome was used so make sure that Chrome on your local machine is installed

__chromedriver__ is required to run Selenium tests in Chrome browser. Depending of the browser version, download appropriate driver from __https://chromedriver.chromium.org/downloads__

1 Clone repo

2 Got to the root folder of the project and create virtual environment - __python3 -m venv $(pwd)/venv__ (more info here: __https://docs.python.org/3.7/library/venv.html__)

3 Activate virtual environment - __source ./venv/bin/activate__

4 Install requred dependencies - __make deps__

5 Add chromedriver to environmental variables - __export CHROMEDRIVER=absolute/path/to/chromedriver__

6 Run tests by command - __behave__

