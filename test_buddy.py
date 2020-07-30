import unittest
from buddy_pair import buddy

#go to terminal:$ python -m test_buddy

class MyTestCase(unittest.TestCase):
    def test_buddy_pair(self):
        pair = buddy(48, 50)
        self.assertEqual(pair, [48, 75])

    def test_buddy_pair2(self):
        pair = buddy(10, 50)
        self.assertEqual(pair, [48, 75])

    def test_buddy_None(self):
        pair = buddy(1000, 500)
        self.assertEqual(pair, None)

    def test_buddy_another_pair(self):
        pair = buddy(100, 5000)
        self.assertEqual(pair, [140, 195])


if __name__ == '__main__':
    unittest.main()
