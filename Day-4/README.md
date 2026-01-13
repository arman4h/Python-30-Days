# 📆 Day 4 — Task Tracker (Full CRUD CLI Application)

## 🎯 Project Objective

Build a **Task Tracker CLI application** that supports **full CRUD operations** (Create, Read, Update, Delete) with **file-based persistence**.

This project is designed to:

* Strengthen backend logic
* Practice real-world data manipulation
* Build stable, loop-driven CLI software
* Prepare for automation and Linux utilities

---

## 🧠 Skills Practiced

* Function-based program design
* File read/write (persistent storage)
* CRUD operations
* Input validation
* Loop-based menu systems
* Safe file rewriting logic

---

## 📌 Project Overview

The Task Tracker allows users to manage tasks from the terminal.

Users can:

* Add new tasks
* View all tasks
* Update existing tasks
* Delete tasks
* Exit safely

All tasks are stored in a file so data remains after program exit.

---

## 🧱 Data Model

Each task is represented as:

```python
{
  "id": 1,
  "title": "Finish Python project",
  "status": "Pending"
}
```

---

## 💾 File Storage Format

All tasks are stored in `tasks.txt` using the format:

```
id|title|status
```

### Example:

```
1|Finish Python project|Pending
2|Review code|Completed
```

---

## 📂 Project Structure

```
task_tracker/
│
├── task_tracker.py
├── tasks.txt
└── README.md
```

---

## 🧩 Core Features (CRUD)

### ➕ Add Task

* Auto-generate unique task ID
* Task title must not be empty
* Default status is `Pending`

---

### 📋 View Tasks

* Display all tasks
* Show ID, title, and status
* Handle empty task list safely

---

### ✏️ Update Task

* Update task title **or** status
* Validate task ID before updating
* Rewrite file safely after update

---

### ❌ Delete Task

* Delete task by ID
* Validate task existence
* Rewrite file after deletion

---

## 🧠 Menu System (Loop-Based)

```
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
```

* Menu runs inside a `while True` loop
* Program exits using `break`
* No recursion is allowed

---

## ⚠️ Validation Rules

* Task title cannot be empty
* Task ID must exist for update/delete
* Invalid input must not crash the program
* File content must remain consistent

---

## ❌ Restrictions (Important)

* ❌ No classes
* ❌ No external libraries
* ❌ No GUI
* ❌ No argparse
* ❌ No database

Pure Python logic only.

---

## ✅ Completion Checklist

Day 4 is considered complete when:

* [ ] All CRUD operations work correctly
* [ ] Invalid inputs are handled gracefully
* [ ] Menu uses loop (no recursive calls)
* [ ] File data remains correct after updates/deletes
* [ ] You can explain every function in your own words

---

## 🔮 Why This Project Matters

This project represents a **real backend-style system**.

Next Steps After Completing it:

* Automation scripts
* Linux utilities
* CLI tools with flags
* GUI logic integration

