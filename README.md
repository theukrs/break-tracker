# Break Tracker 🕒  
![version](https://img.shields.io/badge/version-v0.1.2-blue)

A simple Python GUI app to help you track your break durations more effectively. Built using `tkinter`, this tool is designed to assist you in maintaining a healthy work-break balance during long sessions.

---

## 🚀 Features

- Start/Stop break timer with a single click  
- Live timer display with millisecond precision
- Toast-style notifications for break start, end, and reset
- Persistent break history saved in a local file (`data.txt`)  
- Automatically creates `data.txt` if missing
- Settings window with options to:
      - Reset total break time
      - Switch between mm:ss and mm:ss:ms formats
- Displays the current version in the window title  
- Clean UI with customizable color themes  
- **Modular code structure using `Counter` class** *(added in v0.1.2)*

---

## 🆕 Changelog – v0.2.0

- Added toast-style notifications for key events (break start/end/reset)
- Added settings window with reset and time format options
- Millisecond-precision live timer
- Improved UI color consistency and styles  
- Updated main window layout for better readability

---

## 🛠️ Tech Stack

- Python 3  
- Tkinter  
- File I/O (for persistent tracking)

---

## 📷 Screenshot  
<p align="center">
  <img src="https://github.com/theukrs/break-tracker/blob/main/demo.gif?raw=true" alt="Break Tracker Demo">
</p>

---

## 📦 Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/theukrs/break-tracker.git
