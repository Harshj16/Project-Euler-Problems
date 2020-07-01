# Project Euler No 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#defining the list to find prime number
#if number is divisible by any of the number in between 2-9 it is not prime
def find_prime():
    prime_to_find  = 10001
    list_primes = []
    x = 2
    while(len(list_primes) < prime_to_find): # It checks wether the numbers is lsit does not exceed the prime to find
        if all(x % prime for prime in list_primes): # all checks all is true the only procced further
            list_primes.append(x)
        x +=1
    print(list_primes[-1])
find_prime()
        
