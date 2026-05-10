from main import UserService, APIClient
import pytest

"""
Instead of running a real function (e.g., sending an actual email), a mock stands in its place and returns a predefined value.
You don't have to call any real api or email service. Also you can perform test even if service is not yet created or is downed.
"""
def test_save_user(mocker):
    mock_api_client = mocker.Mock(spec=APIClient) # Create a mock API client.
    # Mock get_user_data
    mock_api_client.get_user_data.return_value = {"id": 1, "name": "John"}
    service = UserService(mock_api_client)
    result = service.get_username(1)
    assert result == 'JOHN'
    mock_api_client.get_user_data.assert_called_once_with(1)

if __name__ == "__main__":
    pytest.main()