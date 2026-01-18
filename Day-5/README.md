# 📅 Day 5 Project Design

## 🧠 Project: File Organizer Automation Tool

### 🎯 What this project teaches

* OS & filesystem control
* Automation thinking
* Safe file operations
* Real-world utility script
* Foundation for Linux tools & background scripts

---

## 🏗️ Project Concept (Simple & Powerful)

A **CLI automation tool** that:

* Scans a directory
* Organizes files by extension
* Creates folders automatically
* Moves files safely
* Logs all actions

This is a **real tool people actually use**.

---

## 📂 Project Structure (Day 5)

```
Day-05-File-Organizer/
│
├── organizer.py        # Main automation script
├── config.py           # User configuration (paths, rules)
├── logger.py           # Action logging logic
├── utils.py            # Helper functions
├── logs/
│   └── activity.log    # Log file
│
├── test_files/         # Dummy files for testing
│   ├── photo.jpg
│   ├── resume.pdf
│   ├── song.mp3
│   └── code.py
│
└── README.md           # Documentation
```

---

## 🧩 File Responsibilities (VERY IMPORTANT)

### 🔹 `organizer.py` (MAIN)

Handles:

* User input
* Directory scan
* Calls helper functions
* High-level control flow

Think: **brain of the program**

---

### 🔹 `config.py`

Stores:

* Base directory path
* Extension → folder mapping
* Ignored files

Example responsibility:

```python
EXTENSION_MAP = {
    "jpg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "mp3": "Music",
    "py": "Code"
}
```

---

### 🔹 `utils.py`

Helper functions:

* Create folder if not exists
* Get file extension
* Move files safely
* Check duplicates

No printing. No menus. Just logic.

---

### 🔹 `logger.py`

Handles:

* Writing logs
* Timestamping
* Error logging

Example log:

```
2026-01-18 10:30 | MOVED | resume.pdf → Documents/
```

---

### 🔹 `logs/activity.log`

* Created automatically
* Appends logs
* No overwrite

---

### 🔹 `test_files/`

* Fake files to test safely
* Prevents damaging real folders

---

## 🔄 Core Workflow (MENTAL MODEL)

```
START
 ↓
Scan directory
 ↓
For each file:
    ├─ Detect extension
    ├─ Decide folder
    ├─ Create folder (if missing)
    ├─ Move file
    └─ Log action
 ↓
DONE
```

---

## 🧠 Core Concepts You’ll Practice

| Concept         | Used |
| --------------- | ---- |
| `os` module     | ✅    |
| `shutil`        | ✅    |
| File safety     | ✅    |
| Automation flow | ✅    |
| Logging         | ✅    |
| CLI mindset     | ✅    |

---

## 🚫 What NOT to do (important)

❌ No GUI
❌ No recursion
❌ No advanced OOP
❌ No external libraries

Keep it **pure Python automation**.

---

## 🎯 Day 5 Success Criteria

You finish Day 5 if:

* Files move automatically
* Folders are created safely
* Logs are written
* Script doesn’t crash on unknown files

---

## 🔜 Day 6 Preview (Motivation)

* Command-line arguments (`sys.argv`)
* Run tool like:

```bash
python organizer.py ~/Downloads
```

---

## 🟢 Final Verdict

You are **100% on the correct path**.
This structure:

* Builds real skills
* Prepares you for Linux tools
* Leads directly to automation & background scripts

---

If you want next:

* Full Day 5 README
* Step-by-step build plan
* Starter code skeleton
* Safety checklist before moving files

Just say **“Day 5 next”** 🔥
