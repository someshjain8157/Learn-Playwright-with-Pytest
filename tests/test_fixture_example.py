import pytest


# Runs once for entire test execution
@pytest.fixture(scope="session")
def session_fixture():
    print("\n[SESSION SETUP]")
    yield "Session Data"
    print("\n[SESSION TEARDOWN]")


# Runs once per module/file
@pytest.fixture(scope="module")
def module_fixture():
    print("\n[MODULE SETUP]")
    yield "Module Data"
    print("\n[MODULE TEARDOWN]")


# Runs once per test class
@pytest.fixture(scope="class")
def class_fixture():
    print("\n[CLASS SETUP]")
    yield "Class Data"
    print("\n[CLASS TEARDOWN]")


# Runs before every test
@pytest.fixture(scope="function")
def function_fixture():
    print("\n[FUNCTION SETUP]")
    yield "Function Data"
    print("\n[FUNCTION TEARDOWN]")


# Runs automatically before every test
@pytest.fixture(autouse=True)
def auto_fixture():
    print("\n[AUTO SETUP]")
    yield
    print("\n[AUTO TEARDOWN]")


def test_one(
    session_fixture,
    module_fixture,
    function_fixture
):
    print("Executing Test One")

    print(session_fixture)
    print(module_fixture)
    print(function_fixture)

    assert True


def test_two(
    session_fixture,
    module_fixture,
    function_fixture
):
    print("Executing Test Two")

    assert True


class TestSample:

    def test_three(
        self,
        session_fixture,
        module_fixture,
        class_fixture,
        function_fixture
    ):
        print("Executing Test Three")

        assert True

    def test_four(
        self,
        session_fixture,
        module_fixture,
        class_fixture,
        function_fixture
    ):
        print("Executing Test Four")

        assert True