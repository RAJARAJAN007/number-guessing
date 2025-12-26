import tkinter as tk
import random

# ---------- GAME LOGIC (same as CLI) ----------

def generate_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 50)
    elif level == 3:
        return random.randint(1, 100)

def check_guess(guess, target):
    if guess == target:
        return "correct"
    elif guess > target:
        return "high"
    else:
        return "low"

# ---------- VARIABLES ----------

level = None
secret_number = None
attempts = 0
max_number = 0

# ---------- FUNCTIONS ----------

def start_game(selected_level):
    global level, secret_number, attempts, max_number

    level = selected_level
    attempts = 0

    if level == 1:
        max_number = 10
    elif level == 2:
        max_number = 50
    else:
        max_number = 100

    secret_number = generate_number(level)

    # Hide level UI
    level_label.pack_forget()
    level_frame.pack_forget()

    # Show game UI
    info_label.config(text=f"Guess a number from 1 to {max_number}")
    attempts_label.config(text="Attempts: 0")

    guess_label.pack(pady=5)
    guess_entry.pack(pady=5)
    submit_btn.pack(pady=10)
    attempts_label.pack(pady=5)

    guess_entry.delete(0, tk.END)
    guess_entry.focus()

def submit_guess():
    global attempts

    try:
        guess = int(guess_entry.get())
    except ValueError:
        return  # ignore invalid input

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    result = check_guess(guess, secret_number)

    if result == "correct":
        info_label.config(
            text=f"🎉 Congratulations! You guessed the number in {attempts} attempts."
        )
        root.after(2000, reset_game)
    elif result == "high":
        info_label.config(text="📈 Too high! Try again.")
    else:
        info_label.config(text="📉 Too low! Try again.")

    guess_entry.delete(0, tk.END)

def reset_game():
    global level, secret_number, attempts

    level = None
    secret_number = None
    attempts = 0

    # Hide game UI
    guess_label.pack_forget()
    guess_entry.pack_forget()
    submit_btn.pack_forget()
    attempts_label.pack_forget()

    # Show level UI again
    level_label.pack(pady=5)
    level_frame.pack(pady=5)

    info_label.config(text="Select a level to start")

# ---------- GUI ----------

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("420x380")
root.resizable(False, False)

tk.Label(
    root,
    text="Number Guessing Game",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Level selection
level_label = tk.Label(root, text="Select difficulty level:")
level_label.pack(pady=5)

level_frame = tk.Frame(root)
level_frame.pack(pady=5)

tk.Button(level_frame, text="Easy", width=10, command=lambda: start_game(1)).grid(row=0, column=0, padx=5)
tk.Button(level_frame, text="Medium", width=10, command=lambda: start_game(2)).grid(row=0, column=1, padx=5)
tk.Button(level_frame, text="Hard", width=10, command=lambda: start_game(3)).grid(row=0, column=2, padx=5)

# Game info
info_label = tk.Label(root, text="Select a level to start", font=("Arial", 11))
info_label.pack(pady=10)

# Guess UI (hidden initially)
guess_label = tk.Label(root, text="Enter your guess:")
guess_entry = tk.Entry(root, justify="center")
submit_btn = tk.Button(root, text="Submit Guess", width=15, command=submit_guess)
attempts_label = tk.Label(root, text="Attempts: 0")

root.mainloop()
