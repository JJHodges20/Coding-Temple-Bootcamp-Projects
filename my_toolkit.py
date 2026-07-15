# This Project is for practice creating functions and testing them

# Calculate_Average Function

def calculate_average(numbers):
    """Returns the average of a list of numbers.
    Returns 0 if the list is empty.
    """

    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return average
    
# Find Max and Min Functions

def find_max_and_min(numbers):
    """Returns a tuple containing the largest and smallest values."""

    if len(numbers) == 0:
        return (None, None)

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:

        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return (max_value, min_value)

# Count Occurences Function

def count_occurrences(items, target):
    """Counts how many times the target number appears in a list."""

    count = 0

    for item in items:

        if item == target:
            count += 1

    return count

# Palidrome Function

def is_palindrome(text):
    """Returns True if the text is a palindrome."""

    cleaned_text = text.lower().replace(" ", "")

    return cleaned_text == cleaned_text[::-1]

# Create Report Function

def create_report(title, scores):
    """Creates and returns a report."""

    average = calculate_average(scores)
    highest, lowest = find_max_and_min(scores)

    report = (
        f"{title}\n"
        f"{'=' * len(title)}\n"
        f"Total Scores: {len(scores)}\n"
        f"Average Score: {average:.2f}\n"
        f"Highest Score: {highest}\n"
        f"Lowest Score: {lowest}"
    )

    return report

# Test

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))