"""
========================
VerifyAlertDismiss.py
========================

:Module Desc: Verify the alert button by clicking cancel.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import unittest
from selenium import webdriver
import time
import allure


@allure.parent_suite("Alerts")
class VerifyAlertDismiss(unittest.TestCase):
    """
    :Class Description: Verify the alert button by clicking cancel.

    """
    @allure.feature("Verify the alert button by clicking cancel.")
    def test_alert_dismiss(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get('https://testautomationpractice.blogspot.com/')
        driver.maximize_window()  # Maximize window size
        driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
        time.sleep(5)

        driver.switch_to.alert.dismiss()    # Closes alert window by clicking Cancel button


if __name__ == '__main__':
    unittest.main()
