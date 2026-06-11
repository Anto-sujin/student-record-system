# 🎓 Student Record Management System

A beginner-friendly Python project that demonstrates **file handling** through a fully functional command-line Student Record System — no database required!

---

## 📁 Project Structure

```
project/
├── student.py     # Main program
└── detail.txt     # Auto-generated data file (stores student records)
```

> `detail.txt` is created automatically when you add your first student.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add Student** | Save student name, age, and course to file |
| 2 | **View Students** | Display all stored student records |
| 3 | **Search Student** | Find a student record by name |
| 4 | **Delete Student** | Remove a student record permanently |
| 5 | **Update Student** | Edit an existing student's details |
| 6 | **Exit** | Close the program |

---

## 🚀 How to Run

**Requirements:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/Anto-sujin/student-record-system.git
# Navigate into the folder
cd student-record-system

# Run the program
python student.py
```

---

## 🖥️ Sample Output

```
===== Student Record System =====
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Exit

Enter your choice: 1
Name   : Alice
Age    : 20
Course : Computer Science
Student added successfully.
```

---

## 📂 How Data is Stored

Records are stored in plain text format inside `detail.txt`:

```
Alice,20,Computer Science
Bob,22,Information Technology
Charlie,21,Data Science
```

Each line = one student record, with fields separated by commas.

---

## 💡 What I Learned

- Reading and writing files using `open()` in Python
- Using file modes: `"a"` (append), `"r"` (read), `"w"` (write)
- Parsing structured data from plain text
- Handling exceptions like `FileNotFoundError` and `ValueError`
- Building a full CRUD application without a database

---

## 🛠️ Built With

- Python 3
- Built-in `open()` file I/O — no external libraries needed

---

## 📌 Future Improvements

- [ ] Add student ID for unique identification
- [ ] Export records to CSV
- [ ] Add input validation (e.g., age must be a number)
- [ ] Sort students by name or course

---

## 👤 Author

**Your Name**
- GitHub: [@Anto-sujin](https://github.com/Anto-sujin/student-record-system.git)

---

⭐ If you found this helpful, consider giving it a star!
