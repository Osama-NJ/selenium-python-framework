"""
=====================
Suite: InputBoxes.py
=====================

:Test Author: https://github.com/Osama-NJ
"""


# Python import
import unittest

# Project import
from Jenkins.test_cases.web.InputBox import Verify_Input_Boxes_Count
from Jenkins.test_cases.web.InputBox import Verify_Input_Box_Displayed
from Jenkins.test_cases.web.InputBox import Verify_Input_Box_Value


class InputBoxes:

    @staticmethod
    def test_suite():
        # get all tests from classes
        test_input_boxes_count = unittest.TestLoader().loadTestsFromTestCase(Verify_Input_Boxes_Count)
        test_input_box_displayed = unittest.TestLoader().loadTestsFromTestCase(Verify_Input_Box_Displayed)
        test_input_box_value = unittest.TestLoader().loadTestsFromTestCase(Verify_Input_Box_Value)

        # create a test suite
        all_testes = unittest.TestSuite([
            test_input_boxes_count, test_input_box_displayed, test_input_box_value
        ])

        # run the suite
        unittest.TextTestRunner(verbosity=2).run(all_testes)
