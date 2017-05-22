# Coded by domo4862
# 3 Different formula that calculates the value of Pi to the nth decimal places
# Chudnovsky Algorithm is considered to the be the fastest

from decimal import *

def main():
    print("Which Formula?")
    print("1. Bailey-Borwein-Plouffe")
    print("2. Bellard")
    print("3. Chudnovsky")
    x = input()

    # Input for decimal places
    print("How many decimal places?")
    n = int(input())
    if n > 200:
        print("Error: Decimal limit is 200")
        exit()

    # Set Precision to input for number of decimals
    getcontext().prec = n
    if x == '1':
        bbp(n)
    elif x == '2':
        bellard(n)
    elif x == '3':
        chud(n)

# Bailey-Borwein-Plouffe Formula
def bbp(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    print("(Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))")
    print(pi)

# Bellard's Formula
def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k/(1024**k)) * (Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5)\
         - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))
        k += 1
    pi = pi * 1/(2**6)
    print("[(Decimal(-1)**k/(1024**k)) * (Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5)\
     - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))] * 1/(2**6)")
    print(pi)

# Chudnovsky Algorithm
def chud(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    print("{[(Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k))) * (13591409+545140134*k)/(640320**(3*k)))] * Decimal(10005).sqrt()/4270934400}**(-1)")
    print(pi)

# Recursion for factorisation (e.g 3! = 3! * (3 -1)! * (3 - 2)! * (3 - 3)!)
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    main()
