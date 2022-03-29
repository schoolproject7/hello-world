numbers = [5, 7, 10, 3, 5, 9]

def median(numbers):
    if lin(numbers) == 0:
        return 0

numbers.sort()
midpoint = int(len(numbers) / 2)
print("The median is", end = " ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

def mode(numbers):
    counts = []
    for items in numbers:
        counts[item] += 1
    else:
        counts[item] = 1

    return [key for key in counts.keys() if counts[key] == max(counts.values())]

def mean(numbers):
    if len(numbers) == 0:
        return 0
    total(0)
    for number in numbers:
        total += number
        return total/len(numbers)
    

def main():
    print("List", numbers)
    print("Mode:", mode(numbers))
    print("Median:", median(numbers))
    print("Mean:", mean(numbers))


main()

