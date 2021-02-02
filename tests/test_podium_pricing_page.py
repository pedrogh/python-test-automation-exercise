"""
Tests for Podium's page to request a price quote.
"""

# TODO: Remove
import logging

# Used for debugging only.
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

def test_pricing_form_displays_and_has_correct_fields(podiumHomePage, podiumPricingPage):
  # See a different way of finding an element and clicking on it
  # in tests/test_podium_login_page.py
  podiumHomePage.get_pricing_menu_item().click()

  PRICING_FORM_ITEMS = [
    'First Name', 
    'Last Name', 
    'Company Name', 
    'Email Address', 
    'Mobile', 
    'Get a Quote']
  PRICING_FORM_ITEMS_LENGTH = len(PRICING_FORM_ITEMS)

  form_inputs = podiumPricingPage.get_pricing_form_inputs()
  
  assert len(form_inputs) == PRICING_FORM_ITEMS_LENGTH

  LAST_ELEMENT_POS = len(form_inputs)-1
  for t in range(LAST_ELEMENT_POS):
    assert form_inputs[t].get_attribute('placeholder') == PRICING_FORM_ITEMS[t]
  
  assert form_inputs[LAST_ELEMENT_POS].get_attribute('value') == PRICING_FORM_ITEMS[LAST_ELEMENT_POS]
