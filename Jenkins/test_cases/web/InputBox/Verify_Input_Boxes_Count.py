"""
========================
VerifyInputBoxesCount.py
========================

:Module Desc: Verify input boxes count in the page.

:Test Author: https://github.com/Osama-NJ

"""

# Python imports
import allure
import unittest
from selenium import webdriver


@allure.parent_suite("InputBoxes")
class VerifyInputBoxesCount(unittest.TestCase):
    """
    :Class Description: Verify input boxes count in the page.

    """
    @allure.feature("Verify input boxes count in the page.")
    def test_input_boxes_count(self):
        driver = webdriver.Chrome('../../../driver/chromedriver.exe')
        driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
        inputboxes = driver.find_elements_by_class_name("text_field")
        if int(inputboxes) == 6:
            assert True
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
