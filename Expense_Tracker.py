expenses = []

def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully.\n")


def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Date: {expense['date']}")
        print(f"   Category: {expense['category']}")
        print(f"   Amount: {expense['amount']}")
        print(f"   Description: {expense['description']}")
        print("---------------------------")


def category_total():
    category = input("Enter category: ")

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    print(f"Total expenses for {category}: {total}\n")


def delete_expense():
    view_expenses()

    try:
        num = int(input("Enter expense number to delete: "))

        if 1 <= num <= len(expenses):
            del expenses[num - 1]
            print("Expense deleted successfully.\n")
        else:
            print("Invalid expense number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Total")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            category_total()

        elif choice == '4':
            delete_expense()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


main()