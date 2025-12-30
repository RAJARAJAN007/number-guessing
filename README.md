# 🎯 Number Guessing Game

This repository contains **three versions** of the **Number Guessing Game**, implemented using different technologies for learning and practice.

1. **CLI Version** – play in the terminal  
2. **GUI Version** – play with a graphical interface using Tkinter  
3. **Web Version** – play in the browser using HTML, CSS, and JavaScript  

---

## 📁 Folder Structure

- number-guessing/
  - num_cli/
    - cli.py
    - README.md
  - num_gui/
    - gui.py
    - README.md
  - flask/
    - static/
      - style.css
      - images/
        - num.jpg
    - templates/
      - index.html
    - README.md
  - README.md

---

## 🖥 CLI Version

Play directly in the terminal.

### Features
- 3 difficulty levels:
  - Easy (1–10)
  - Medium (1–50)
  - Hard (1–100)
- Exception handling for invalid inputs
- Tracks number of attempts

📄 See **CLI README** for details.

---

## 🎨 GUI Version (Tkinter)

Play with a graphical interface using **Tkinter**.

### Features
- Select difficulty level with buttons
- Real-time feedback:
  - Too high 📈
  - Too low 📉
  - Correct 🎉
- Automatically shows congratulations message
- Automatically restarts the game after correct guess
- Tracks number of attempts

📄 See **GUI README** for details.

---

## 🌐 Web Version (HTML, CSS, JavaScript)

Play the game directly in your **web browser**.

### Features
- Retro / funky arcade-style UI
- Multi-screen game flow:
  - Main Menu
  - Level Selection
  - Guessing Screen
- Difficulty levels:
  - Easy (1–10)
  - Medium (1–50)
  - Hard (1–100)
- Instant feedback:
  - Too High 📈
  - Too Low 📉
  - Correct 🎉
- Attempt counter
- Restart, Back to Menu, and Exit options
- Transparent light-violet game box with background image
- Fully frontend (no backend required)

📄 See **Web README** inside the `flask` folder for details.

---

## 📌 Notes

- Requires **Python 3.x** for CLI and Tkinter versions
- No external libraries needed
- Web version runs without any server
- Great project for beginners to understand **logic, UI, and user interaction**

🎉 Enjoy guessing the numbers!
