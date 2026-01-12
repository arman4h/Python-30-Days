# 📒 Contact Book (Python – File Based)

## 📌 Project Overview

This is a **command-line Contact Book application** built using Python.
The project allows users to **add, view, and search contacts**, and stores all contact data in a **text file** so that data is not lost after the program exits.

This project focuses on:

* Functions
* Lists & dictionaries
* Basic file handling
* Clean program structure

---

## 🎯 Features

* Add a new contact
* View all saved contacts
* Search contact by name
* Store contacts permanently using a file
* Simple menu-driven interface

---

## 🧱 Data Structure

Each contact is stored as:

```python
{
    "name": "John Doe",
    "phone": "017XXXXXXXX",
    "email": "john@email.com"
}
```

All contacts are saved in a text file:

```
contacts.txt
```

Each contact is stored in one line using a simple format:

```
name,phone,email
```

---

## 📂 File Structure

```
contact_book/
│
├── contact_book.py
├── contacts.txt
└── README.md
```

---

## 🧠 Program Flow

```
Start Program
   ↓
Load contacts from file
   ↓
Show menu
   ↓
User selects option
   ↓
Call corresponding function
   ↓
Save changes to file (if any)
   ↓
Exit safely
```

---

## 🧩 Functions to Implement

### `load_contacts()`

* Reads data from `contacts.txt`
* Converts file data into list of dictionaries

---

### `save_contacts(contacts)`

* Writes all contacts back to `contacts.txt`
* Overwrites old data safely

---

### `add_contact(contacts)`

* Takes user input
* Adds new contact to list
* Saves updated list to file

---

### `view_contacts(contacts)`

* Displays all contacts neatly
* Handles empty contact list

---

### `search_contact(contacts)`

* Searches contact by name
* Case-insensitive search

---

### `show_menu()`

Displays:

```
1. Add Contact
2. View Contacts
3. Search Contact
4. Exit
```

---

## 🚫 Limitations (for now)

* No duplicate checking
* No delete or update feature
* No file encryption

*(These can be added later)*

---

## 🚀 Learning Outcomes

By completing this project, you will understand:

* How functions work together
* How to store structured data using files
* How to convert file data ↔ Python data
* How to build small real-world CLI programs

---

## 🔮 Future Improvements

* Delete contact
* Update contact
* Phone number validation
* Export contacts as CSV
* Password protection

---
