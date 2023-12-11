import pytest
from lab_04 import *

operators = {'+', '-', '*', '/', '^'}

def test_1():
    example = ["10","5","+"]
    result = token_list(example)
    assert result == 15

def test_2():
    example = ["3", "7", "*", "/", "(", "3", "4", "+", ")"]
    result = token_list(example)
    assert result == 3

def test_3():
    example = ["4", "5", "*", "*", "(", "2", "5", "*", "2", "^", ")"]
    result = token_list(example)
    assert result == 1000


if __name__ == "__main__":
    pytest.main()

    