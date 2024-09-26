import math
TOLERANCE = 0.000001

def newton(x, estimate):
    estimate = (estimate + x / estimate) / 2
    difference = abs (x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton (x, estimate)

def main():
    while True:
        x = input("Enter a positive number here: ")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("The program's estimate is", newton(x, estimate))
        print("Python's estimate is ", math.sqrt(x))
if __name__ == "__main__":
    main()
