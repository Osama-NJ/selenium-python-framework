"""
===================
Suite: Dropdown.py
===================

:Test Author: https://github.com/Osama-NJ
"""

# Python import
import unittest

# Project import
from Jenkins.test_cases.web.Dropdown import Verify_Dropdown_Morning
from Jenkins.test_cases.web.Dropdown import Verify_Dropdown_Afternoon
from Jenkins.test_cases.web.Dropdown import Verify_Dropdown_Evening


class Dropdown:

    @staticmethod
    def test_suite():
        # get all tests from classes
        test_dropdown_morning = unittest.TestLoader().loadTestsFromTestCase(Verify_Dropdown_Morning)
        test_dropdown_afternoon = unittest.TestLoader().loadTestsFromTestCase(Verify_Dropdown_Afternoon)
        test_dropdown_evening = unittest.TestLoader().loadTestsFromTestCase(Verify_Dropdown_Evening)

        # create a test suite
        all_testes = unittest.TestSuite([
            test_dropdown_morning, test_dropdown_afternoon, test_dropdown_evening
        ])

        # run the suite
        unittest.TextTestRunner(verbosity=2).run(all_testes)
