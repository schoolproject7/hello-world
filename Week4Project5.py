organism_amount = int(input("Enter the initial number of organisms: "))
growth = float(input("Enter the rate of growth: "))
rate = int(input("Enter the number of hours to achieve the rate of growth: "))
hours_of_growth = int(input("Enter the total hours of growth: "))

population = organism_amount
hours = 0
while hours < hours_of_growth:
    population *= growth
    hours += rate
