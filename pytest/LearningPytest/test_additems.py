import pytest


def testLogin():
    print("logiin successful")


def testLogOff():
    print("logoff successful")

@pytest.mark.sanity
def testCalc():
    assert 2 + 2 == 4