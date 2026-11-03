
import tkinter as tk
from tkinter import messagebox
from database import create_database, save_score

# Create Database
create_database()

# Quiz Questions
questions = [
    {
        "question": "1. Which language is used for Python programming?",
        "options": ["Python", "Java", "HTML", "CSS"],
        "answer": "Python"
    },
    {
        "question": "2. Which function is used to display output?",
        "options": ["input()", "print()", "display()", "show()"],
        "answer": "print()"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool"
    },
    {
        "question": "5. Which keyword is used to define a function?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "6. Which operator is used for addition?",
        "options": ["+", "-", "*", "/"],
        "answer": "+"
    },
    {
        "question": "7. Which loop repeats while a condition is true?",
        "options": ["for", "while", "if", "def"],
        "answer": "while"
    },
    {
        "question": "8. Which function gets user input?",
        "options": ["print()", "input()", "type()", "len()"],
        "answer": "input()"
    },
    {
        "question": "19. Which extension is used for Python files?",
        "options": [".java", ".html", ".py", ".css"],
        "answer": ".py"
    }

]

current_question = 0
score = 0
user_name = ""


def start_quiz():
    global user_name

    user_name = name_entry.get().strip()

    if user_name == "":
        messagebox.showwarning("Warning", "Please enter your name")
        return

    start_frame.pack_forget()
    quiz_frame.pack(pady=30)

    show_question()


def show_question():
    global current_question

    if current_question < len(questions):

        q = questions[current_question]

        question_label.config(text=q["question"])
        selected_option.set("")

        for i, option in enumerate(q["options"]):
            option_buttons[i].config(
                text=option,
                value=option
            )

        progress_label.config(
            text=f"Question {current_question + 1} / {len(questions)}"
        )

    else:
        show_result()


def next_question():
    global current_question, score

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Please select an answer"
        )
        return

    correct_answer = questions[current_question]["answer"]

    if selected == correct_answer:
        score += 1

    current_question += 1
    show_question()


def show_result():
    quiz_frame.pack_forget()
    result_frame.pack(pady=40)

    result_label.config(
        text=f"Hello {user_name}!\n\n"
             f"Your Score: {score}/{len(questions)}"
    )

    save_score(user_name, score)


# Main Window
root = tk.Tk()
root.title("Python Quiz Application")
root.geometry("500x450")
root.config(bg="#eaf2f8")


# Start Frame
start_frame = tk.Frame(root, bg="#eaf2f8")
start_frame.pack(pady=70)

tk.Label(
    start_frame,
    text="QUIZ APPLICATION",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#154360"
).pack(pady=20)

tk.Label(
    start_frame,
    text="Enter Your Name",
    font=("Arial", 13),
    bg="#eaf2f8"
).pack()

name_entry = tk.Entry(start_frame, font=("Arial", 14))
name_entry.pack(pady=10)

tk.Button(
    start_frame,
    text="Start Quiz",
    font=("Arial", 13, "bold"),
    bg="#2874a6",
    fg="white",
    command=start_quiz
).pack(pady=15)


# Quiz Frame
quiz_frame = tk.Frame(root, bg="#eaf2f8")

progress_label = tk.Label(
    quiz_frame,
    font=("Arial", 12, "bold"),
    bg="#eaf2f8"
)
progress_label.pack(pady=10)

question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 14, "bold"),
    wraplength=430,
    bg="#eaf2f8"
)
question_label.pack(pady=20)

selected_option = tk.StringVar()

option_buttons = []

for i in range(4):
    btn = tk.Radiobutton(
        quiz_frame,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12),
        bg="#eaf2f8"
    )
    btn.pack(anchor="w", padx=50, pady=5)
    option_buttons.append(btn)


tk.Button(
    quiz_frame,
    text="Next Question",
    font=("Arial", 12, "bold"),
    bg="#239b56",
    fg="white",
    command=next_question
).pack(pady=25)


# Result Frame
result_frame = tk.Frame(root, bg="#01070b")

result_label = tk.Label(
    result_frame,
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
result_label.pack(pady=30)

tk.Button(
    result_frame,
    text="Exit",
    command=root.destroy,
    font=("Arial", 12),
    bg="#c0392b",
    fg="white"
).pack(pady=15)


# Run Application
root.mainloop()
