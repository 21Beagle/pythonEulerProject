import time
import math


def primesbelow(n, primesin):
    primes = primesin
    if primesin == []:
        primes = [2]
    start = time.process_time()
    primestest = [2]
    m = 0
    for i in range(max(primes), int(n)):
        m += 1
        if primestest[len(primestest)-1] <= i**0.5:
            primestest.append(primes[len(primestest)])
        if all(i % prime != 0 for prime in primestest):
            primes.append(i)
        if int(100 * m / n) > int((100 * m - 1) / n):
            print(str(int(100 * m / n)) + "%, Time Remaining =",int(((time.process_time() - start)/(100 * m / n))*(100 - 100 * m / n)),"Seconds")
    print(primes)
    return primes


def triangle(n):
    x = 0
    for i in range(0,n+1):
        x += i
    return x



def nodiv(n):
    primes = [2]
    primestest = [2]
    m = 0
    for i in range(max(primes), int(n**0.5)):
        m += 1
        if primestest[len(primestest)-1] <= i**0.5:
            primestest.append(primes[len(primestest)])
        if all(i % prime != 0 for prime in primestest):
            primes.append(i)
        else:
            l = [1]
            for j in primes:
                if n % j == 0:
                    l.append(j)
                    for k in range(1, int(math.log(n,j))+1):
                        if n % (j ** k) == 0 and (j ** k) not in l:
                            l.append(j**k)
    for divisor1 in range(0,len(l)):
        for divisor2 in range(divisor1, len(l)):
            if l[divisor1] * l[divisor2] <= int(n/2) and l[divisor1] * l[divisor2] not in l and n % (l[divisor1] * l[divisor2]) == 0:
                l.append(l[divisor1] * l[divisor2])
                print(l[divisor1] * l[divisor2])
    if n not in l:
        l.append(n)
    l.sort()
    print(n, len(l), l)
    return len(l)


nodiv(100)



def triangle(n):
    x = 1
    while nodiv(x) < n:
        print(x)
        if nodiv(x) > n:
            print("we found one" + str(x))
            break
    x += x
    return x

triangle(2)