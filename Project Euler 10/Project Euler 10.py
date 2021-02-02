import time


def primesbelow(n):
    start = time.process_time()
    primes = [2]
    primestest = []
    m = 0
    for i in range(max(primes), int(n)):
        m += 1
        if all(i % prime != 0 for prime in primestest):
            primes.append(i)
            if i < n ** 0.5:
                primestest.append(i)
        if int(100 * m / n) > int((100 * m - 1) / n):
            print(str(int(100 * m / n)) + "%, Time Remaining =",int(((time.process_time() - start)/(100 * m / n))*(100 - 100 * m / n)),"Seconds")
    return primes


def sumprimesbelow(n):
    total = sum(primesbelow(n))
    print(total)


sumprimesbelow(2000000)
