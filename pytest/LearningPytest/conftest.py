import pytest


# @pytest.fixture(scope="session",autouse=True)
# def tc_setUp():
#     print("Launch browser")
#     print("Login")
#     print("Browse product")
#     yield  #tearDown
#     print("Logoff")
#     print("Close")

@pytest.fixture(scope="session",autouse=True)
def tc_setUp(browser):
    if browser=="chrome":
        print("Launch chrome")
    elif browser=="ff":
        print("Launch firefox")
    else:
        print("invalid")
    # print("Launch browser")
    print("Login")
    print("Browse product")
    yield  #tearDown
    print("Logoff")
    print("Close")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return request.config.getoption("browser")