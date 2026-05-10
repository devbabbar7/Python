from main import save_user
import pytest

"""
Instead of running a real function (e.g., sending an actual email), a mock stands in its place and returns a predefined value.
You don't have to call any real api or email service. Also you can perform test even if service is not yet created or is downed.
"""
def test_save_user(mocker):
    mock_conn = mocker.patch('main.sqlite3.connect')
    mock_cursor = mock_conn.return_value.cursor.return_value
    save_user('John', 30)
    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with(
        'INSERT INTO users (name, age) VALUES (?, ?)', ('John', 30)
    )
    
if __name__ == "__main__":
    pytest.main()
