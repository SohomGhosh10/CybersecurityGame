import tkinter as tk
from tkinter import messagebox
import random

# Global variables
score = 0
total_questions = 0

def generate_arithmetic_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        question_text = f"What is {num1} + {num2}?"
        correct_answer = str(num1 + num2)
    elif operation == '-':
        question_text = f"What is {num1} - {num2}?"
        correct_answer = str(num1 - num2)
    elif operation == '*':
        question_text = f"What is {num1} * {num2}?"
        correct_answer = str(num1 * num2)
    else:
        while num2 == 0 or num1 % num2 != 0:
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
        question_text = f"What is {num1} / {num2}?"
        correct_answer = str(num1 // num2)

    return question_text, correct_answer

def generate_logical_question():
    questions = [
        ("Which number is missing in the series: 2, 4, 8, 16, ?", "32"),
        ("If A is 1, B is 2, what is Z?", "26"),
        ("If all bloops are razzies and all razzies are lazzies, all bloops are definitely lazzies. True or False?", "True"),
    ]
    question_text, correct_answer = random.choice(questions)
    return question_text, correct_answer

def generate_cybersecurity_question():
    questions = [
        ("What does the acronym 'VPN' stand for?", "Virtual Private Network"),
        ("What is phishing?", "A fraudulent attempt to obtain sensitive information"),
        ("Which of the following is a strong password?", "A1b@cD3fG!"),
    ]
    question_text, correct_answer = random.choice(questions)
    return question_text, correct_answer

def generate_random_question():
    question_type = random.choice(['arithmetic', 'logical', 'cybersecurity'])
    
    if question_type == 'arithmetic':
        return generate_arithmetic_question()
    elif question_type == 'logical':
        return generate_logical_question()
    elif question_type == 'cybersecurity':
        return generate_cybersecurity_question()

def check_answer(selected_option):
    global score, total_questions
    
    if selected_option == current_answer:
        score += 1
    
    total_questions += 1
    ask_to_continue()

def ask_to_continue():
    if messagebox.askyesno("Continue?", "Do you want to continue?"):
        show_question()
    else:
        show_final_score()

def show_question():
    global current_answer
    
    question_text, correct_answer = generate_random_question()
    current_answer = correct_answer
    
    question_label.config(text=question_text)
    
    options = [correct_answer]
    while len(options) < 4:
        if "or False" in question_text:  # Handle True/False questions
            options = ["True", "False"]
            break
        else:
            wrong_answer = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", str(random.randint(1, 50))])
            if wrong_answer not in options:
                options.append(wrong_answer)
    
    random.shuffle(options)
    
    for i, option in enumerate(options):
        option_buttons[i].config(text=option, command=lambda opt=option: check_answer(opt))

def show_final_score():
    messagebox.showinfo("Game Over", f"Your final score is {score} out of {total_questions}.")
    root.quit()

# GUI setup
root = tk.Tk()
root.title("Versatile Quiz Game")

question_label = tk.Label(root, text="", wraplength=400)
question_label.pack(pady=20)

option_buttons = []
for _ in range(4):
    btn = tk.Button(root, text="", width=50, height=2)
    btn.pack(pady=5)
    option_buttons.append(btn)

show_question()
root.mainloop()
