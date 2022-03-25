"""
========================
VerifyDropdownEvening.py
========================

:Module Desc: Verify dropdown list by clicking Evening.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@allure.parent_suite("Dropdown")
class VerifyDropdownEvening(unittest.TestCase):
    """
    :Class Description: Verify dropdown list by clicking Evening.

    """
    @allure.feature("Verify dropdown list by clicking Evening.")
    def test_dropdown_evening(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        driver.maximize_window()
        element = driver.find_element_by_id("RESULT_RadioButton-9")
        drp = Select(element)

        # select by value
        drp.select_by_value("Radio-2")  # Evening


if __name__ == '__main__':
    unittest.main()
