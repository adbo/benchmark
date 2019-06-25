"""Tests for comparators classes"""
import unittest

import src.comparators as comparators

class TestCompareAndSendEmailOrSms(unittest.TestCase):
    """Tests for CompareAndSendEmailOrSms"""

    COMPARED_RESULTS = {'url': 'http://google.com', 'loading_time': 1}
    COMPETITORS_RESULTS = (
        {'url': 'http://bing.com', 'loading_time': 1.2},
        {'url': 'http://yahoo.com', 'loading_time': 1.3},
        {'url': 'http://ask.com', 'loading_time': 1.5})

    def setUp(self):
        self.comparator = comparators.Comparator()

    def test_compare(self):
        self.comparator.compare(self.COMPARED_RESULTS, self.COMPETITORS_RESULTS)