def numbersAverage(x):
    total = 0
    for number in x:
        total += float(number)
    return total/len(x)

def main():
    fname = input("Enter a file name here: ")

    try:
        numbers = open(fname,"r").read().split()
        avg = numbersAverage(numbers)
        print("The average is ", avg)
    except:
        print("Invalid criteria")

main()
