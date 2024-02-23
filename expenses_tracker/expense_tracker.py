import os
import datetime

DATA_FILE = "expenses.txt"

def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w"):
            pass

def add_expense(amount, category):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DATA_FILE, "a") as file:
        file.write(f"{amount},{category},{date}\n")

def view_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            expenses = file.readlines()
            for index, expense in enumerate(expenses, start=1):
                amount, category, date = expense.strip().split(',')
                print(f"Amount: {amount}, Category: {category}, Date: {date}")
    else:
        print("No expenses found.")

def view_report():
    if os.path.exists(DATA_FILE):
        category_expenses = {}
        with open(DATA_FILE, "r") as file:
            expenses = file.readlines()
            for expense in expenses:
                amount, category, _ = expense.strip().split(',')
                if category in category_expenses:
                    category_expenses[category] += float(amount)
                else:
                    category_expenses[category] = float(amount)

        print("Expense Report:")
        for category, total_amount in category_expenses.items():
            print(f"Category: {category}, Total Amount: {total_amount}")
    else:
        print("No expenses found.")

def expenses():
    initialize_data_file()
    
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Report")
    print("4. Exit")
        

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            add_expense(amount, category)
            print("Expense added successfully.")
        elif choice == '2':
            print("\nAll Expenses:")
            view_expenses()
        elif choice == '3':
            print("\nExpense Report:")
            view_report()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

expenses()