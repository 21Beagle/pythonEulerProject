def primefactor(n):
    factors: list[int] = []
    primes: list[int] = []
    primesfinal: list[int] = []
    for i in range(3, int(n**0.5) + 1, 2):
        print(str(factors), ", ", str(i / n**0.5))
        if n % i == 0:
            factors.append(i)
    factors.reverse()
    print(str(factors))
    for i in range(0, len(factors)):
        for j in range(i + 1, len(factors)):
            if factors[i] % factors[j] == 0:
                primes.append(factors[i])
    print(str(primes))
    for item in factors:
        if item not in primes:
            primesfinal.append(item)
    print(str(primesfinal))


primefactor(600851475143)
