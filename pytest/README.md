
# PyTest

## Unit tests

Unit-Test: unit testing is a software method by which indivual units of source code are tested to determine wheter they are fit for use.

- Tests reduce bugs in new features and existing features.
- Tests are good documentation
- Tests reduce the cost of change.
- Faster debugging
- Faster development
- Better design

## Installation

On a terminal we simply type:

    $ pip install pytest

### 3. Fixtures

In pytest, text fixtures refer to the mechanism pytest provides to allow separation of "getting ready for" and "cleaning up after" code from your test functions.

You can put fixtures into individual test files but to share fixtures among multiple test files, you need to use conftest.py file somewhere centrally  located for all of the tests.

    @pytest.fixture()
    def tasts_db(tmpdir):
    '''Connect to db before tests and disconnect after.'''
    '''Setup : start_db()'''
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    ''' this is where testing happens'''
    yield

    '''Teardown : stop_db() '''
    tasks.stop_tasks_db()


The value of tmpdir is not a string, it is an object that represents a directory. A fixure function runs before the tests are done. 

SETUP -> TESTS -> TEARDOWN


