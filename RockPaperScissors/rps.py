

import tkinter as tk
import random


choices = ["rock", "paper", "scissors"]
pscore = cscore = 0
light_theme = {"bg": "#f0f0f0" , "fg": "#000"}
dark_theme = {"bg":"#222" , "fg":"#fff"}
curr_theme = light_theme

def apply_theme():
    root.config(bg=curr_theme["bg"])
    title_label.config(bg=curr_theme["bg"], fg=curr_theme["fg"])
    score_label.config(bg=curr_theme["bg"], fg=curr_theme["fg"])
    result_label.config(bg=curr_theme["bg"], fg=curr_theme["fg"])
    button_frame.config(bg=curr_theme["bg"])
    toggle_btn.config(bg="gray" , fg="white")

def toggle_theme():
    global curr_theme
    curr_theme = dark_theme if curr_theme==light_theme else light_theme
    apply_theme()
def play(choice):
    global pscore,cscore
    computer = random.choice(choices)
    result_text = f"Player: {choice.capitalize()}\nComputer: {computer.capitalize()}\n"
    if choice == computer:
        result_text +="It's a tie!"
    elif(choice == 'rock' and computer=='scissors')  or \
    (choice == 'paper' and computer=='rock')  or \
    (choice == 'scissors' and computer=='paper'):
        result_text += "You win!"
        pscore +=1
    else:
        result_text+="You lose!"
        cscore+=1
    result_label.config(text=result_text)
    score_label.config(text=f"Player: {pscore}  | Computer: {cscore}")

def reset_game():
    global pscore,cscore
    pscore=0
    cscore=0
    result_label.config(text="Make your move!")
    score_label.config(text="Player: 0 | Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors!")
root.geometry("500x500")

title_label = tk.Label(root, text="Rock Paper Scissors" , font=("Arial" , 18 ,"bold"))
title_label.pack(pady=10)
score_label = tk.Label(root, text="Player: 0 | Computer: 0" , font=("Arial" , 14))
score_label.pack(pady=5)
result_label = tk.Label(root, text="Make your move!" ,  font=("Arial" , 12))
result_label.pack(pady=20)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)


rock_img = tk.PhotoImage(file="images/rock.png")
paper_img = tk.PhotoImage(file="images/paper.png")
scissors_img = tk.PhotoImage(file="images/scissors.png")


rock_btn = tk.Button(button_frame, image=rock_img , command=lambda:play("rock"))
rock_btn.grid(row=0,column=0,padx=10)
paper_btn = tk.Button(button_frame, image=paper_img , command=lambda:play("paper"))
paper_btn.grid(row=0,column=1,padx=10)
scissor_btn = tk.Button(button_frame, image=scissors_img , command=lambda:play("scissors"))
scissor_btn.grid(row=0,column=2,padx=10)


reset_btn = tk.Button(root , text="Reset Game" , width=15 , height =2 , command=reset_game , bg="lightblue")
reset_btn.place(relx=0.5 , rely=0.98 , anchor="s")

toggle_btn=tk.Button(root, text="🌙 Switch to Dark Mode" , width = 20 , command=toggle_theme)
toggle_btn.place(relx=0.95 , rely=0.03 , anchor="ne")

apply_theme()

root.mainloop()

