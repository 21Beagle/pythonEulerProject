def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def smalldiv(n):
    numbers = []
    truers = []
    for i in range(1, n+1):
        numbers.append(i)
    print(numbers)
    for j in range(factorial(int(n/2)),factorial(n)):
        if all(j % number == 0 for number in numbers):
            truers.append(j)
            print(str(j) + ', ' + str(truers))
        else:
            print(str(j) + ', ' + str(truers))
        if truers:
            break




smalldiv(20)
