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

def get_median(x):
   x = sorted(x)
   size = len(x)
   if size % 2 == 0: # 判断列表长度为偶数
    median = (x[size//2]+x[size//2-1])/2
    x[0] = median
   if size % 2 == 1: # 判断列表长度为奇数
    median = x[(size-1)//2]
    x[0] = median
   return x[0]

print(get_median(numbers))