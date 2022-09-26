"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

def median(x):
    x.sort()
    list_length = len(x)
    if list_length % 2 == 1:
        z = list_length // 2
        y = x[z]
    else:
        y = (x[list_length // 2] + x[list_length // 2 - 1]) / 2
        return y

print(median(numbers))