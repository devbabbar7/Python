from main import get_weather
import pytest

"""
Instead of running a real function (e.g., sending an actual email), a mock stands in its place and returns a predefined value.
You don't have to call any real api or email service. Also you can perform test even if service is not yet created or is downed.
"""
def test_get_weather(mocker):
    # main = file name, mocking requests.get
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": 'Sunny'}
    
    result = get_weather('Dubai')
    assert result == {"temperature": 25, "condition": 'Sunny'}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
    
if __name__ == "__main__":
    pytest.main()
