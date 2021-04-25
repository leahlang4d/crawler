#!/usr/bin/env python
from unittest.mock import patch
import unittest
from requests_html import HTMLSession
import os

from crawler import get_url, parse_links


class Tests(unittest.TestCase):
    @patch('builtins.input', return_value='https://www.rescale.com')
    def test_get_url(self, mocked_input):
        # mocked_input.return_value = 'https://www.rescale.com'
        result = get_url()
        self.assertEqual(result, 'https://www.rescale.com')

    def test_parse_links(self):
        if(os.path.abspath('results.txt')):
            os.remove(os.path.abspath('results.txt'))
        session = HTMLSession()
        result = parse_links('https://www.rescale.com', session, True)
        results = os.stat(os.path.abspath('results.txt')).st_size == 0
        self.assertEqual(results, False)


if __name__ == '__main__':
    unittest.main()