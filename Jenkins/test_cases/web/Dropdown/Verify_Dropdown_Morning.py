"""
========================
VerifyDropdownMorning.py
========================

:Module Desc: Verify dropdown list by clicking Morning.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@allure.parent_suite("Dropdown")
class VerifyDropdownMorning(unittest.TestCase):
    """
    :Class Description: Verify dropdown list by clicking Morning.

    """
    @allure.feature("Verify dropdown list by clicking Morning.")
    def test_dropdown_morning(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        driver.maximize_window()
        element = driver.find_element_by_id("RESULT_RadioButton-9")
        drp = Select(element)

        # select by visible text
        drp.select_by_visible_text("Morning")  # Morning


if __name__ == '__main__':
    unittest.main()
