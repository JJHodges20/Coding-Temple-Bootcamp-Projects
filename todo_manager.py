# This project creates an editable to-do list.
# Users can view, add, and remove tasks.

# Initial List of Tasks

tasks = [ "Work on bootcamp", "Play video games", "Eat some food"]

# Display Current To-Do List

print("=" * 35)
print("      My To-Do List")
print("=" * 35)

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print(f"\nTotal Tasks: {len(tasks)}")

# Ask the User What They Want to Do

print("\nWhat would you like to do?")
print("1. Add a task")
print("2. Remove a task")

choice = input("\nEnter your choice (1 or 2): ")

# Add a New Task

if choice == "1":
    new_task = input("\nEnter new task: ")
    tasks.append(new_task)
    print(f'\n"{new_task}" has been added.')

# Remove a Task

elif choice == "2":

    print("\nCurrent Tasks:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

    try:
        task_number = int(input("\nEnter the task number to remove: "))

        # Convert from 1-based numbering to 0-based indexing
        removed_task = tasks.pop(task_number - 1)

        print(f'\n"{removed_task}" has been removed.')

    except (ValueError, IndexError):
        print("\nInvalid task number.")

# Invalid Menu Choice

else:
    print("\nInvalid choice. Please enter 1 or 2.")

# Display Updated To-Do List

print("\n" + "=" * 35)
print("      Updated To-Do List")
print("=" * 35)

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print(f"\nTotal Tasks: {len(tasks)}")