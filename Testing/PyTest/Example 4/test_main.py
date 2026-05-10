from main import is_prime
import pytest

@pytest.mark.parametrize("num, expected", {
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False)
})

def test_is_prime(num, expected):
    assert is_prime(num) == expected
    
if __name__ == "__main__":
    pytest.main()

