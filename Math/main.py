import cmath

def quadratic(a,b,c):
    solutions = []
    x1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
    if type(x1) != complex:
        solutions.append(x1)
        if x1 != x2:
            solutions.append(x2)
    return solutions


print(((25-18.5)/2)+18.5)
print("Quadratic function solver! Enter your values for a, b and c")
print("where ax^2 + bx + c")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

solutions = quadratic(a,b,c)

if len(solutions) == 2:
    print("There are %s real solutions to the function %sx^2 + %sx + %s"% (str(len(solutions)), str(a), str(b), str(c)+":"))
    for each in solutions:
        print("x =" + str(each))
elif len(solutions) == 1:
    print("There is only %s real solution to the function %sx^2 + %sx + %s" % (str(len(solutions)), str(a), str(b), str(c) + ":"))
    for each in solutions:
        print("x =" + str(each))
elif len(solutions) == 0:
    print("There are %s real solutions to the function %sx^2 + %sx + %s" % (str(len(solutions)), str(a), str(b), str(c) + ":"))

