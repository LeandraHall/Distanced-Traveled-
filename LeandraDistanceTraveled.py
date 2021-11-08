#Using the distance formula (Distance = Speed x time) this
#code with calculate the distance traveled by a car
#going 70 mph for 6, 10, & 15 hours

#The speed of the car set to a constant variable
constantCarSpeed = 70

#The different times for the distance equation
time1 = 6
time2 = 10
time3 = 15

#The distance equations for each time the car travels
distanceOne = constantCarSpeed * time1
distanceTwo = constantCarSpeed * time2
distanceThree = constantCarSpeed * time3

#The print functions to display the results of
#the equations
print("If the car travels at 70 miles per hour for 6 hours,", end="")
print(" then it has traveled " + str(distanceOne) + " miles.")
print("If the car travels for 10 hours,", end="")
print(" then it has traveled " + str(distanceTwo) + " miles.")
print("If the car travels for 15 hours,", end="")
print(" then it has traveled " + str(distanceThree) + " miles.")