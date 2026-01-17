from pro1 import celsius_to_fahrenheit

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_negative_value():
    assert celsius_to_fahrenheit(-40) == -40
