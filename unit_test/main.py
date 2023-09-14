# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest

class LearnTest(unittest.TestCase):

    def test_func_1(self):
        pass

    def test_func_2(self):
        pass

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):

    def test_sumtest1(self):
        #Arrange
        a=10
        b=10

        #Act
        result= sum(a,b)

        #Assert
        self.assertEqual(result, a+b)

    def test_sumtest2(self):
        #Arrange
        a=10
        b=10

        #Act
        result= sum(b,a)

        #Assert
        self.assertEqual(result, a+b)

class SumTest2(unittest.TestCase):

    def setUp(self):
        print("setup call..")
        self.a=10
        self.b=20
    def tearDown(self):
        print("tearDown...")

    def test_sumtest1(self):
        print("test1...")
        #Act
        result= sum(self.a,self.b)

        #Assert
        self.assertEqual(result, self.a+self.b)

    def test_sumtest2(self):
        print("test2...")
        #Act
        result= sum(self.b,self.a)

        #Assert
        self.assertEqual(result, self.a+self.b)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
