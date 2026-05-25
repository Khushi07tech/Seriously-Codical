# Problem: Print numbers in countdown order using recursion
# Algorithm: Recursion
# Approach: Print current number and recursively call function with smaller value
# Key Idea: Solve one step, then delegate remaining work to a smaller function call
# Time Complexity: O(n)
# Space Complexity: O(n)

def countdown(number):
    if number== 0:
        return
    else:
        print(number)
        number-= 1
        countdown(number)

def main():
    number = 5
    countdown(number)

main()