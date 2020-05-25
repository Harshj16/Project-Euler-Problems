#Project euler no 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#tell if all numbers is divisible by 1 to 20
def isdivisibleby1to20(number):
    for iterate in range(2,21):
        if number % iterate != 0:
            return False
    return True

#starting by number 1 , check if its divisible by 1 - 20
number = 20
while True:
    if isdivisibleby1to20(number):
        break
    number += 20 #increment number
#if number found stop
print(number)
