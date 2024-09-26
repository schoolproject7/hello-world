hourlyWage = int(input("Enter hourly wage here: "))
regularHours = int(input("Enter regular hours: "))
overTime = int(input("Enter total overtime hours here: "))
weeklyPay = (hourlyWage * regularHours) + (overTime * hourlyWage * 1.5)

print('The total weekly pay is', weeklyPay)
