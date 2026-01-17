# pro1.py
import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    if len(sys.argv) == 2:
        celsius = float(sys.argv[1])
        print("Fahrenheit:", celsius_to_fahrenheit(celsius))
    else:
        # IMPORTANT: do NOT exit with error
        print("No input provided. Skipping execution.")
