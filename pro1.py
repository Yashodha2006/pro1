import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pro1.py <celsius>")
        sys.exit(1)

    c = float(sys.argv[1])
    print(celsius_to_fahrenheit(c))
