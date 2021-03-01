


##Here we have a function that finds the number of primes below a number n. We know that we only need to test all the prime numbers up to squareroot(n) this speeds up the process.
def primesUnder(n):
    ##We define two arrays. One is the primes we have found and the other is all the primes up to squareroot(n) 
    primes = [2]
    primestest = [2]

    #For every odd number between 3 and n (3 because 2 is already added to the list and we know 3 is prime) we divide by all the numbers in the primetest array. iff all of them have a remainder we append i to primes list
    for i in range(3, n, 2):
        if all(i % prime != 0 for prime in primestest):
            primes.append(i)
            #We only append i to the primestest array if it is less than squareroot(n) this reduces the search space and computation time since testing any number greater than squareroot(n) is useless if we have already tested every prime below it.
            if i <= n ** 0.5:
                primestest.append(i)
    return primes



print(primesUnder(200))