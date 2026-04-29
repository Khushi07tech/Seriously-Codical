# Problem: Print increasing and decreasing star patterns
# Pattern: Nested loops + conditional logic
# Complexity: O(n^2)

def validate_option(user_option):
    try:
        return int(user_option)
    except ValueError:
        print("Value Error:\nPlease enter a number")
        return None

def validate_rows(user_rows):
    try:
        return int(user_rows)
    except ValueError:
        print("Value Error\nPlease enter a number")
        return None

print("Star patterns\nEnter 1 for increasing pattern\nEnter 2 for decreasing pattern")

user_option = input("Select: ")
option = validate_option(user_option)

if option == 1 or option == 2:
    user_rows = input("Rows: ")
    rows = validate_rows(user_rows)

    for row in range(rows):
        if option == 1:
            stars = row + 1
        else:
            stars = rows - row

        for col in range(stars):
            print("*", end="")
        print()
else:
    print("Select between 1 and 2 only")