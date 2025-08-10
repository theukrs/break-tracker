# 📋 Changelog – Break Tracker

All notable changes to this project will be documented here.

---
## [v0.2.0] – 2025-08-10
### ✨ New Features
- Added toast-style notifications for break start, end, and reset
- Added millisecond precision to live timer display
- New settings window with options to:
      - Reset total break time
      - Switch between mm:ss and mm:ss:ms formats

### 🎨 UI/UX
- Updated color scheme and refined button styles for better readability
- Improved layout consistency across main and settings windows

### 🛠 Refactoring
- Enhanced Counter class to support new time formats and settings
- Codebase prepared for easier feature expansion in future releases

---

## [v0.1.2] – 2025-07-19
### 🛠 Refactoring
- Extracted timer logic into a separate Counter class (counter.py)
- Simplified main.py by delegating timer functionality
- Codebase is now more modular and easier to maintain

---

## [v0.1.1] – 2025-07-06
### ✨ Improvements
- Added `__version__ = "0.1.1"` to enable internal version tracking
- App window now shows the current version in the title bar

### 🐛 Fixes
- Added fallback using `try-except` to create `data.txt` if it doesn't exist
- Prevents crash when running the app for the first time or if file is deleted

---

## [v0.1.0] – 2025-07-06
### 🎉 Initial Release
- Break timer with start/stop toggle and reset button
- Displays live timer using `Canvas` and formatted time
- Stores total break duration in `data.txt`
- Clean UI with customizable colors


