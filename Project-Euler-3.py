#Project Euler No 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143
#First we will find the factors
import math
def getfactors(number):
    factors = []
    for iteration in range(1, int(math.sqrt(number))+1):
        if number % iteration == 0:
            factors.append(iteration)
            factors.append(number//iteration)
    return factors


#Once we get the factors list
#Find the prime numbers from that list
def isprime(number):
    return len(getfactors(number)) == 2


allfactors = getfactors(600851475143)


#Finding the lagest number
largestprimefactor = 0
for prime_factors in allfactors:
    if isprime(allfactors) and prime_factor > largestprimefactor :
        largestprimefactor = factor

print(largestprimefactor)        
