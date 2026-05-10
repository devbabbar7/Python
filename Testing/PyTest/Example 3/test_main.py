from main import UserManager
import pytest

# A fixture is like setup in apex test class, it runs before every test function.
@pytest.fixture
def user_manager():
    "Create a fresh instance of UserManager before each test."
    db = UserManager()
    # We use yield when we want to pause execution of the test setup, till the child test functions finish execution so clear() can run once test function has finished executing.
    # we can use return because there is no actual db in our code, if there was we will need to manually clear its state once the test function finished executing.
    yield db 

    # simulate clearing the database before every test run.
    # Required when using an actual database.
    db.users.clear() 

def test_add_user(user_manager):
    assert user_manager.add_user('John_Doe', 'john@example.com') == True
    assert user_manager.get_user('John_Doe') == 'john@example.com'

def test_add_duplicate_user(user_manager):
    assert user_manager.add_user('John_Doe', 'john@example.com') == True
    with pytest.raises(ValueError):
        user_manager.add_user('John_Doe', 'john@example.com')