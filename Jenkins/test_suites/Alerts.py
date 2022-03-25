"""
===================
Suite: Alerts.py
===================

:Test Author: https://github.com/Osama-NJ
"""

# Python import
import unittest

# Project import
from Jenkins.test_cases.web.Alerts import VerifyAlertDismiss
from Jenkins.test_cases.web.Alerts import VerifyAlertAccept


class Alerts:

    @staticmethod
    def test_suite():
        # get all tests from classes
        test_alert_dismiss = unittest.TestLoader().loadTestsFromTestCase(VerifyAlertDismiss)
        test_alert_accept = unittest.TestLoader().loadTestsFromTestCase(VerifyAlertAccept)

        # create a test suite
        all_testes = unittest.TestSuite([
            test_alert_dismiss, test_alert_accept
        ])

        # run the suite
        unittest.TextTestRunner(verbosity=2).run(all_testes)
