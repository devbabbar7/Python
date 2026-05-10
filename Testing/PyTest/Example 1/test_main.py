from main import get_weather
import pytest

def test_get_weather():
    assert get_weather(21) == 'Hot'
    assert get_weather(15) == 'Cold'
    assert get_weather(20) == 'Cold'