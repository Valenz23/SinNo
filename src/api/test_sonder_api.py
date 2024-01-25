import hug
import unittest

import sonder_api as api

class TestSonderApi(unittest.TestCase):
    def test_status(self):
        data = hug.test.get(api,'/status')
        self.assertEqual(data.status, '200 OK')
        self.assertEqual(data.data['status'], 'OK')

    def test_not_found(self):
        data = hug.test.get(api, '/error')
        self.assertEqual(data.status, '404 Not Found')
    
    def test_buscar_cancion(self):
        data = hug.test.get(api, '/buscar')
        self.assertEqual(data.status, '')

if __name__ == '__main__':
    unittest.main()