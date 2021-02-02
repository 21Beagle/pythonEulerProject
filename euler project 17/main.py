def chartostring(n):
    string = str(n)
    output = ""
    if len(string) == 3:
        string = "0" + string
    if len(string) == 2:
        string = "00" + string
    if len(string) == 1:
        string = "000" + string
    if string[1] == "1":
        output += "onehundred"
    if string[1] == "2":
        output += "twohundred"
    if string[1] == "3":
        output += "threehundred"
    if string[1] == "4":
        output += "fourhundred"
    if string[1] == "5":
        output += "fivehundred"
    if string[1] == "6":
        output += "sixhundred"
    if string[1] == "7":
        output += "sevenhundred"
    if string[1] == "8":
        output += "eighthundred"
    if string[1] == "9":
        output += "ninehundred"
    if string[1] != "0" and (string[2] != "0" or string[3] != "0"):
        output += "and"
    if string[2] == "1" and string[3] == "0":
        output += "ten"
    if string[2] == "2":
        output += "twenty"
    if string[2] == "3":
        output += "thirty"
    if string[2] == "4":
        output += "forty"
    if string[2] == "5":
        output += "fifty"
    if string[2] == "6":
        output += "sixty"
    if string[2] == "7":
        output += "seventy"
    if string[2] == "8":
        output += "eighty"
    if string[2] == "9":
        output += "ninety"
    if string[2] != "1" and string[3] == "1":
        output += "one"
    if string[2] != "1" and string[3] == "2":
        output += "two"
    if string[2] != "1" and string[3] == "3":
        output += "three"
    if string[2] != "1" and string[3] == "4":
        output += "four"
    if string[2] != "1" and string[3] == "5":
        output += "five"
    if string[2] != "1" and string[3] == "6":
        output += "six"
    if string[2] != "1" and string[3] == "7":
        output += "seven"
    if string[2] != "1" and string[3] == "8":
        output += "eight"
    if string[2] != "1" and string[3] == "9":
        output += "nine"
    if string[2] == "1" and string[3] == "1":
        output += "eleven"
    if string[2] == "1" and string[3] == "2":
        output += "twelve"
    if string[2] == "1" and string[3] == "3":
        output += "thirteen"
    if string[2] == "1" and string[3] == "4":
        output += "fourteen"
    if string[2] == "1" and string[3] == "5":
        output += "fifteen"
    if string[2] == "1" and string[3] == "6":
        output += "sixteen"
    if string[2] == "1" and string[3] == "7":
        output += "seventeen"
    if string[2] == "1" and string[3] == "8":
        output += "eighteen"
    if string[2] == "1" and string[3] == "9":
        output += "nineteen"
    if string == "1000":
        output += "onethousand"
    return output


def nochar(n):
    x = len(chartostring(n))
    return x

x = 0
stringer = ""
for i in range(1, 1001):
    print(chartostring(i))
    stringer += chartostring(i)

print(stringer)
print(len(stringer))

