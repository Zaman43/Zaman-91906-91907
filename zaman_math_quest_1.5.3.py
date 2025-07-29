from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import messagebox, ttk

#Variables for math quiz tracking.
question_no = 0 #Tracks current question number.
students_score = 0 #Tracks how many questions the user got correct.
current_quiz_questions = [] #Stores selected questions for the quiz.
selected_topic = "" #User selected topic.
selected_difficulty = "" #User selected difficulty

#Dictionary storing questions.
quiz = {
    "Algebra": {
        "Easy": [
            {"question": "Solve for x: 3x + 5 = 20", "answer": "5"},
            {"question": "What is x if 2x = 14?", "answer": "7"},
            {"question": "x + 4 = 9. Find x.", "answer": "5"},
            {"question": "If x - 7 = 3, find x.", "answer": "10"},
            {"question": "Solve for x: 4x = 24", "answer": "6"},
            {"question": "Find x: x/2 = 8", "answer": "16"},
            {"question": "If 5x = 20, then x = ?", "answer": "4"},
            {"question": "x - 3 = 7. What is x?", "answer": "10"},
            {"question": "If 7 + x = 13, find x.", "answer": "6"},
            {"question": "Solve for x: 8x = 32", "answer": "4"}

        ],
        "Medium": [
            {"question": "Solve for x: 5x - 7 = 18", "answer": "5"},
            {"question": "If 4x + 2 = 18, find x.", "answer": "4"},
            {"question": "2x + 3 = 11. What is x?", "answer": "4"},
            {"question": "Solve for x: x² - 5x + 6 = 0", "answer": "2 or 3"},
            {"question": "Solve the inequality: 3x - 4 > 5", "answer": "x > 3"},
            {"question": "Solve the system:\n x + y = 7\n x - y = 3", "answer": "x=5, y=2"},
            {"question": "Expand and simplify: 2(x + 3) - 4", "answer": "2x + 2"},
            {"question": "Solve for x: (1/2)x + 3 = 7", "answer": "8"},
            {"question": "A number decreased by 4 equals 10. Find the number.", "answer": "14"},
            {"question": "Solve for x: 4x - 3(x - 2) = 7", "answer": "13"},
        ],
        "Hard": [
            {"question": "Solve for x: x² - 4x - 5 = 0\n(Type the positive root only)", "answer": "5"},
            {"question": "Solve for x using quadratic formula: 2x² + 3x - 2 = 0\n(Type the root with decimal answer)", "answer": "0.5"},
            {"question": "Solve for x: 3x + 2y = 12 and 5x - y = 7\n(Type the value of x only)", "answer": "2"},
            {"question": "Simplify and write the coefficient: (2x³)(3x²) =", "answer": "6"},  
            {"question": "Find the smaller root of x² - 9x + 20 = 0", "answer": "4"},
            {"question": "Solve inequality |2x - 3| < 7\n(Type the lower bound of x)", "answer": "-2"},
            {"question": "If f(x) = 2x² - 3x + 1, find f(3).", "answer": "10"},
            {"question": "Solve for x: (x + 2)/(x - 1) = 3\n(Type decimal answer)", "answer": "2.5"},
            {"question": "Expand and simplify: (x - 3)(x + 4)\n(Type the coefficient of x²)", "answer": "1"},
            {"question": "If twice a number plus 3 equals 17, find the number.", "answer": "7"},
        ]
    },
    "Geometry": {
        "Easy": [
            
            {"question": "The lengths of the two shorter sides of a triangle are 10 cm and 14 cm. What could be the length of the largest side? Choose from: 25 cm, 13 cm, 30 cm, 21 cm. Type your answer.", "answer": "21"},
            {"question": "A triangle has two sides measuring 7 cm and 9 cm. What could be the length of the third side? Choose from: 15 cm, 3 cm, 18 cm, 10 cm. Type your answer.", "answer": "15"},
            {"question": "Look at the shape provided. What is the name of this shape?", "answer": "pentagon", "image": "geometry_easy_3.jpg"},
            {"question": "Which of the following shapes is a polygon? Options: 1) Circle  2) Ellipse  3) Curve  4) Triangle. Type the number of the correct option.", "answer": "4", "image": "geometry_easy_4.jpg"},
            {"question": "Look at the shape provided. What is the name of this shape?", "answer": "trapezium", "image": "geometry_easy_5.jpg"}

        ],
        "Medium": [
            {"question": "Solve for x: 5x - 7 = 18", "answer": "5"},
            {"question": "If 4x + 2 = 18, find x.", "answer": "4"},
            {"question": "2x + 3 = 11. What is x?", "answer": "4"},
            {"question": "Solve for x: x² - 5x + 6 = 0", "answer": "2 or 3"},
            {"question": "Solve the inequality: 3x - 4 > 5", "answer": "x > 3"},
            {"question": "Solve the system:\n x + y = 7\n x - y = 3", "answer": "x=5, y=2"},
            {"question": "Expand and simplify: 2(x + 3) - 4", "answer": "2x + 2"},
            {"question": "Solve for x: (1/2)x + 3 = 7", "answer": "8"},
            {"question": "A number decreased by 4 equals 10. Find the number.", "answer": "14"},
            {"question": "Solve for x: 4x - 3(x - 2) = 7", "answer": "13"},
        ],
        "Hard": [
            {"question": "Solve for x: x² - 4x - 5 = 0\n(Type the positive root only)", "answer": "5"},
            {"question": "Solve for x using quadratic formula: 2x² + 3x - 2 = 0\n(Type the root with decimal answer)", "answer": "0.5"},
            {"question": "Solve for x: 3x + 2y = 12 and 5x - y = 7\n(Type the value of x only)", "answer": "2"},
            {"question": "Simplify and write the coefficient: (2x³)(3x²) =", "answer": "6"},
            {"question": "Find the smaller root of x² - 9x + 20 = 0", "answer": "4"},
            {"question": "Solve inequality |2x - 3| < 7\n(Type the lower bound of x)", "answer": "-2"},
            {"question": "If f(x) = 2x² - 3x + 1, find f(3).", "answer": "10"},
            {"question": "Solve for x: (x + 2)/(x - 1) = 3\n(Type decimal answer)", "answer": "2.5"},
            {"question": "Expand and simplify: (x - 3)(x + 4)\n(Type the coefficient of x²)", "answer": "1"},
            {"question": "If twice a number plus 3 equals 17, find the number.", "answer": "7"},
        ]
    },
    "Statistics": {
        "Easy": [
            {"question": "What is the mean of 4, 8, 12?", "answer": "8"},
            {"question": "Find the median of 5, 7, 9.", "answer": "7"},
            {"question": "What is the mode of 3, 3, 6, 7?", "answer": "3"},
            {"question": "Find the range of 10, 15, 25.", "answer": "15"},
            {"question": "How many numbers are in this set: 1, 2, 3, 4, 5?", "answer": "5"},
            {"question": "What is the smallest number in the set: 6, 8, 3, 7?", "answer": "3"},
            {"question": "What is the largest number in the set: 2, 5, 1, 8?", "answer": "8"},
            {"question": "Find the mean of 10 and 20.", "answer": "15"},
            {"question": "What is the range of 4, 4, 4?", "answer": "0"},
            {"question": "What is the mode of 6, 6, 7, 8?", "answer": "6"}
        ],
        "Medium": [
            {"question": "A bivariate dataset has a correlation coefficient of 0.82. Is this closer to a strong or weak relationship? (1=strong, 0=weak)", "answer": "1"},
            {"question": "The heights of students are normally distributed with mean 170 and standard deviation 10. What proportion of students are taller than 180? (approximate to nearest whole number)", "answer": "16"},
            {"question": "A bag has 5 red and 15 blue balls. What is the probability of randomly selecting a red ball? (as a percentage)", "answer": "25"},
            {"question": "Two independent events A and B: P(A)=0.4, P(B)=0.5. What is P(A and B) as a percentage?", "answer": "20"},
            {"question": "A sample of 50 students has a mean of 75. A larger population has mean 72. What is the sample mean minus population mean?", "answer": "3"},
            {"question": "18 out of 30 students prefer tea. What is the percentage who prefer tea?", "answer": "60"},
            {"question": "A random variable X ~ N(50,5). What is the z-score for X=60?", "answer": "2"},
            {"question": "A spinner has 3 equal sections labelled 1,2,3. If spun twice, what is the probability of getting 1 then 2? (as a percentage rounded)", "answer": "11"},
            {"question": "A scatterplot shows a downward slope. Is the correlation positive or negative? (-1=negative, 1=positive)", "answer": "-1"},
            {"question": "A dataset has Q3=75 and Q1=45. What is the interquartile range?", "answer": "30"}
        ],
        "Hard": [
            {"question": "A 95% confidence interval for a mean is [48,52]. What is the margin of error?", "answer": "2"},
            {"question": "A regression line is ŷ = 2x+5. What is the predicted y when x=10?", "answer": "25"},
            {"question": "In a binomial distribution with n=10 and p=0.3, what is the expected number of successes?", "answer": "3"},
            {"question": "A sample mean is 80 with standard error 2. Construct a 95% confidence interval. What is the lower bound?", "answer": "76"},
            {"question": "A sample mean is 80 with standard error 2. Construct a 95% confidence interval. What is the upper bound?", "answer": "84"},
            {"question": "What is the probability of guessing exactly 3 correct out of 5 questions (each with 4 choices)? Approximate as percentage.", "answer": "8"},
            {"question": "A correlation coefficient is -0.92. Is the relationship strong or weak? (1=strong, 0=weak)", "answer": "1"},
            {"question": "A dataset has mean=50 and standard deviation=5. What is the coefficient of variation? (as a percentage)", "answer": "10"},
            {"question": "A test of significance yields p-value=0.03. Is this statistically significant at the 5% level? (1=yes, 0=no)", "answer": "1"},
            {"question": "In a population of 1000, a sample of 100 has a mean of 20. What percentage of the population was sampled?", "answer": "10"}
        ]
    }
}


#Function to save user's test score to a file called progress.txt.
def save_progress(topic, difficulty, score, total):
    """save quiz results to progress.txt"""
    try:
        with open("progress.txt", "a") as file:
            file.write(f"{topic},{difficulty},{score}/{total}\n")
            print(f"✅ Progress saved: {topic}, {difficulty}, {score}/{total}")
    except Exception as error:
        print(f"❌ Error saving progress: {error}")

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
#This compares the user input to the correct answer.
    if user_answer == correct:
        students_score += 1
        feedback_label.config(text="✅ Correct!", fg="green")
    else:
        feedback_label.config(text=f"❌ Incorrect. The answer was {correct}", fg="red")

    score_label.config(text=f"Score: {students_score}/{len(current_quiz_questions)}")
    next_button.config(state="normal") #Enables the next button

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
        #quiz summary 
        complete_topic_label.config(text=f"Topic: {selected_topic}")
        show_frame(complete_level)
        complete_questions_label.config(text=f"Questions Answered: {len(current_quiz_questions)}")
        complete_score_label.config(text=f"Correct Answers: {students_score}/{len(current_quiz_questions)}")
        save_progress(selected_topic, selected_difficulty, students_score, len(current_quiz_questions)) #for saving file

#Show current question and image if there is one.
def show_question():
    question_data = current_quiz_questions[question_no]
    question_label.config(text=question_data["question"])

    if "image" in question_data and question_data["image"]:
        try:
            img = Image.open(question_data["image"])
            img = img.resize((300, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo, text="")
            image_label.image = photo
        except FileNotFoundError:
            image_label.config(text="Image not found", image='') #if there is an error and the image is not loading it will say.
            image_label.image = None
    else:
        image_label.config(image="", text="") #if there is supposed to be no image it won't say image not found.
        image_label.image = None

    answer_entry.delete(0, tk.END)
    answer_entry.focus()

#Starts the game.
def start_game():
    global question_no, students_score, current_quiz_questions,selected_topic,selected_difficulty
    
    selected_topic = topic_box.get()
    selected_difficulty = difficulty_box.get()
    
    #This checks if both selections have been made.
    if not selected_topic or not selected_difficulty:
        messagebox.showwarning("Selection Required", "Please select both a topic and a difficulty before starting.")
        return
    
    question_no = 0
    students_score = 0

    #Updates topic and difficulty labels.
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
#Ends program
def exit_program():
    root.destroy()

#Root window.
root = tk.Tk()
root.title("Math Quest")
root.geometry("700x800")
root.configure(bg="#ccffcc")

#The main menu frame.===========================================================================================================================================================================================================================
main_frame = tk.Frame(root, bg="#ccffcc")
main_frame.place(relwidth=1, relheight=1)

#The title of the game.
title_label = tk.Label(main_frame, text="Math Quest", font=("Calibri", 18, "bold"),
                       bg="#339966", fg="white", width=25, height=2)
title_label.pack(pady=15)

#Gif icon.
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'tools.gif')#tools.gif is in same folder.

pil_image = Image.open(image_path)
pil_image = pil_image.resize((pil_image.width // 6, pil_image.height // 6), Image.Resampling.LANCZOS)
tools_icon = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(main_frame, image=tools_icon, bg="#ccffcc")
image_label.image = tools_icon 
image_label.pack(pady=10)

#Menu buttons.
def start_new_game():
    show_frame(topic_frame)

def view_progress():
    if not os.path.exists("progress.txt"):
        messagebox.showinfo("Progress", "Nothing recorded yet.")
        return

    with open("progress.txt", "r") as file:
        quiz_entries = file.readlines()

    if not quiz_entries:
        messagebox.showinfo("Progress", "Nothing recorded yet.")
        return

    progress_text = "Your Progress:\n\n"
    for line in quiz_entries:
        progress_text += line.strip() + "\n"

    messagebox.showinfo("Progress", progress_text)


def view_instructions():
    messagebox.showinfo("Instructions", "Choose a math topic and difficulty suitable for you!\nAnswer questions to improve your score.")

def go_back_to_main():
    show_frame(main_frame)

#This adds the menu buttons.
button_style(main_frame, "Start New Game", start_new_game).pack(pady=5)
button_style(main_frame, "View Progress", view_progress).pack(pady=5)
button_style(main_frame, "View Instructions", view_instructions).pack(pady=5)

tk.Button(main_frame, text="Exit", bg="red", fg="white", font=("Calibri", 12, "bold"),
          width=20, height=2, command=exit_program).pack(pady=10)

#Frame for topic and difficulty selection.===========================================================================================================================================================
topic_frame = tk.Frame(root, bg="#ccffcc")
topic_frame.place(relwidth=1, relheight=1)

topic_label_title = tk.Label(topic_frame, text="Choose Topic", font=("Calibri", 12, "bold"),
                             bg="#339966", fg="white", width=25, height=2)
topic_label_title.pack(pady=8)

topic_box = ttk.Combobox(topic_frame, values=["Geometry", "Algebra", "Statistics"], font=("Calibri", 12), state="readonly")#readonly will make it so the dropdown box cannot be written in.
topic_box.pack(pady=5)

difficulty_label_title = tk.Label(topic_frame, text="Choose Difficulty", font=("Calibri", 12, "bold"),
                                 bg="#339966", fg="white", width=25, height=2)
difficulty_label_title.pack(pady=8)

difficulty_box = ttk.Combobox(topic_frame, values=["Easy", "Medium", "Hard"], font=("Calibri", 12), state="readonly")#readonly will make it so the dropdown box cannot be written in.
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

#Quiz header labels.
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

#Entry for the user 
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

#Complete level frame.======================================================================================================================================================
complete_level = tk.Frame(root, bg="#ccffcc")
complete_level.place(relwidth=1, relheight=1)

tk.Label(complete_level, text="Level Complete!", font=("Calibri", 24, "bold"),
         bg="#339966", fg="white", width=25, height=2).pack(pady=10)
complete_topic_label = tk.Label(complete_level, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
complete_topic_label.pack(pady=5)
complete_questions_label = tk.Label(complete_level, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
complete_questions_label.pack(pady=5)
complete_score_label = tk.Label(complete_level, text="", font=("Calibri", 14, "bold"), bg="#ccffcc")
complete_score_label.pack(pady=5)

button_style(complete_level, "Back To Main Menu", go_back_to_main, bg="#ffcc00", fg="black").pack(pady=20)  #Button to go back to main menu at the completed level screen.

#Start at main menu.
show_frame(main_frame)
root.mainloop()
