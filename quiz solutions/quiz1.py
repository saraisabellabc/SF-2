def isPrime(n:int)-> bool:
    if n < 2:
        return False
    for i in range(int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(isPrime(int(input())))

primes =[]
n = 2
while len(primes) < 100:
    if isPrime(n):
        primes.append(n)
    else:
        n += 1 
    
