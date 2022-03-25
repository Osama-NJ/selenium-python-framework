"""
========================
VerifyScrollByPixels.py
========================

:Module Desc: Verify scroll down the page by pixels.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver


@allure.parent_suite("Scrolling")
class VerifyScrollByPixels(unittest.TestCase):
    """
    :Class Description: Verify scroll down the page by pixels.

    """
    @allure.feature("Verify scroll down the page by pixels.")
    def test_scroll_by_pixels(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
        driver.maximize_window()  # Maximize window size
        driver.execute_script("window.scrollBy(0,10000)")   # Scroll down page by pixels


if __name__ == '__main__':
    unittest.main()
