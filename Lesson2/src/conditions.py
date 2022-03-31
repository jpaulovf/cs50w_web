#n = input("number: ")  'n' is a string, not a number
n = int(input("number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")