from . import sonder_api as api

import hug
import unittest

class TestSonderApi(unittest.TestCase):

    def test_api_status(self):
        data = hug.test.get(api,'/status')
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_not_found(self):
        data = hug.test.get(api, '/error')
        self.assertEqual(data.status, hug.HTTP_404)

    def test_api_buscar_cancion_correct(self):
        data = hug.test.get(api,'/buscar', {'atributo':'artista','valor':'dragon'})
        self.assertEqual(data.status, hug.HTTP_200)

    # def test_buscar_cancion_fail(self):
    #     data = hug.test.get(api,'/buscar', {'atributo':'none','valor':'none'}) 
    #     self.assertEqual(data.status, hug.HTTP_404)

    def test_api_add_cancion(self):
        data = hug.test.put(api, '/add', {'artista':'test', 'titulo':'test', 'letra':'test'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'9999'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_add_lote(self):
        data = hug.test.put(api, '/lote', {'path':'BBDD/lote.csv'})
        self.assertEqual(data.status, hug.HTTP_200)
    
if __name__ == '__main__':
    unittest.main()