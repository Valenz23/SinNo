import unittest
import time

class Testing(unittest.TestCase):
    def test_0_creating_songs(self):
        a = 'some'
        b = 'some'
        time.sleep(0.5)
        self.assertEqual(a, b)

    def test_1_modifying_songs(self):
        a = 'some'
        b = 'some'        
        time.sleep(1)
        self.assertEqual(a, b)

    def test_2_removing_songs(self):
        a = 'some'
        b = 'some'
        time.sleep(0.3)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()