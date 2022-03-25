"""
===========================
VerifyInputBoxDisplayed.py
===========================

:Module Desc: Verify input box is displayed in the page.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver


@allure.parent_suite("InputBoxes")
class VerifyInputBoxDisplayed(unittest.TestCase):
    """
    :Class Description: Verify input box is displayed in the page.

    """
    @allure.feature("Verify input box is displayed in the page.")
    def test_input_box_displayed(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        box_displayed = driver.find_element_by_id("RESULT_TextField-1").is_displayed()
        if box_displayed:
            assert True
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
