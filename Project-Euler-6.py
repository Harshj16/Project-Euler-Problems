#Project euler no 6
#The sum of the squares of the first ten natural numbers is,385
#The square of the sum of the first ten natural numbers is,3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#3025−385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
natural_sum = 0
square_of_sum = 0
for  i in range(1,101):
    natural_sum = i**2 + natural_sum #Sum of squares of 100 natural numbers
    square_of_sum = i + square_of_sum #the square of the sum
print((square_of_sum **2)-natural_sum) #printing difference


    
    

