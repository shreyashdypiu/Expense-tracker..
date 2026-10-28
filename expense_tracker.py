"""Expense Tracker - a simple command-line expense management tool.

Records are stored in a local JSON file (expenses.json).
Run with: python expense_tracker.py
"""

import json
import os
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file. Return an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read the data file. Starting fresh.")
        return []


def save_expenses(expenses):
    """Save the list of expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=2)


def get_text(prompt):
    """Ask until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_amount(prompt):
    """Ask until the user enters a positive number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return round(amount, 2)
            print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def add_expense(expenses):
    description = get_text("Description: ")
    category = get_text("Category: ").title()
    amount = get_amount("Amount: ")

    next_id = max((item["id"] for item in expenses), default=0) + 1
    expenses.append(
        {
            "id": next_id,
            "date": date.today().isoformat(),
            "description": description,
            "category": category,
            "amount": amount,
        }
    )
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"\n{'ID':<5}{'Date':<13}{'Category':<15}{'Description':<22}{'Amount':>10}")
    print("-" * 65)
    for item in expenses:
        print(
            f"{item['id']:<5}{item['date']:<13}{item['category']:<15}"
            f"{item['description'][:20]:<22}{item['amount']:>10.2f}"
        )
    print("-" * 65)
    total = sum(item["amount"] for item in expenses)
    print(f"{'Total':<55}{total:>10.2f}")


def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for item in expenses:
        totals[item["category"]] = totals.get(item["category"], 0) + item["amount"]

    print(f"\n{'Category':<20}{'Total':>12}")
    print("-" * 32)
    for category, amount in sorted(totals.items(), key=lambda pair: -pair[1]):
        print(f"{category:<20}{amount:>12.2f}")
    print("-" * 32)
    print(f"{'Overall':<20}{sum(totals.values()):>12.2f}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    try:
        target_id = int(input("Enter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in expenses:
        if item["id"] == target_id:
            expenses.remove(item)
            save_expenses(expenses)
            print("Expense deleted.")
            return
    print("No expense found with that ID.")


def main():
    expenses = load_expenses()

    actions = {
        "1": add_expense,
        "2": view_expenses,
        "3": view_summary,
        "4": delete_expense,
    }

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        if choice in actions:
            actions[choice](expenses)
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
