## we define a factorial function 

def factorial(n):
    total = 1
    for i in range(1,n):
        total *= i
    return total



#Now a simple function to sum the digits in an number.

def sumDigits(number):
    numberString = str(number)
    total = 0
    for i in range(0, len(numberString)):
        total += int(numberString[i])
    return total

print(sumDigits(factorial(10)))
