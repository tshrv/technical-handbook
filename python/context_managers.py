"""
Context managers are used to manage the creation and teardown of resources before and after scope of usage
__enter__ and __exit__ methods have to be defined in these classes
__init__ -> initialization on object creation
__enter__ -> getting the resource ready for usage, returns the resource
__exit__ -> resource teardown
"""
from loguru import logger
from contextlib import contextmanager


class DBClient:
    def __init__(self, host, port, database) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.connection = False
    
    def connect(self):
        # create connection
        self.connection = True
        logger.debug('connected')
    
    def disconnect(self):
        # destroy connection
        self.connection = False
        logger.debug('disconnected')
    
    def get_user(self):
        if not self.connection:
            raise ConnectionRefusedError('connection closed')
        return 'john.doe@example.com'


class ContextManagedDBClient(DBClient):
    def __enter__(self) -> 'ContextManagedDBClient':
        logger.info('entering')
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.disconnect()
        logger.info('exiting')

@contextmanager
def context_managed_dbclient(host, port, database):
    try:
        # build
        logger.info('building')
        client = DBClient(host, port, database)
        client.connect()

        # yield
        yield client
    
    finally:
        # teardown
        client.disconnect()
        logger.info('teardown')

def main():
    host = 'HOST'
    port = 'PORT'
    database = 'DATABASE'
    # --------------------------------------------------------------------------------------

    # without context manager, connection leakage : dbc_1
    logger.info('without context manager, demonstrate connection leakage')
    dbc_1 = DBClient(host, port, database)
    dbc_1.connect()
    user = dbc_1.get_user()
    logger.info(f'user: {user}')

    logger.debug(f'connection status w/o explicitly closing {dbc_1.connection}')
    # connection has to be explicitly closed
    # connections can be leaked and eventually db will refuse to establish more connections
    dbc_1.disconnect()
    logger.debug('-'*50)
    # --------------------------------------------------------------------------------------

    # with context manager: dbc_2
    logger.info('with context manager: dbc_2')
    with ContextManagedDBClient(host, port, database) as dbc_2:
        user = dbc_2.get_user()
        logger.info(f'user: {user}')
    
    logger.info(f'connection status w/o explicitly closing {dbc_2.connection}')
    logger.debug('-'*50)
    # --------------------------------------------------------------------------------------

    # with decorated context manager: dbc_3
    logger.info('with decorated context manager: dbc_3')

    with context_managed_dbclient(host, port, database) as dbc_3:
        user = dbc_3.get_user()
        logger.info(f'user: {user}')
    
    logger.info(f'connection status w/o explicitly closing {dbc_3.connection}')

main()

    