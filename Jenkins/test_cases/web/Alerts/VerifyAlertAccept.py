"""
========================
VerifyAlertAccept.py
========================

:Module Desc: Verify the alert button by clicking accept.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import unittest
from selenium import webdriver
import time
import allure


@allure.parent_suite("Alerts")
class VerifyAlertAccess(unittest.TestCase):
    """
    :Class Description: Verify the alert button by clicking accept.

    """
    @allure.feature("Verify the alert button by clicking accept.")
    def test_alert_access(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get('https://testautomationpractice.blogspot.com/')
        driver.maximize_window()  # Maximize window size
        driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
        time.sleep(5)

        driver.switch_to.alert.accept()  # Closes alert window by clicking OK button


if __name__ == '__main__':
    unittest.main()
