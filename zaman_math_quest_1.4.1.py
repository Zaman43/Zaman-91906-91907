from PIL import Image, ImageTk
import os

import tkinter as tk
from tkinter import messagebox, ttk

#Variables for math quiz tracking.
question_no = 0
students_score = 0
current_quiz_questions = []

quiz = {
    "Algebra": {
        "Easy": [
            {"question": "Solve for x: 3x + 5 = 20", "answer": "5", "image": "algebra_easy_1.png"},
            {"question": "What is x if 2x = 10?", "answer": "5", "image": "algebra_easy_2.png"},
            {"question": "x + 4 = 9. Find x.", "answer": "5", "image": "algebra_easy_3.png"},
        ],
        "Medium": [
            {"question": "Solve for x: 5x - 7 = 18", "answer": "5", "image": "algebra_medium_1.png"},
            {"question": "If 4x + 2 = 18, find x.", "answer": "4", "image": "algebra_medium_2.png"},
            {"question": "2x + 3 = 11. What is x?", "answer": "4", "image": "algebra_medium_3.png"},
        ],
        "Hard": [
            {"question": "Solve for x: 3(x - 2) + 4 = 13", "answer": "5", "image": "algebra_hard_1.png"},
            {"question": "If 2(x + 5) = 18, find x.", "answer": "4", "image": "algebra_hard_2.png"},
            {"question": "Find x: 5x - 3 = 2x + 6", "answer": "3", "image": "algebra_hard_3.png"},
        ]
    },
    "Addition": {
        "Easy": [
            {"question": "What is 2 + 3?", "answer": "5", "image": "addition_easy_1.png"},
            {"question": "Add 4 and 5.", "answer": "9", "image": "addition_easy_2.png"},
            {"question": "Calculate 1 + 7.", "answer": "8", "image": "addition_easy_3.png"},
        ],
        "Medium": [
            {"question": "Add 15 and 22.", "answer": "37", "image": "addition_medium_1.png"},
            {"question": "What is 34 + 18?", "answer": "52", "image": "addition_medium_2.png"},
            {"question": "Calculate 27 + 35.", "answer": "62", "image": "addition_medium_3.png"},
        ],
        "Hard": [
            {"question": "Add 123 and 456.", "answer": "579", "image": "addition_hard_1.png"},
            {"question": "Calculate 289 + 732.", "answer": "1021", "image": "addition_hard_2.png"},
            {"question": "What is 158 + 647?", "answer": "805", "image": "addition_hard_3.png"},
        ]
    },
    "Statistics": {
        "Easy": [
            {"question": "What is the mean of 2, 4, 6?", "answer": "4", "image": "statistics_easy_1.png"},
            {"question": "Find the median of 1, 3, 5.", "answer": "3", "image": "statistics_easy_2.png"},
            {"question": "What is the mode of 2, 2, 3?", "answer": "2", "image": "statistics_easy_3.png"},
        ],
        "Medium": [
            {"question": "Mean of 4, 8, 12, 16?", "answer": "10", "image": "statistics_medium_1.png"},
            {"question": "Median of 7, 3, 9, 5?", "answer": "6", "image": "statistics_medium_2.png"},
            {"question": "Mode of 5, 5, 6, 7?", "answer": "5", "image": "statistics_medium_3.png"},
        ],
        "Hard": [
            {"question": "Find variance of 2, 4, 6, 8.", "answer": "5", "image": "statistics_hard_1.png"},
            {"question": "Calculate standard deviation of 3, 3, 3, 3.", "answer": "0", "image": "statistics_hard_2.png"},
            {"question": "What is the range of 10, 20, 30?", "answer": "20", "image": "statistics_hard_3.png"},
        ]
    }
}

#Switch to other frame.
def show_frame(frame):
    frame.tkraise()

#My button styling.
def button_style(parent_widget, text, command, bg="#339966", fg="white"):
    return tk.Button(parent_widget, text=text, command=command, bg=bg, fg=fg,
                     font=("Calibri", 12, "bold"), width=20, height=2, relief="raised", bd=3)

#Submit user answer and show feedback.
def check_answer():
    global question_no, students_score
    user_answer = answer_entry.get().strip()
    correct = current_quiz_questions[question_no]["answer"]

    if user_answer == correct:
        students_score += 1
        feedback_label.config(text="✅ Correct!", fg="green")
    else:
        feedback_label.config(text=f"❌ Incorrect. The answer was {correct}", fg="red")

    score_label.config(text=f"Score: {students_score}/{len(current_quiz_questions)}")
    next_button.config(state="normal")

#Puts the user to next question.
def next_question():
    global question_no
    question_no += 1

    if question_no < len(current_quiz_questions):
        show_question()
        question_num_label.config(text=f"Question {question_no + 1} of {len(current_quiz_questions)}")
        answer_entry.delete(0, tk.END)
        feedback_label.config(text="")
        next_button.config(state="disabled")
    else:
        show_frame(complete_level)
        complete_score_label.config(text=f"Correct Answers: {students_score}/{len(current_quiz_questions)}")

#Show current question and image.
def show_question():
    question_data = current_quiz_questions[question_no]
    question_label.config(text=question_data["question"])

    try:
        img = Image.open(question_data["image"])
        img = img.resize((300, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="Image not found", image='')

    answer_entry.delete(0, tk.END)
    answer_entry.focus()

#Starts the game.
def start_game():
    global question_no, students_score, current_quiz_questions
    question_no = 0
    students_score = 0

    #Update topic and difficulty labels.
    selected_topic = topic_box.get()
    selected_difficulty = difficulty_box.get()
    current_quiz_questions = quiz[selected_topic][selected_difficulty]

    topic_label.config(text=f"Topic: {selected_topic}")
    difficulty_label.config(text=f"Difficulty: {selected_difficulty}")

    show_frame(quiz_frame)
    show_question()
    question_num_label.config(text=f"Question 1 of {len(current_quiz_questions)}")
    next_button.config(state="disabled")
    score_label.config(text=f"Score: 0/{len(current_quiz_questions)}")

def exit_program():
    root.destroy()

#Root window.
root = tk.Tk()
root.title("Math Quest")
root.geometry("600x500")
root.configure(bg="#ccffcc")

#The main menu frame.
main_frame = tk.Frame(root, bg="#ccffcc")
main_frame.place(relwidth=1, relheight=1)

title_label = tk.Label(main_frame, text="Math Quest", font=("Calibri", 18, "bold"),
                       bg="#339966", fg="white", width=25, height=2)
title_label.pack(pady=15)

#Gif using PhotoImage.
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'tools.gif')#tools.gif is in same folder as script

pil_image = Image.open(image_path)
pil_image = pil_image.resize((pil_image.width // 6, pil_image.height // 6), Image.Resampling.LANCZOS)
calculator_icon = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(main_frame, image=calculator_icon, bg="#ccffcc")
image_label.image = calculator_icon 
image_label.pack(pady=10)

def start_new_game():
    show_frame(topic_frame)

def continue_progress():  #not done need to add save to file.
    messagebox.showinfo("Not done")

def view_instructions():
    messagebox.showinfo("Instructions", "Choose a math topic and difficulty suitable for you!\nAnswer questions to improve your score.")

def go_back_to_main():
    show_frame(main_frame)

button_style(main_frame, "Start New Game", start_new_game).pack(pady=5)
button_style(main_frame, "Continue Progress", continue_progress).pack(pady=5)
button_style(main_frame, "View Instructions", view_instructions).pack(pady=5)

tk.Button(main_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(pady=10)

#Frame for topic and difficulty selection.
topic_frame = tk.Frame(root, bg="#ccffcc")
topic_frame.place(relwidth=1, relheight=1)

topic_label_title = tk.Label(topic_frame, text="Choose Topic", font=("Calibri", 12, "bold"),
                             bg="#339966", fg="white", width=25, height=2)
topic_label_title.pack(pady=8)

topic_box = ttk.Combobox(topic_frame, values=["Addition", "Algebra", "Statistics"], font=("Calibri", 12), state="readonly")
topic_box.pack(pady=5)

difficulty_label_title = tk.Label(topic_frame, text="Choose Difficulty", font=("Calibri", 12, "bold"),
                                 bg="#339966", fg="white", width=25, height=2)
difficulty_label_title.pack(pady=8)

difficulty_box = ttk.Combobox(topic_frame, values=["Easy", "Medium", "Hard"], font=("Calibri", 12), state="readonly")
difficulty_box.current(0)
difficulty_box.pack(pady=5)

button_style(topic_frame, "Start", start_game, bg="#ffcc00", fg="black").pack(pady=20)
button_style(topic_frame, "Back", go_back_to_main, bg="#6666cc").pack(pady=5)

tk.Button(topic_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(side="bottom", pady=10)

#Frame for quiz. 
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

image_label = tk.Label(quiz_frame, bg="#ccffcc")#Label question images.
image_label.pack(pady=10)

answer_entry = tk.Entry(quiz_frame, font=("Calibri", 14))
answer_entry.pack(pady=5)

#Submit button.
button_style(quiz_frame, "Submit Answer", check_answer, bg="#339966").pack(pady=10)

feedback_label = tk.Label(quiz_frame, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
feedback_label.pack()

#Button to go to next question.
next_button = button_style(quiz_frame, "Next Question", next_question, bg="#ffcc00", fg="black")
next_button.config(state="disabled")
next_button.pack(pady=10)

#Label which tells user their score.
score_label = tk.Label(quiz_frame, text="Score: 0/3", font=("Calibri", 12, "bold"), bg="#ccffcc")
score_label.pack()

tk.Button(quiz_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(side="bottom", pady=10)

#Complete level frame.
complete_level = tk.Frame(root, bg="#ccffcc")
complete_level.place(relwidth=1, relheight=1)

tk.Label(complete_level, text="Level Complete!", font=("Calibri", 24, "bold"),
         bg="#339966", fg="white", width=25, height=2).pack(pady=10)
tk.Label(complete_level, text="Topic: Algebra", font=("Calibri", 14, "bold"), bg="#ccffcc").pack(pady=5)
tk.Label(complete_level, text="Questions Answered: 3", font=("Calibri", 14, "bold"), bg="#ccffcc").pack(pady=5)
complete_score_label = tk.Label(complete_level, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
complete_score_label.pack(pady=5)

button_style(complete_level, "Back To Main Menu", go_back_to_main, bg="#ffcc00", fg="black").pack(pady=20)  #Button to go back to main menu at the completed level screen.

#Start at main menu.
show_frame(main_frame)
root.mainloop()
