import random
import tkinter as tk

# Define game constants
CHOICES = ["Rock", "Paper", "Scissors"]
COLORS = {"Rock": "gray", "Paper": "white", "Scissors": "blue"}

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.configure(bg="black")

# Create labels for player and computer choices
player_label = tk.Label(root, text="Player:", font=("Arial", 14, "bold"), bg="black", fg="white")
player_choice_label = tk.Label(root, text="", font=("Arial", 18), bg="black", fg="white")
computer_label = tk.Label(root, text="Computer:", font=("Arial", 14, "bold"), bg="black", fg="white")
computer_choice_label = tk.Label(root, text="", font=("Arial", 18), bg="black", fg="white")

# Create labels for result and score
result_label = tk.Label(root, text="", font=("Arial", 20, "bold"), bg="black", fg="white")
player_score_label = tk.Label(root, text="Player Score: 0", font=("Arial", 14, "bold"), bg="black", fg="white")
computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 14, "bold"), bg="black", fg="white")

# Create buttons for player choices
rock_button = tk.Button(root, text="Rock", font=("Arial", 12), bg="gray", command=lambda: play_game("Rock"))
paper_button = tk.Button(root, text="Paper", font=("Arial", 12), bg="white", command=lambda: play_game("Paper"))
scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), bg="blue", command=lambda: play_game("Scissors"))

# Function to handle player choices and determine the winner
def play_game(player_choice):
    computer_choice = random.choice(CHOICES)

    player_choice_label.config(text=player_choice, bg=COLORS[player_choice])
    computer_choice_label.config(text=computer_choice, bg=COLORS[computer_choice])

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You win!")
        update_score("player")
    else:
        result_label.config(text="Computer wins!")
        update_score("computer")

# Function to update the score
def update_score(winner):
    if winner == "player":
        player_score = int(player_score_label.cget("text").split(": ")[1]) + 1
        player_score_label.config(text=f"Player Score: {player_score}")
    else:
        computer_score = int(computer_score_label.cget("text").split(": ")[1]) + 1
        computer_score_label.config(text=f"Computer Score: {computer_score}")

# Place widgets on the window
player_label.grid(row=0, column=0)
player_choice_label.grid(row=0, column=1)
computer_label.grid(row=1, column=0)
computer_choice_label.grid(row=1, column=1)
result_label.grid(row=2, columnspan=2)
player_score_label.grid(row=3, column=0)
computer_score_label.grid(row=3, column=1)
rock_button.grid(row=4, column=0, pady=10)
paper_button.grid(row=4, column=1, pady=10)
scissors_button.grid(row=5, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
