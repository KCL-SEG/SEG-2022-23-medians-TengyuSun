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
print(numbers)
def median(numbers):
numbers.sort()
list_length = len(numbers)
if list_length % 2 == 0:
return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
return list[int(list_length / 2)]
