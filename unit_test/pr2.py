import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a=1
        b=1
        self.assertIs(a,b)
        # self.assertNotEqual(a,b,msg="1 not equal to 10")
        # self.assertEqual(a,b)  # add assertion here


if __name__ == '__main__':
    unittest.main()
