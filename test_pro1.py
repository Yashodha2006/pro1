from pro1 import celsius_to_fahrenheit

def test_zero_celsius():
    c = 0
    assert celsius_to_fahrenheit(c) == 32
