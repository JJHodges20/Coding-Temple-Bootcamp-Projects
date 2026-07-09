# This program is meant to collect numbers and make fallbacks to prevent errors and crashes.

# First Number
try:
    number1 = int(input("Enter the first number: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number1 = 0

# Second Number
try:
    number2 = int(input("Enter the second number: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number2 = 0

# Third Number
try:
    number3 = int(input("Enter the third number: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number3 = 0

# Calculate the sum and average
sum_numbers = number1 + number2 + number3
average = sum_numbers / 3

# Display the results
print(f"\nYour Numbers: {number1}, {number2}, {number3}")
print(f"Sum: {sum_numbers}")
print(f"Average: {average:.2f}")