from loguru import logger

# content of test_sample.py

# simple function
def func(x):
    return x + 1

# raise exception
def func_exc():
    raise BaseException('Explicitly raised exception')

# following is use case to test mokeypatch/mocking
class DBClient:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def get_user_details(self, id: str) -> dict:
        logger.debug('original query executed')
        return 'user-data'

    def disconnect(self):
        self.connected = False