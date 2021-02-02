def fizzbuzz(n, a, b):
    for i in range(1,n):
        output = ""
        if i % a == 0:
            output += "Fizz"
        if i % b == 0:
            output += "Buzz"
        if output == "":
            print(i)
        else:
            print(output)

fizzbuzz(100,4,7)