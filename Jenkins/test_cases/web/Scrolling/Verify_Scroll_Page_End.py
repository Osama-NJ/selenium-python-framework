"""
========================
VerifyScrollPageEnd.py
========================

:Module Desc: Verify scroll down page till end of the page.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver
import sys

@allure.parent_suite("Scrolling")
class VerifyScrollPageEnd(unittest.TestCase):
    """
    :Class Description: Verify scroll down page till end of the page.

    """
    @allure.feature("Verify scroll down page till end of the page.")
    def test_scroll_page_down(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
        driver.maximize_window()  # Maximize window size
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # Scroll down page till end


if __name__ == '__main__':
    unittest.main()
