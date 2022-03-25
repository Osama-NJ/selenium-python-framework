"""
===================
Suite: Scrolling.py
===================

:Test Author: https://github.com/Osama-NJ
"""

# Python import
import unittest

# Project import
from Jenkins.test_cases.web.Scrolling import Verify_Scroll_By_Pixels
from Jenkins.test_cases.web.Scrolling import Verify_Scroll_To_Element
from Jenkins.test_cases.web.Scrolling import Verify_Scroll_Page_End


class Scrolling:

    @staticmethod
    def test_suite():
        # get all tests from classes
        test_scroll_by_pixels = unittest.TestLoader().loadTestsFromTestCase(Verify_Scroll_By_Pixels)
        test_scroll_to_element = unittest.TestLoader().loadTestsFromTestCase(Verify_Scroll_To_Element)
        test_scroll_page_end = unittest.TestLoader().loadTestsFromTestCase(Verify_Scroll_Page_End)

        # create a test suite
        all_testes = unittest.TestSuite([
            test_scroll_by_pixels, test_scroll_to_element, test_scroll_page_end
        ])

        # run the suite
        unittest.TextTestRunner(verbosity=2).run(all_testes)
