# 📒 Contact Directory (Python – File Based)

## 📌 Project Overview

This is a **menu-driven Contact Directory application** built using Python.
The program allows users to **add, view, and search contacts**, with all data stored permanently in a text file.

This project focuses on:

* Functions and program structure
* Dictionaries, strings, and file handling
* Menu-driven CLI applications
* Real-world beginner software logic

---

## 🎯 Features

* ➕ Add new contacts
* 📋 View all saved contacts
* 🔍 Search contacts by **name or email**
* 💾 Persistent storage using file write/read
* Simple footer-based navigation system

---

## 📂 File Structure

```
contact_directory/
│
├── contact_directory.py
├── Contacts.txt
└── README.md
```

---

## 🧱 Data Storage Format

All contacts are stored in **Contacts.txt**
Each contact is saved in **one line** using comma-separated values:

```
Name,Email,Phone
```

### Example:

```
John Doe,john@email.com,017XXXXXXXX
Arman Hossain,arman@gmail.com,018XXXXXXXX
```

---

## 🧠 Program Flow

```
Start Program
   ↓
Show Main Menu
   ↓
User Selects Option
   ↓
Call Related Function
   ↓
Read / Write File
   ↓
Show Footer Menu
   ↓
Return to Main or Exit
```

---

## 🧩 Functions Overview

### `main()`

* Displays the main menu
* Routes user input to correct function

Menu Options:

```
1. Add Contacts
2. View All Contacts
3. Search Contacts
4. Exit
```

---

### `add_contacts()`

* Takes user input (name, email, phone)
* Stores contact data as a dictionary
* Writes contact to `Contacts.txt` in append mode

---

### `view_contacts()`

* Reads all contacts from file
* Displays stored data line by line
* Handles end-of-file safely

---

### `search_contact(key)`

* Searches contacts by **name or email**
* Case-insensitive matching
* Displays contact details if found
* Shows message if no match exists

---

### `footer()`

Displays navigation options after each operation:

```
0. Main Menu
1. Exit
```

Controls program flow without restarting the program.

---

## 🚫 Current Limitations

* No duplicate contact validation
* No update or delete functionality
* No formatted table output
* No error handling for corrupted file data

*(These will be added in later days)*

---

## 🚀 Learning Outcomes

By completing this project, you learned:

* How to design function-based programs
* How to store structured data using files
* How to search and parse file-based records
* How to build a reusable CLI menu system
* How to debug logical conditions in real programs

---

## 🔮 Possible Improvements (Future Work)

* Delete contact
* Update contact
* Prevent duplicate email or phone numbers
* Format output in table style
* Convert storage to CSV or JSON
* Replace recursive menus with loops

---

## ✅ Status

**Day 3 – Completed ✔**

---

### 🎉 Final Note

This project represents a **strong beginner milestone**.
You are now ready to move into **Day 4: Validation, Delete & Update Logic**.
