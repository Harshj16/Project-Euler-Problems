#Project Euler No. 4
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def pallindrom(n):
	a=str(n)
	b=a[::-1]
	if(a==b):
		return True
p=0
lp=0
for i in range(100,1000):
	for j in range(100,1000):
		p=i*j
		if(pallindrom(p)):
			if(p>lp):
				lp=p
print(lp)


            
    
