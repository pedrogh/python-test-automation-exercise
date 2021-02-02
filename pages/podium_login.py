"""
Object page for the Podium Login page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PodiumLoginPage:

    # URL
    # URL = 'https://podium.com'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # def load(self):
    #     self.browser.get(self.URL)

    def get_email_field(self):
      email_field = self.browser.find_element_by_id(
            'emailOrPhoneInput')
      return email_field

    def get_password_field(self):
      email_field = self.browser.find_element_by_id(
            'passwordInput')
      return email_field

    def get_signin_button(self):
      signin_button = self.browser.find_element_by_id(
            'signInButton')
      return signin_button
    
    def click_on_signin_button(self):
      signin_button = self.get_signin_button()
      signin_button.click()
