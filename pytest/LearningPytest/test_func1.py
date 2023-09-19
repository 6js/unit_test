import pytest


def testLogin():
    print("logiin successful")

@pytest.mark.sanity
def testLogOff():
    print("logoff successful")

@pytest.mark.skip
def testCalc():
    assert 2 + 2 == 4

@pytest.mark.xfail
def testCalc1():
    assert 2 + 2 == 4
