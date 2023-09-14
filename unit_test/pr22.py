import unittest

class test1():
    pass

class test2():
    pass

class MyTestCase(unittest.TestCase):
    def test_something(self):
        t1=test1()
        t2=test1()
        t3=None
        # self.assertIs(t1,t2)
        # self.assertIsNot(t1, t2)
        # self.assertIsInstance(t1,test1,msg="Instance mismatch")
        # self.assertNotIsInstance(t1,test2)
        # self.assertIsNone(t3)
        # self.assertIsNotNone(t3,msg="not none")
        # self.assertTrue(t1 == t1)
        self.assertFalse(t1 == t2)

if __name__ == '__main__':
    unittest.main()
