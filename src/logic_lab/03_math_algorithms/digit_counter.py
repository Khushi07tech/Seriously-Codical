#Problem: Count digits in a number without using len()
#Pattern: digit manipulation using division
#Time Complexity: O(d) = O(log10 n)

def validate_num(user_num):
    try:
        return int(user_num)
    except ValueError:
        print("Value Error:\nPlease enter numbers")
        return None

user_num = input("Number: ")
num = validate_num(user_num)
count = 0

if num is not None:
    num = abs(num)
    if num == 0:
        count += 1
    else:
        while num > 0:
            num = num // 10
            count += 1

    print(f"Digits: {count}")