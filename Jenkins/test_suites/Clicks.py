"""
===================
Suite: Clicks.py
===================

:Test Author: https://github.com/Osama-NJ
"""

# Python import
import unittest

# Project import
from Jenkins.test_cases.web.Clicks import VerifyDoubleClick


class Clicks:

    @staticmethod
    def test_suite():
        # get all tests from classes
        test_double_click = unittest.TestLoader().loadTestsFromTestCase(VerifyDoubleClick)

        # create a test suite
        all_testes = unittest.TestSuite([
            test_double_click
        ])

        # run the suite
        unittest.TextTestRunner(verbosity=2).run(all_testes)
