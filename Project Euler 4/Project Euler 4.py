# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

s = 123456
str(s)

print(str(s)[1])

def checkpal(n):
    if str(n)[0] == str(n)[len(str(n))-1] and str(n)[1] == str(n)[len(str(n))-2] and str(n)[2] == str(n)[len(str(n))-3]:
        return True
    else:
        return False

def palfinder(m):
    numbers = []
    for i in range(100, 999):
        for j in range(i,999):
            if checkpal(i*j) == True:
                numbers.append(i*j)
                print(max(numbers), ' ', str(i), ' ', str(j))

palfinder(999999)
