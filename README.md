# Expense Tracker

A command-line application for recording and reviewing personal expenses. Built with Python, with data stored locally in a JSON file.

## Features

- Add expenses with a description, category, and amount
- View all recorded expenses in a formatted table
- View total spending and a summary by category
- Delete expenses by ID
- Data is saved automatically and persists between sessions
- Input validation for amounts and menu choices
- No external libraries required

## Requirements

- Python 3.6 or higher

## Installation

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

## How to Run

```bash
python expense_tracker.py
```

On some systems, use `python3` instead.

## Example

```
===== Expense Tracker =====
1. Add expense
2. View all expenses
3. View summary by category
4. Delete expense
5. Exit

Enter choice (1-5): 1
Description: Lunch
Category: Food
Amount: 12.50
Expense added successfully.
```

## Project Structure

```
expense-tracker/
├── expense_tracker.py
├── requirements.txt
└── README.md
```

A file named `expenses.json` is created automatically on first use to store your data.

## Future Improvements

- Filter expenses by date range
- Export records to CSV
- Monthly budget limits and alerts

## License

This project is licensed under the MIT License.

## Author

**Your Name**
- GitHub: [shreyashdypiu](https://github.com/shreyashdypiu)
