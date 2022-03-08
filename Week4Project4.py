height = int(input("Enter the height here: "))
bounce_index = float(input("Enter the bounciness index of the ball here: "))
number_of_bounces = float(input("Enter the number of bounces here: "))

distance = 0

while number_of_bounces > 0:
    distance = distance * height
    height = height * bounce_index
    distance = distance * height
    number_of_bounces -= 1
    print("Total distance is: ", distance)
