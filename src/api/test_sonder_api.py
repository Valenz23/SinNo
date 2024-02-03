from . import sonder_api as api

import hug
import unittest

class TestSonderApi(unittest.TestCase): 

    def test_api_status(self):
        data = hug.test.get(api,'/status')
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_buscar_cancion(self):
        data = hug.test.get(api,'/buscar', {'atributo':'artista','valor':'dragon'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_add_cancion(self):
        data = hug.test.put(api, '/add', {'artista':'test', 'titulo':'test', 'letra':'test'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_delete_cancion(self):
        data = hug.test.delete(api, '/del', {'id':'9999'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_add_lote(self):
        data = hug.test.put(api, '/lote', {'path':'BBDD/lote.csv'})
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_listar_canciones(self):
        data = hug.test.get(api, '/lista')
        self.assertEqual(data.status, hug.HTTP_200)

    def test_api_modificar_letra(self):
        data = hug.test.put(api, '/mod', {'id':'1004','letra':'api letra'})
        self.assertEqual(data.status, hug.HTTP_200)
    
if __name__ == '__main__':
    unittest.main()