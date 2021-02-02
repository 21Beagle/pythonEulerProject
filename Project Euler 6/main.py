def squaresum(n):
    sqs = 0
    for i in range(0,n+1):
        sqs += i*i
    return sqs


def sumsquare(n):
    sqs = 0
    for i in range(0,n+1):
        sqs += i
        total = sqs*sqs
    return total


def diff(n):
    dif = sumsquare(n)-squaresum(n)
    print(dif)
    return diff


diff(100)