import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    result_text.set(f"You chose {user_choice}, Computer chose {comp_choice}")

    if user_choice == comp_choice:
        outcome = "It's a Tie!"
        result_label.config(fg="black")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        outcome = "You Win!"
        user_score += 1
        result_label.config(fg="green")
    else:
        outcome = "You Lose!"
        comp_score += 1
        result_label.config(fg="red")

    result.set(outcome)
    user_score_label.config(text=f"Your Score: {user_score}")
    comp_score_label.config(text=f"Computer Score: {comp_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_text.set("")
    result.set("")
    user_score_label.config(text="Your Score: 0")
    comp_score_label.config(text="Computer Score: 0")
    result_label.config(fg="black")

adi = tk.Tk()
adi.title("Rock Paper Scissors Game")
adi.geometry("420x450")
adi.configure(bg="white")

title = tk.Label(adi, text="Rock - Paper - Scissors", font=("Arial", 20, "bold"), bg="yellow", fg="blue")
title.pack(pady=10, fill="x")

result_text = tk.StringVar()
result = tk.StringVar()

info_label = tk.Label(adi, textvariable=result_text, font=("Arial", 13), bg="white", fg="black")
info_label.pack(pady=(5, 0))

result_label = tk.Label(adi, textvariable=result, font=("Arial", 16, "bold"), bg="white", fg="black")
result_label.pack(pady=5)

button_frame = tk.Frame(adi, bg="white")
button_frame.pack(pady=15)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 14), width=10, bg="red", fg="white", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=6)

paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 14), width=10, bg="green", fg="white", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=6)

scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 14), width=10, bg="blue", fg="white", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=6)

score_frame = tk.Frame(adi, bg="white")
score_frame.pack(pady=20)

user_score_label = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12), bg="white", fg="brown")
user_score_label.grid(row=0, column=0, padx=20)

comp_score_label = tk.Label(score_frame, text="Computer Score: 0", font=("Arial", 12), bg="white", fg="black")
comp_score_label.grid(row=0, column=1, padx=20)

reset_btn = tk.Button(adi, text="Reset Game", font=("Arial", 12), bg="maroon", fg="white", command=reset_game)
reset_btn.pack(pady=10)

adi.mainloop()
