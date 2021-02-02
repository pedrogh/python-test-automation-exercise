"""
Tests for Podium's home page.
"""

import pytest
import logging
from selenium.common.exceptions import NoSuchElementException

# Used for debugging only.
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

IMAGES = {
    'pdmlogo_black.png': 'PDM_LOGO'
}

def is_podium_logo_image(image):
    podium_logo_is_present = False
    # Get the image file name.
    img_src = image.get_attribute('src').split('/')[-1]
    if IMAGES[img_src] == 'PDM_LOGO':
        podium_logo_is_present = True

    return podium_logo_is_present

def test_podium_logo_image_is_present(podiumHomePage):
    logo = podiumHomePage.get_logo_image()
    # Assert the Punisher image is absent
    assert is_podium_logo_image(logo)

def test_podium_prompt_is_visible(podiumHomePage):
  prompt = podiumHomePage.get_prompt()
  assert prompt.is_displayed()

# @pytest.mark.skip(reason="This is failing in Docker for some reason")
def test_menu_items_are_correct(podiumHomePage):
  PRODUCT_ITEMS = [
    'Products', 
    'Solutions',
    'Enterprise', 
    'Resources', 
    'Pricing']

  PRODUCT_ITEMS_LENGTH = len(PRODUCT_ITEMS)
  
  product_items = podiumHomePage.get_product_menu_items()
  mylogger.info('product_items: {}'.format(product_items))

  assert len(product_items) == PRODUCT_ITEMS_LENGTH

  # Maybe it would be better to do a check for each item to be
  # in the list returned in case the order changes.
  for t in range(len(product_items)):
    # assert product_items[t].text == PRODUCT_ITEMS[t]
    assert product_items[t].text in PRODUCT_ITEMS
