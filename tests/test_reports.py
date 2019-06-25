"""Tests for reports classes"""
import io
import unittest
from unittest.mock import patch, mock_open

import src.reports as reports

class TestReportLoadingTime(unittest.TestCase):
    """Testing report loading time"""

    MESSAGE = 'test log'
    PATH = 'output.txt'

    def setUp(self):
        self.report_to_file = reports.ReportToFile(self.PATH)
        self.report_to_console = reports.ReportToConsole()

    def test_log_to_file(self):
        open_mock = mock_open()
        with patch("src.reports.open", open_mock, create=True):
            self.report_to_file.report(self.MESSAGE)
            open_mock.assert_called_with(self.PATH, 'w')
            open_mock.return_value.write.assert_called_once_with(self.MESSAGE)

    def test_log_to_console(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_console:
            self.report_to_console.report(self.MESSAGE)
            self.assertEqual(mock_console.getvalue(), self.MESSAGE + '\n')