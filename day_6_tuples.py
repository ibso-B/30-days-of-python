
# 1. Creating Tuples
print("--- 1. Creating Tuples ---")
coordinates = (10.0, 20.5)
person = ("Alice", 30, "Developer")

# Important: A single-element tuple requires a trailing comma!
# Without the comma, Python treats it just as a regular grouped expression.
single_item = (42,) 

print("Coordinates:", coordinates)
print("Person record:", person)
print("Single item tuple:", single_item)


# 2. Accessing Elements (Indexing & Slicing)
print("\n--- 2. Accessing Elements ---")
print("First item in person:", person[0])     # Output: Alice
print("Last item in person:", person[-1])     # Output: Developer

# Slicing works just like lists
numbers = (10, 20, 30, 40, 50, 60)
print("Slice (index 1 to 4):", numbers[1:4])  # Output: (20, 30, 40)


# 3. Immutability (Read-Only Safety)
print("\n--- 3. Immutability ---")
# The following line would raise a TypeError if you ran it:
# coordinates[0] = 15.0  
print("Tuples cannot be modified after creation.")
print("This makes them great for protecting fixed data or configuration constants.")


# 4. Tuple Unpacking
print("\n--- 4. Tuple Unpacking ---")
x, y = coordinates
print(f"Unpacked -> X: {x}, Y: {y}")

# You can also use an asterisk (*) to capture multiple remaining items
scores = (88, 92, 79, 95, 100)
first, *middle, last = scores
print(f"First score: {first}")
print(f"Middle scores: {middle}")
print(f"Last score: {last}")


# 5. Built-in Tuple Methods
print("\n--- 5. Tuple Methods ---")
colors = ("red", "blue", "green", "blue", "yellow", "blue")

# .count() tells you how many times a value appears
print("How many times does 'blue' appear?", colors.count("blue"))

# .index() finds the index of the first occurrence of a value
print("Index of the first 'green':", colors.index("green"))

