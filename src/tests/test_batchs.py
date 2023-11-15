import unittest
import time

class Testing(unittest.TestCase):
    def test_adding_batch_songs(self):
        a = 'some'
        b = 'some'
        time.sleep(5)
        self.assertEqual(a, b)

    def test_removing_batch_songs(self):
        a = 'some'
        b = 'some'
        time.sleep(5)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()