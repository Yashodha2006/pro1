import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter Celsius temperature as a command-line argument.")
        print("Example:")
        print("  python pro1.py 25")
        sys.exit(0)  

    c = float(sys.argv[1])
    print("Fahrenheit:", celsius_to_fahrenheit(c))
