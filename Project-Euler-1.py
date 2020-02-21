#Project Euler No.1
#If we list all the natural numbers below 10 that are multiples of 3 or 5
#we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#definig natural number
num = int(input("Enter number = "))
add = 0
for iterate in range(1,num):
    if(iterate%3==0 or iterate%5==0):
        add = add+iterate
print(add)
