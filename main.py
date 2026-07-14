def main():
    print("Welcome to the Task Tracker CLI!")
    print("This is a simple command-line interface for tracking tasks.")
    print("You can add, view, and delete tasks using this tool.")

    while True:
        print("\n----------------------------------------------\n")
        print("Please choose an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        print("\n----------------------------------------------\n")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("Thank you for using the Task Tracker CLI!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()