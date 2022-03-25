"""
========================
VerifyDoubleClick.py
========================

:Module Desc: Verify double click on button.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
from selenium import webdriver
from selenium.webdriver import ActionChains
import allure
import unittest


@allure.parent_suite("Clicks")
class VerifyDoubleClick(unittest.TestCase):
    """
    :Class Description: Verify double click on button.

    """
    @allure.feature("Verify double click on button.")
    def test_double_click(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get('https://testautomationpractice.blogspot.com/')
        driver.maximize_window()  # Maximize window size
        element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
        actions = ActionChains(driver)
        actions.double_click(element).perform()  # Double Click on button


if __name__ == '__main__':
    unittest.main()
