import hug
import unittest

import sonder_api as api

class TestSonderApi(unittest.TestCase):
    def test_status(self):
        data = hug.test.get(api,'/status')
        self.assertEqual(data.status, '200 OK')
        self.assertEqual(data.data['status'], 'OK')


if __name__ == '__main__':
    unittest.main()