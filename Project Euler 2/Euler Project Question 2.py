def fib(n) -> object:
    a = 0
    b = 1
    total = 0
    for i in range(n):
        while a < n:
            print("a = " + str(a) + " b = " + str(b))
            z = a + b
            t = a
            if t % 2 == 0:
                total += t
                print("total = " + str(total))
            a = b
            b = z


fib(4000000)
