"""Module containing classes for measure websites"""
import requests
import time

class MeasureLoadingTime:
    """Class for measure loading time of website"""

    def measure(self, url):
        """Method to make and store results of request in results dictionary
            
        Args:
            url (str): url of website
        """

        result = {'url': url}
        try:
            time_start = time.time()
            requests.get(url)
            result['loading_time'] = time.time() - time_start
        except requests.exceptions.RequestException as e:
            result['error'] = f'Unable to connect to {url}. {e}'

        return result
