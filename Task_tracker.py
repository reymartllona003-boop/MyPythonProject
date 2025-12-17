# ==========================
# Task Tracker CLI Program
# Created by: Reymart G. Llona
# Description: A simple command-line app to add, view, complete, and delete tasks.
# Tasks are stored locally in a JSON file for persistence.
# ==========================

import json       # Used to save and load data from the JSON file
import os         # Used to check if the task file exists
from datetime import datetime   # Used to store the date and time a task was created
from colorama import Fore, Style, init   # Used to colorize the terminal output

# Initialize colorama (for Windows compatibility)
init(autoreset=True)

# File where tasks will be saved
TASK_FILE = "tasks.json"

# ==========================
# Function: load_tasks()
# Loads existing tasks from the JSON file.
# If the file doesn’t exist, it returns an empty list.
# ==========================
def load_tasks():
    if not os.path.exists(TASK_FILE):   # Check if file exists
        return []                       # If not, return an empty list
    with open(TASK_FILE, "r") as f:     # Open the JSON file in read mode
        return json.load(f)             # Load and return the data (list of tasks)

# ==========================
# Function: save_tasks(tasks)
# Saves the updated list of tasks into the JSON file.
# ==========================
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:     # Open file in write mode
        json.dump(tasks, f, indent=4)   # Write tasks in formatted JSON

# ==========================
# Function: add_task(description)
# Adds a new task to the list and saves it.
# ==========================
def add_task(description):
    tasks = load_tasks()   # Load existing tasks
    task = {
        "description": description,    # Task name
        "completed": False,            # Default status (not yet done)
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp
    }
    tasks.append(task)     # Add the new task to the list
    save_tasks(tasks)      # Save updated list
    print(Fore.GREEN + "✅ Task added successfully!")  # Display success message

# ==========================
# Function: list_tasks()
# Displays all tasks with their index, description, and status.
# ==========================
def list_tasks(show_completed=None):
    tasks = load_tasks()     # Load all tasks
    if not tasks:            # If the list is empty
        print(Fore.YELLOW + "No tasks found.")  # Inform user
        return

    # Enumerate over all tasks and display them with a number
    for i, task in enumerate(tasks, start=1):
        # Status color: green if completed, red if pending
        status = Fore.GREEN + "[✔]" if task["completed"] else Fore.RED + "[ ]"
        print(f"{i}. {status} {task['description']} ({task['created_at']})")

# ==========================
# Function: complete_task(index)
# Marks a specific task as completed.
# ==========================
def complete_task(index):
    tasks = load_tasks()  # Load current tasks
    try:
        tasks[index - 1]["completed"] = True  # Mark selected task as complete
        save_tasks(tasks)                     # Save changes
        print(Fore.CYAN + "🎯 Task marked as completed!")
    except IndexError:
        print(Fore.RED + "❌ Invalid task number!")  # If number doesn’t exist

# ==========================
# Function: delete_task(index)
# Removes a task from the list.
# ==========================
def delete_task(index):
    tasks = load_tasks()  # Load tasks
    try:
        removed = tasks.pop(index - 1)        # Remove the chosen task
        save_tasks(tasks)                     # Save updated list
        print(Fore.MAGENTA + f"🗑️  Deleted: {removed['description']}")  # Show removed task
    except IndexError:
        print(Fore.RED + "❌ Invalid task number!")  # Invalid number

# ==========================
# Function: main()
# Main menu that runs in a loop until the user exits.
# ==========================
def main():
    while True:
        # Print main menu
        print(Style.BRIGHT + "\n=== TASK TRACKER CLI ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        # Get user choice
        choice = input("Choose an option: ")

        # Handle each option
        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            idx = int(input("Enter task number to mark completed: "))
            complete_task(idx)
        elif choice == "4":
            list_tasks()
            idx = int(input("Enter task number to delete: "))
            delete_task(idx)
        elif choice == "5":
            print(Fore.CYAN + "👋 Goodbye!")   # Exit message
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")  # Error handling

# ==========================
# Program Entry Point
# ==========================
if __name__ == "__main__":
    main()   # Run the program
