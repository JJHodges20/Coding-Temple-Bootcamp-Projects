# This project is to create a grade analyzer to process student data

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# Calculate Basic Score Information

total_scores = len(scores)
average_score = sum(scores) / total_scores
highest_score = max(scores)
lowest_score = min(scores)

# Assigning/Counting Passing and Failing Grades

passing_scores = 0
failing_scores = 0

for score in scores:
    if score >= 60:
        passing_scores += 1
    else:
        failing_scores += 1

# Assigning Grade Distribution

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_f = 0

for score in scores:

    if score >= 90:
        grade_a += 1

    elif score >= 80:
        grade_b += 1

    elif score >= 70:
        grade_c += 1

    elif score >= 60:
        grade_d += 1

    else:
        grade_f += 1


# Display Score Results

print("=== Grade Analyzer ===")

print(f"Total Scores: {total_scores}")
print(f"Average Score: {average_score:.1f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passing Scores (60+): {passing_scores}")
print(f"Failing Scores (Below 60): {failing_scores}")

print("\nGrade Distribution")
print("-" * 20)

print(f"A (90-100): {grade_a}")
print(f"B (80-89):  {grade_b}")
print(f"C (70-79):  {grade_c}")
print(f"D (60-69):  {grade_d}")
print(f"F (<60):    {grade_f}")

# Add Additional Scores

print("\nAdd Additional Scores")
print("Type 'done' when you are finished entering scores.")

while True:

    new_score = input("Enter a score (or 'done' to finish): ")

    if new_score.lower() == "done":
        break

    try:
        new_score = int(new_score)

        if 0 <= new_score <= 100:

            scores.append(new_score)

            average_score = sum(scores) / len(scores)

            print(f"Score added successfully!")
            print(f"Updated Average: {average_score:.2f}")

        else:
            print("Please enter a score between 0 and 100.")

    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Display Final Results

print("\nFinal Number of Scores:", len(scores))
print(f"Final Average Score: {sum(scores) / len(scores):.2f}")