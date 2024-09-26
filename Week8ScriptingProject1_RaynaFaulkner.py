import math
tolerance = 0.000001
estimate = 1.0

def newton(n, estimate):
        estimate = (estimate + n / estimate) /2
        difference = abs(n - estimate ** 2)
        if difference <= tolerance:
            return estimate
        else:
            return newton(n, estimate)

def main():
    while True:
        try:
            number = float(input("Please enter a positive number\n"))
            print("The program's estimate is",newton(number, estimate))
            print("Python's estimate is ", math.sqrt(number))
        except Exception as x:
            print(x)
            break

if __name__ == "__main__":
    main()
