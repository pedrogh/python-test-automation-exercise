"""
Object page for the Podium Main page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PodiumMainPage:

    # URL
    URL = 'https://podium.com'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_text_elements(self):
        text_columns = self.browser.find_elements_by_css_selector(
            '.large-10.columns')
        return text_columns

    def get_logo_image(self):
        logo = self.browser.find_element_by_class_name(
            'logo')
        return logo

    def get_prompt(self):
      iframe = self.browser.find_element_by_id('podium-prompt')
      self.browser.switch_to.frame(iframe)
      prompt = self.browser.find_element_by_class_name('Prompt')
      # Not needed maybe since each test reloads the page?
      # driver.switch_to.default_content()
      return prompt

    def get_pricing_menu_item(self):
      pricing_link = self.browser.find_element_by_link_text(
            'Pricing')
      return pricing_link

    def get_login_menu_item(self):
      pricing_link = self.browser.find_element_by_link_text(
            'Login')
      return pricing_link

    def get_product_menu_items(self):
      product_items = self.browser.find_elements_by_css_selector(
            'div.menu-left > ul > li')
      return product_items

    def click_on_login(self):
      self.get_login_menu_item().click()

    def get_pricing_form_inputs(self):
      product_items = self.browser.find_elements_by_css_selector(
            '.cform > input')
      return product_items
  