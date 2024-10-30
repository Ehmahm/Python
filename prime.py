def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_primes(limit):
    primes_found = 0
    for num in range(2, limit+1):
        if is_prime(num):
            primes_found += 1
            print(f"{num} is a prime number.")

            if primes_found == 5:
                print("Found 5 primes. Stopping.")
                break
        
        else:
            pass 

find_primes(50)