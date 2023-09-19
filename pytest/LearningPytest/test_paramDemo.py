import pytest

# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)


@pytest.mark.parametrize("a,b,final",[(2,6,8),(2,4,8)])
def testAdd(a,b,final):
    assert a+b==final


# def testLogin(demo_fixture):
#     print("logiin successful")


# def testLogOff():
#     print("logoff successful")
#
#
# def testCalc():
#     assert 2 + 2 == 4


