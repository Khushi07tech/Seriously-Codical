# Problem: Reverse a string without using built-in slicing or reverse functions
# Approach: Use manual index traversal starting from the last character
# Technique: Pointer-based iteration (while loop)
# Key Idea: Build the reversed string step-by-step by moving backwards
# Time Complexity: O(n)
# Space Complexity: O(n)

text = input("Original Text: ").lower()
position = len(text) - 1
reverse = []

while position >= 0:
    reverse.append(text[position])
    position -= 1

print(f"Reversed Text:", "".join(reverse))