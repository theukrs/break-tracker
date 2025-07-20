# Break Tracker 🕒  
![version](https://img.shields.io/badge/version-v0.1.2-blue)

A simple Python GUI app to help you track your break durations more effectively. Built using `tkinter`, this tool is designed to assist you in maintaining a healthy work-break balance during long sessions.

---

## 🚀 Features

- Start/Stop break timer with a single click  
- Live timer display using `Canvas` and custom time formatting  
- Persistent break history saved in a local file (`data.txt`)  
- Automatically creates `data.txt` if missing  
- Displays the current version in the window title  
- Clean UI with customizable color themes  
- **Modular code structure using `Counter` class** *(added in v0.1.2)*

---

## 🆕 Changelog – v0.1.2

- Refactored timer logic into a separate `Counter` class (`counter.py`)  
- Improved code readability and structure  
- Prepped for easier expansion (settings, theming, etc.)

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
