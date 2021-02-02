# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

total = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        total += i
print(total)
