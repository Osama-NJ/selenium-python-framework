"""
========================
VerifyScrollToElement.py
========================

:Module Desc: Verify scroll down the page till the element is visible

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver


@allure.parent_suite("Scrolling")
class VerifyScrollToElement(unittest.TestCase):
    """
    :Class Description: Verify scroll down the page till the element is visible.

    """
    @allure.feature("Verify scroll down the page till the element is visible.")
    def test_scroll_to_element(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
        driver.maximize_window()  # Maximize window size
        flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[26]/td[1]/img')
        driver.execute_script("arguments[0].scrollIntoView() ;", flag)   # Scroll down page till the element is visible


if __name__ == '__main__':
    unittest.main()
