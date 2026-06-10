# Problem: Reverse a string using recursion
# Algorithm: Recursion
# Approach: Reverse the remaining string first, then append the current character
# Key Idea: Break the string into first character + remaining substring
# Time Complexity: O(n²) due to string slicing and concatenation
# Space Complexity: O(n) due to recursive call stack


def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:]) + text[:1]


def main():
    text = "hello"
    print(reverse(text))

main()