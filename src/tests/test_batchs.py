import unittest
import time

class Testing(unittest.TestCase):
    def test_0_adding_batch_songs(self):
        a = 'some'
        b = 'some'
        time.sleep(4.5)
        self.assertEqual(a, b)

    def test_1_removing_batch_songs(self):
        a = 'some'
        b = 'some'
        time.sleep(3.8)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()