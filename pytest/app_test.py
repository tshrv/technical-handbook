from typing import Optional

import app
import pytest
from loguru import logger

# test simple function
def test_answer_valid():
    assert app.func(4) == 5

def test_answer_invalid():
    assert app.func(3) != 5

# test exception
def test_func_exc():
    with pytest.raises(BaseException):
        app.func_exc()

# combining tests in a class
class TestFunc:
    def test_func_valid(self):
        assert app.func(4) == 5

    def test_func_invalid(self):
        assert app.func(3) != 5

# use a temporary directory, builtin fixture from pytest
# there are a lot of builtin fixtures available from pytest, pytest --fixtures
def test_needsfiles(tmp_path):
    logger.debug(tmp_path)
    assert tmp_path is not None
    # assert 0

# Fixtures
@pytest.fixture
def user_object():
    user = {
        'id': 1214,
        'name': 'Mohan Sharma',
        'department': 'Digital Transformations',
    }
    logger.debug('user object created')
    yield user
    logger.debug('teardown complete')
    # teardown

@pytest.fixture
def user_object_w_finalizer(request):
    user = {
        'id': 1214,
        'name': 'Mohan Sharma',
        'department': 'Digital Transformations',
    }
    def cleanup():
        logger.debug('teardown complete')
    request.addfinalizer(cleanup)
    return user

class TestUser:
    def test_user(self, user_object):
        logger.debug(user_object)
        assert user_object['id'] == 1214
    def test_user_w_finaliser(self, user_object_w_finalizer):
        logger.debug(user_object_w_finalizer)
        assert user_object_w_finalizer['id'] == 1214
        assert user_object_w_finalizer['name'] == 'Mohan Sharma'

# @use_fixtures
@pytest.mark.usefixtures("user_object")
def test_user_object():
    logger.debug('testing user object')
    # logger.debug(user_object)
    # user_object is a function here not an accessible object
    # but it is initiated before initiating the test marked by it
    # used for any environment setup, change to new dir, execute test, change to old dir


# Parametrization
# @pytest.mark.parametrize("input_value, expected_output", ((1, 2), (3, 4), (9, 10)))
@pytest.mark.parametrize(('input_value', 'expected_output'), ((1, 2), (3, 4), (9, 10)))
def test_func_w_parameters(input_value, expected_output):
    logger.debug((input_value, expected_output))
    assert app.func(input_value) == expected_output

# parametrize a test function like above
# a class consists of test functions by decorating the class
@pytest.mark.parametrize(('inp_val', 'exp_val'), ((1, 2), (3, 4), (9, 10)))
class TestFuncParametrized:
    def test_func_1(self, inp_val, exp_val):
        logger.debug((inp_val, exp_val))
        assert app.func(inp_val) == exp_val

    def test_func_2(self, inp_val, exp_val):
        logger.debug((inp_val, exp_val))
        assert app.func(inp_val+1) == exp_val+1

    def test_func_3(self, inp_val, exp_val):
        logger.debug((inp_val, exp_val))
        assert app.func(inp_val-1) == exp_val-1

@pytest.fixture
def dbclient():
    client = app.DBClient()
    yield client
    client.disconnect()

# monkeypatch / mocking
def mocked_get_user_details(id:str) -> Optional[str]:
    logger.debug('mock query executed')
    if id == '1214':
        return 'user-data'
    else:
        return None

class TestDBClient:
    def test_get_user_details(self, dbclient):
        user_data = dbclient.get_user_details(id='1214')
        assert user_data == 'user-data'
        # invoked database call, not unit testing
        # use monkeypatching to mock the database call

    def test_get_user_details_mocked_query(self, dbclient, monkeypatch):
        monkeypatch.setattr(dbclient, 'get_user_details', mocked_get_user_details)
        user_data = dbclient.get_user_details(id='1214')
        assert user_data == 'user-data'
        # used monkeypatching to mock the database call