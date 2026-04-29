# Problem: Check if a string is a palindrome
# Pattern: Two Pointers
# Approach: Compare characters from both ends and move inward
# Key Idea: Stop early if mismatch is found
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_palindrome(text, left, right):
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

user_text = input("Text: ").lower().strip()

left_pointer = 0
right_pointer = len(user_text) - 1


result = is_palindrome(user_text, left_pointer, right_pointer)

if result:
    print("Palindrome")
else:
    print("Not Palindrome")
