import unittest
import time

class Testing(unittest.TestCase):
    def test_0_creating_liked_list(self):
        a = 'some'
        b = 'some'
        time.sleep(0.7)
        self.assertEqual(a, b)

    def test_1_adding_songs_to_liked_list(self):
        a = 'some'
        b = 'some'
        time.sleep(1.5)
        self.assertEqual(a, b)

    def test_2_removing_songs_to_liked_list(self):
        a = 'some'
        b = 'some'
        time.sleep(0.5)
        self.assertEqual(a, b)

    def test_3_removing_liked_list(self):
        a = 'some'
        b = 'some'
        time.sleep(0.3)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()