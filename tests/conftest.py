"""
This module contains shared fixtures.
"""

import pytest
import requests
import os
import allure

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from pages.podium_main import PodiumMainPage
from pages.podium_login import PodiumLoginPage
from pages.podium_pricing_form import PodiumPricingPage

# ----------------------------------------------------------------------
# Fixture: Create the WebDriver instance and other pages as 
#          fixtures used in the tests.
# ----------------------------------------------------------------------

@pytest.fixture()
def browser():
  ''' Creates a Chrome driver, yields, terminates the driver '''
  # --- Scenario 1
  # --- Uncomment the line below to see tests running outside of Docker
  # --- Comment out the code for scenarios 2 and 3 below. 
  driver = Chrome()
  # --- end of Scenario 1

  # --- Scenario 2
  # --- Uncomment the lines below to see tests running outside of Docker
  # --- Comment out the code for scenarios 1 above and 3 below. 

  # chrome_options = Options()
  # chrome_options.add_argument('--no-sandbox')
  # chrome_options.add_argument('--disable-dev-shm-usage')
  # driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=chrome_options)
  # #driver.set_window_size(1920, 1080)
  # --- end of Scenario 2

  # --- Scenario 3
  # --- comment from below to see tests running within Docker

  # chrome_options = Options()
  # chrome_options.add_argument('--headless')
  # chrome_options.add_argument('--no-sandbox')
  # chrome_options.add_argument('--disable-dev-shm-usage')
  # driver = Chrome(chrome_options=chrome_options)
  # driver.set_window_size(1920, 1080)
  # --- comment from above to see tests running in Docker
  # --- end of Scenario 3

  driver.implicitly_wait(5)
  yield driver
  driver.quit()

@pytest.fixture
def podiumHomePage(browser):
  ''' Creates a PodiumMainPage, loads it, and returns it to the test. '''
  podium_home_page = PodiumMainPage(browser)
  # Load the main page.
  podium_home_page.load()
  return podium_home_page

@pytest.fixture
def podiumLoginPage(browser):
  ''' Creates a PodiumLoginPage and returns it to the test. '''
  podium_login_page = PodiumLoginPage(browser)
  return podium_login_page

@pytest.fixture
def podiumPricingPage(browser):
  ''' Creates a PodiumPricingPage and returns it to the test. '''
  podium_pricing_page = PodiumPricingPage(browser)
  return podium_pricing_page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
