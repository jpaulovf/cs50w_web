import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid input.")
    sys.exit(1)

# try to divide, except when an division by zero error happens
try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)

print(f"{x} / {y} = {result}")