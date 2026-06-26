# 💰 Expense Tracker (Python)

A simple command-line **Expense Tracker** built with Python that helps you record, organize, and manage your daily expenses. All expense data is stored in a JSON file, making it lightweight and easy to use.

## ✨ Features

* ➕ Add new expenses
* 📖 View all saved expenses
* 🔍 Search expenses by category
* 💰 View total amount spent
* 📅 Monthly expense summary
* 🗑️ Delete expenses using their ID
* 💾 Automatically saves data to a JSON file

---

## 📂 Project Structure

```
Expense-Tracker/
│
├── data/
│   └── data.json
│
├── main.py
├── tracker.py
└── README.md
```

---

## 🛠️ Built With

* Python 3
* JSON
* pathlib
* datetime
* random

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mayurcodingx/expence-tracker.git
```

> If your repository name actually contains a space (`expence tracker`), use:
>
> ```bash
> git clone "https://github.com/mayurcodingx/expence tracker.git"
> ```
>


### 2. Go to the project folder

```bash
cd expence-tracker
```

### 3. Run the application

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## 📸 Application Menu

```
1. Add Expense
2. View Expenses
3. Search by Category
4. Show Total Spent
5. Monthly Summary
6. Delete Expense
7. Save & Exit
```

---

## 💾 Data Storage

All expenses are stored inside:

```
data/data.json
```

Example:

```json
[
    {
        "id": 101,
        "category": "food",
        "amount": 250,
        "description": "Burger",
        "take_date": "25/06/2026",
        "month": "jun"
    }
]
```

---

## 🎯 Future Improvements

* Budget limits
* Expense charts
* CSV export
* Multiple user accounts
* Better validation
* Colored terminal output
* Statistics dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📜 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Mayur**

GitHub: https://github.com/mayurcodingx

If you found this project useful, consider giving it a ⭐ on GitHub!
