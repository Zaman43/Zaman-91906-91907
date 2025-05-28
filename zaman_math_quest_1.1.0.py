import tkinter as tk
from tkinter import messagebox, ttk

# Variables for math quiz tracking.
question_no = 0
students_score = 0

quiz = [
    {"topic": "Algebra", "difficulty": "Easy", "question": "Solve for x: 3x + 5 = 20", "answer": "5"},
    {"topic": "Algebra", "difficulty": "Easy", "question": "What is x if 2x = 10?", "answer": "5"},
    {"topic": "Algebra", "difficulty": "Easy", "question": "x + 4 = 9. Find x.", "answer": "5"},
]

# Switch to other frame.
def show_frame(frame):
    frame.tkraise()

# My button styling.
def button_style(parent_widget, text, command, bg="#339966", fg="white"):
    return tk.Button(parent_widget, text=text, command=command, bg=bg, fg=fg,
                     font=("Calibri", 12, "bold"), width=20, height=2, relief="raised", bd=3)

# Submit user answer and show feedback.
def check_answer():
    global question_no, students_score
    user_answer = answer_entry.get().strip()
    correct = quiz[question_no]["answer"]

    if user_answer == correct:
        students_score += 1
        feedback_label.config(text="✅ Correct!", fg="green")
    else:
        feedback_label.config(text=f"❌ Incorrect. The answer was {correct}", fg="red")

    score_label.config(text=f"Score: {students_score}/{len(quiz)}")
    next_button.config(state="normal")

# Puts the user to next question.
def next_question():
    global question_no
    question_no += 1

    if question_no < len(quiz):
        question = quiz[question_no]
        question_label.config(text=question["question"])
        answer_entry.delete(0, tk.END)
        feedback_label.config(text="")
        next_button.config(state="disabled")
        question_num_label.config(text=f"Question {question_no+1} of {len(quiz)}")
    else:
        show_frame(complete_level)
        complete_score_label.config(text=f"Correct Answers: {students_score}/{len(quiz)}")

# Starts the game.
def start_game():
    global question_no, students_score
    question_no = 0
    students_score = 0

    # Update topic and difficulty labels.
    topic = topic_box.get()
    difficulty = difficulty_box.get()
    topic_label.config(text=f"Topic: {topic}")
    difficulty_label.config(text=f"Difficulty: {difficulty}")

    show_frame(quiz_frame)
    # Show first question.
    question = quiz[question_no]
    question_label.config(text=question["question"])
    question_num_label.config(text=f"Question 1 of {len(quiz)}")
    answer_entry.delete(0, tk.END)
    feedback_label.config(text="")
    next_button.config(state="disabled")
    score_label.config(text=f"Score: 0/{len(quiz)}")

def exit_program():
    root.quit()

# Root window.
root = tk.Tk()
root.title("Math Quest")
root.geometry("600x500")
root.configure(bg="#ccffcc")

# The main menu frame.
main_frame = tk.Frame(root, bg="#ccffcc")
main_frame.place(relwidth=1, relheight=1)

title_label = tk.Label(main_frame, text="Math Quest", font=("Calibri", 18, "bold"),
                       bg="#339966", fg="white", width=25, height=2)
title_label.pack(pady=15)

# Gif using PhotoImage
image_path = r"C:\Users\zaman\OneDrive - Lynfield College\Zaman Assessment 91906 and 91907\image component\tools.gif"

calculator_icon = tk.PhotoImage(file=image_path)
calculator_icon = calculator_icon.subsample(5, 5)  # size reduction factor
image_label = tk.Label(main_frame, image=calculator_icon, bg="#ccffcc")
image_label.pack(pady=10)


def start_new_game():
    show_frame(topic_frame)

def continue_progress():  # not done need to add save to file
    messagebox.showinfo("Not done", "This feature is not implemented yet.")

def view_instructions():
    messagebox.showinfo("Instructions", "Choose a math topic and difficulty suitable for you!\nAnswer questions to improve your score.")

def go_back_to_main():
    show_frame(main_frame)

button_style(main_frame, "Start New Game", start_new_game).pack(pady=5)
button_style(main_frame, "Continue Progress", continue_progress).pack(pady=5)
button_style(main_frame, "View Instructions", view_instructions).pack(pady=5)

tk.Button(main_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(pady=10)

# Frame for topic and difficulty selection
topic_frame = tk.Frame(root, bg="#ccffcc")
topic_frame.place(relwidth=1, relheight=1)

topic_label_title = tk.Label(topic_frame, text="Choose Topic", font=("Calibri", 12, "bold"),
                             bg="#339966", fg="white", width=25, height=2)
topic_label_title.pack(pady=8)

topic_box = ttk.Combobox(topic_frame, values=["Addition", "Algebra", "Statistics"], font=("Calibri", 12))
topic_box.current(1)
topic_box.pack(pady=5)

difficulty_label_title = tk.Label(topic_frame, text="Choose Difficulty", font=("Calibri", 12, "bold"),
                                 bg="#339966", fg="white", width=25, height=2)
difficulty_label_title.pack(pady=8)

difficulty_box = ttk.Combobox(topic_frame, values=["Easy", "Medium", "Hard"], font=("Calibri", 12))
difficulty_box.current(0)
difficulty_box.pack(pady=5)

button_style(topic_frame, "Start", start_game, bg="#ffcc00", fg="black").pack(pady=20)
button_style(topic_frame, "Back", go_back_to_main, bg="#6666cc").pack(pady=5)

tk.Button(topic_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(side="bottom", pady=10)

# Frame for quiz
quiz_frame = tk.Frame(root, bg="#ccffcc")
quiz_frame.place(relwidth=1, relheight=1)

top_frame = tk.Frame(quiz_frame, bg="#ccffcc")
top_frame.pack(pady=10)

topic_label = tk.Label(top_frame, text="Topic: Algebra", font=("Calibri", 12, "bold"),
                       bg="#339966", fg="white", width=15)
topic_label.grid(row=0, column=0, padx=10)

difficulty_label = tk.Label(top_frame, text="Difficulty: Easy", font=("Calibri", 12, "bold"),
                            bg="#339966", fg="white", width=15)
difficulty_label.grid(row=0, column=1, padx=10)

question_num_label = tk.Label(top_frame, text="Question 1 of 3", font=("Calibri", 12, "bold"), bg="#ccffcc")
question_num_label.grid(row=0, column=2, padx=10)

question_label = tk.Label(quiz_frame, text="", font=("Calibri", 16, "bold"), bg="#ccffcc")
question_label.pack(pady=20)

answer_entry = tk.Entry(quiz_frame, font=("Calibri", 14))
answer_entry.pack(pady=5)

# Submit button.
button_style(quiz_frame, "Submit Answer", check_answer, bg="#339966").pack(pady=10)

feedback_label = tk.Label(quiz_frame, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
feedback_label.pack()

# Button to go to next question.
next_button = button_style(quiz_frame, "Next Question", next_question, bg="#ffcc00", fg="black")
next_button.config(state="disabled")
next_button.pack(pady=10)

# label which tells user their score.
score_label = tk.Label(quiz_frame, text="Score: 0/3", font=("Calibri", 12, "bold"), bg="#ccffcc")
score_label.pack()

tk.Button(quiz_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(side="bottom", pady=10)

# Complete level frame.
complete_level = tk.Frame(root, bg="#ccffcc")
complete_level.place(relwidth=1, relheight=1)

tk.Label(complete_level, text="Level Complete!", font=("Calibri", 24, "bold"),
         bg="#339966", fg="white", width=25, height=2).pack(pady=10)
tk.Label(complete_level, text="Topic: Algebra", font=("Calibri", 14, "bold"), bg="#ccffcc").pack(pady=5)
tk.Label(complete_level, text="Questions Answered: 3", font=("Calibri", 14, "bold"), bg="#ccffcc").pack(pady=5)
complete_score_label = tk.Label(complete_level, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
complete_score_label.pack(pady=5)

button_style(complete_level, "Back To Main Menu", go_back_to_main, bg="#ffcc00", fg="black").pack(pady=20)

# Start at main menu.
show_frame(main_frame)
root.mainloop()
