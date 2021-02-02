def pytrip(n):
    list = []
    for i in range(1, n):
        for j in range(i , n):
            ksquared = i*i + j*j
            k = ksquared**0.5
            if k.is_integer() == True:
                print("Where we are:", i, j, k)
                if i + j + k == n:
                    list.append(i)
                    list.append(j)
                    list.append(k)
                    list.append(i*j*k)
                    print("We found one!", i, j, k, i * j * k)
            if list:
                break


pytrip(1000)