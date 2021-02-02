def collatz_seq(n):
    list = []
    i = n
    while i != 1:
        if (i / 2).is_integer() == True:
            i = (i / 2)
            list.append(int(i))
        else:
            i = (3 * i) + 1
            list.append(int(i))
        if i == 1:
            break
    return len(list)


collatznum = []

for i in range(1, 1000000):
    collatznum.append(collatz_seq(i))
    print(i)


print(collatznum)

print(collatznum.index(max(collatznum))+1)
