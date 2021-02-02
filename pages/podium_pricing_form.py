"""
Object page for getting a price quote page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PodiumPricingPage:
    # URL
    # URL = 'https://podium.com'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # def load(self):
    #     self.browser.get(self.URL)

    def get_pricing_form_inputs(self):
      product_items = self.browser.find_elements_by_css_selector(
            '.cform > input')
      return product_items
  