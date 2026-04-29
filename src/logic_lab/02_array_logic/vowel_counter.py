# Problem: Count vowels in a string
# Pattern: Loop + conditional filtering
# Concept: Basic string traversal and counting
# Time Complexity: O(n)

text = input("Text: ").lower()
vowels = ["a", "e", "i", "o", "u"]
count = 0

for letter in text:
    if letter in vowels:
        count += 1

print(f"Vowels: {count}")