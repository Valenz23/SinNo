import unittest
import time

class Testing(unittest.TestCase):
    def test_0_creating_users(self):
        a = 'some'
        b = 'some'
        time.sleep(0.5)
        self.assertEqual(a, b)

    def test_1_modifying_users(self):
        a = 'some'
        b = 'some'
        time.sleep(0.7)
        self.assertEqual(a, b)

    def test_2_removing_users(self):
        a = 'some'
        b = 'some'
        time.sleep(0.3)
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()