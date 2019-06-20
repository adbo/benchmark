"""Tests for measurements classes"""

import unittest

import src.measurements as measure

class TestMeasureLoadingTime(unittest.TestCase):
    """Testing class for measure loading time"""

    GOOGLE_URL = 'http://google.com'

    def setUp(self):
        self.measure_google = measure.MeasureLoadingTime(self.GOOGLE_URL)

    def test_url(self):
        """Testing for url member"""
        self.assertEqual(self.measure_google.url, self.GOOGLE_URL)
