from pro1 import celsius_to_fahrenheit

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32

def test_normal_value():
    assert celsius_to_fahrenheit(25) == 77

def test_negative_value():
    assert celsius_to_fahrenheit(-40) == -40
