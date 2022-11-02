# Pytest for Unit Testing
The `app_test.py` contains the test cases and `app.py` has the required function implementations.
Topics to cover
1. Asserts - assert statements. simple asset and with `pytest.raise(<ExceptionClass>): function_call()`
2. Parametrization - test a function with multiple inputs using `@pytest.mark.parametrize`
3. Fixture - `@pytest.fixture` any resource -> (configured database, dataset, environment, variables, entity object, etc). safe teardown by `yield`(recommended) or `addfinalizer`(callback)
4. Mocking - `monkeypatch`, a fixture which is alrady available, helps to update objects' attrs for that test only. Like code invoking network call, oauth, etc.
5. Lifecycle -
  - `pytest` command is run
  - It discovers all the tests based on standard test discovery
  - identifies all the fixtures
  - Before running a test, loads all the fixtures.
  - Runs a test, the fixtures are destroyed / teardown
  - Repeats for all the tests.
  - Stops where it fails, does not necessarily complete all the tests.
  - Tests can be skipped conditionally
  - Tests can be run with multiple inputs using parametrize
  - Results are shown
