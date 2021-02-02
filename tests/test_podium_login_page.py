"""
Tests for Podium's Login page.
"""

import logging
import time

# Used for debugging only.
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

def test_login_form_fields_work(podiumHomePage, podiumLoginPage):
  # See a different way of finding an element and clicking on it
  # in tests/test_podium_pricing_page.py
  podiumHomePage.click_on_login()

  # TODO
  # assert not login_page.get_password_field().is_displayed()
  # assert not login_page.get_signin_button().is_displayed()

  email_field = podiumLoginPage.get_email_field()

  assert email_field.is_displayed()
  email_field.clear()
  email_field.send_keys('myemail@myemail.com')

  # Click on Sign In Button
  podiumLoginPage.click_on_signin_button()

  # Input field for password and button are now visible
  podiumLoginPage.get_password_field().is_displayed()
  podiumLoginPage.get_signin_button().is_displayed()
