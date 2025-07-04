import calendar
import datetime

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"Expense: {self.name} {self.category} {self.amount:.2f}"

def main():
    print("Program is running.")
    expense_file_path = "expense.csv"
    salary = take_salary_input()
    budget = salary

    while True:
        expense = calculate_expense()
        budget -= expense.amount
        print("Remaining budget:", budget)

        save_to_file(expense, expense_file_path)
        summarize_expenses(expense_file_path, budget)

        add_more = input("Do you want to add more expenses? (yes/no): ")
        if add_more.lower() != 'yes':
            break

def take_salary_input():
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary > 0:
                return salary
            else:
                print("Salary should be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_expense():
    print("Calculating expenses.")
    expense_name = input("Where did you spend the money? ")
    expense_amount = float(input("How much money did you spend there? "))
    print(f"Expense name: {expense_name}, Amount: {expense_amount}")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Miscellaneous",
    ]

    while True:
        print("Select the category of your expense.")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter the category number ({value_range}): ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            print(selected_category)

            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)

            return new_expense
        else:
            print("Invalid category")

def save_to_file(expense, expense_file_path):
    print(f"Saving the expense to file: {expense} at {expense_file_path}")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path, budget):
    print("Summary of user expenses:")
    expenses = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            print(f"{expense_name} {expense_amount} {expense_category}")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount     

    print("Your expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: {amount}")

    total_spent = sum([x.amount for x in expenses])    
    print(f"Total spent: {total_spent:.2f}")

    print(f"Remaining budget: {budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"Remaining days in the month: {remaining_days}")

    daily_budget = budget / remaining_days
    print("Daily budget:", daily_budget)

if __name__ == "__main__":
    main()
