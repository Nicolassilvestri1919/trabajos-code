expenses = []

while True:
    print("1. Add expense")
    print("2. View expense list")
    print("3. Calculate total expenses")
    print("4. Exit")
    choice = input("Choice: ")

    if choice == "1":
        description = input("Description: ")
        amount = float(input("Amount: "))
        expense = {"description": description, "amount": amount}
        expenses.append(expense)
        print("Expense added successfully.")
    elif choice == "2":
        print("Expense list:")
        for expense in expenses:
            print(f"{expense['description']}: {expense['amount']}")
    elif choice == "3":
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total expenses: {total}")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Program terminated.")


