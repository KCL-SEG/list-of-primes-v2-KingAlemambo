"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def is_prime(num, prime_list):
     for prime in prime_list:   
        if num % prime == 0:
            return False
     return True
     
  
def primes(number_of_primes):
   if number_of_primes<=0:
        raise ValueError("You should provide a positive value")
   prime_list = []
   num=2
   while len(prime_list) < number_of_primes:
        if len(prime_list)==0 or is_prime(num, prime_list):
            prime_list.append(num)
        num+=1
   return prime_list
