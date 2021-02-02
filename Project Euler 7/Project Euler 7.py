def numprime(a):
    m = 0
    for i in range(2,999999999):
        if all(i % j != 0 for j in range(2, i-1)):
            m += 1
            if m > a:
               break
            print("Prime =", str(i),", No.=", str(m))
    return m


numprime(100)