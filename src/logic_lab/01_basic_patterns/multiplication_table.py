# Problem: Print multiplication table of a number
# Pattern: Loop (iteration)
# Time Complexity: O(n)

def validate_num(user_num):
    try:
        return int(user_num)
    except ValueError:
        print("Value Error:\nPlease enter a number")
        return None

user_num = input("Number: ")
num = validate_num(user_num)

if num is not None:
    for n in range(1, 11):
        print(f"{num} X {n} = {num * n}")
