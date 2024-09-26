theSum = 0
count = 0

data = input("Enter a number or press enter to quit: ")

while data!="":

    number = float(data)

    theSum += number
    count += 1

    data = input("Enter a number or press Enter ro quit: ")

print("The sum is",theSum)
print("The average is",theSum/count)
