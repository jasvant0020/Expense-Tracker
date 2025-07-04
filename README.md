# 💸 Python Expense Tracker

Track your monthly expenses and manage your budget wisely with this simple and interactive terminal-based Python application.

---

## 📌 Features

- 🧾 **Add Expenses**: Enter where you spent, how much, and categorize it.
- 💰 **Track Budget**: Deducts expense from salary and updates remaining budget.
- 📂 **CSV Logging**: Saves all expenses in `expense.csv` file.
- 📊 **Summary View**: Displays total spent and a breakdown by category.
- 📆 **Smart Suggestions**: Shows remaining days of the month and daily budget left.

---

## 🖥️ Demo

```bash
Program is running.
Enter your monthly salary: 30000
Where did you spend the money? Grocery Store
How much money did you spend there? 1500
Select the category of your expense:
1. Food
2. Home
3. Work
4. Fun
5. Miscellaneous
Enter the category number [1-5]: 1

Remaining budget: 28500.0

Summary of user expenses:
Grocery Store 1500.0 Food
Your expenses by category:
Food: 1500.0
Total spent: 1500.00
Remaining budget: 28500.00
Remaining days in the month: 26
Daily budget: 1096.15


Do you want to add more expenses? (yes/no):
```
---
## 📁 File Structure

- Copy code
   -- expense_tracker/
      ├── expense.csv             
      └── tracker.py
---
## 🚀 How to Run

- Clone the repository

   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
- Run the application
   python tracker.py
- 💡 Make sure you have Python 3 installed.
---
## 📦 Requirements

- Python 3.x
- No external libraries required (uses datetime, calendar — both standard)
---
## 🧠 Categories Supported

- 🍔 Food
- 🏠 Home
- 💼 Work
- 🎉 Fun
- ❓ Miscellaneous
---
## ✨ Highlights

- Clean and beginner-friendly code 🧼
- Easy to extend (e.g., add graphs, monthly reports, GUI) 🧩
- Teaches file handling, classes, user input, and data summarization 👨‍💻
---
## 📈 Future Improvements

- 📊 Add chart visualization using matplotlib
- 🌐 Build a web dashboard
- 💾 Add monthly reset & historical tracking
---
## 🙌 Contributing
- Contributions are welcome!
- Feel free to fork the repo and submit a pull request.
---
## 📜 License

- This project is licensed under the MIT License.
---
## 💬 Author
- Made with ❤️ by [Your Name]
- 🔗 GitHub | 📧 your.email@example.com



