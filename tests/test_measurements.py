"""Tests for measurements classes"""
import unittest
from unittest.mock import patch, MagicMock

import requests

from src import measurements

class TestMeasure(unittest.TestCase):
    """Testing class for measure websites"""

    URL = 'http://url.com'

    def setUp(self):
        self.measure = measurements.MeasureLoadingTime()

    def test_measure_loading_time_sucssed(self):
        """Results dictionary should contain loading_time key for valid request"""

        with patch.object(requests, 'get') as mock_get:
            mock_get.return_value = mock_response = MagicMock()
            mock_response.status_code = 200
            self.assertIn('loading_time', self.measure.measure(self.URL))

    def test_measure_loading_time_failed(self):
        """Results dictionary should contain error key for invalid request"""

        with patch.object(requests, 'get') as mock_get:
            mock_get.side_effect = requests.exceptions.MissingSchema
            self.assertIn('error', self.measure.measure(self.URL))
