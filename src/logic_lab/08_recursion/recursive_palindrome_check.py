# Problem: Check whether a given string is a palindrome using recursion
# Algorithm: Recursion (Divide and Conquer)
# Approach: Compare first and last characters; if they match, recursively check the middle substring
# Key Idea: A string is a palindrome if its outer characters match and the inner substring is also a palindrome
# Base Case: Strings with length 0 or 1 are always palindromes
# Time Complexity: O(n)  (each call reduces string size by 2)
# Space Complexity: O(n)  (recursive call stack)


def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


def main():
    text = "acca"
    print(is_palindrome(text))


main()