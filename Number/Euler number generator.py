# Coded by domo4862
# Calculates the euler number to the nth decimal place

from math import e
from decimal import *

def main():
    print("How many decimal places?")
    n = int(input())
    getcontext().prec = n

    factorial = 1  # factorial counter
    # equation = (1/n!) where n starts from 0
    # at n = 0 and 1, both give 1
    euler = 2

    # Check if within limit
    if 0 < n < 151:
        for i in range(2, n):
            factorial *= i
            print(factorial)
            euler += Decimal(1)/Decimal(factorial)
        print(euler)
    else:
        print("Error: Decimal limit is 150")

if __name__ == "__main__":
    main()
