def number_sum(n):
    x = 0
    string = str(n)
    for i in range(0,len(string)):
        x += int(string[i])
    print(x)
    return x

number_sum(2 ** 1000)

