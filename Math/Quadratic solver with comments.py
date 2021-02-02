# function quadratic finds the solution for the quadratic ax^2 + bx + c using a, b, c as arguments

def quadratic(a, b, c):
    solutions = []
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    if type(x1) != complex:
        solutions.append(x1)
        if x1 != x2:
            solutions.append(x2)
    return solutions


# Asks the user to input their values for a, b and c

print("Quadratic function solver! Enter your values for a, b and c")
print("where ax^2 + bx + c")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter b:"))

# Calls for the function quadratic

solutions1 = quadratic(a, b, c)

# Some grammar cases for when the number of solutions is 0, 1 or 2

if len(solutions1) == 2:
    print("There are %s real solutions to the function %sx^2 + %sx + %s" % (str(len(solutions)), str(a), str(b), str(c) + ":"))
    for each in solutions1:
        print("x =" + str(each))
elif len(solutions1) == 1:
    print("There is only %s real solution to the function %sx^2 + %sx + %s" % (str(len(solutions1)), str(a), str(b), str(c) + ":"))
    for each in solutions1:
        print("x =" + str(each))
elif len(solutions1) == 0:
    print("There are %s real solutions to the function %sx^2 + %sx + %s" % (str(len(solutions1)), str(a), str(b), str(c) + ":"))
