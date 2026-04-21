import sys
import math

try:
    num = int(input("Number: "))
except ValueError:
    print("Invalid Value. Please enter a number")
    sys.exit()

#Checking divisibility by 2 to n-1
def is_prime(num):
    if num == 1:
        return "Not a Prime number"
    if num == 2:
        return "Prime number"

    limit = int(math.sqrt(num))

    for n in range (2, limit + 1):
        if (num % n) == 0:
            return "Not a Prime number"
    return "Prime number"

print(is_prime(num))

