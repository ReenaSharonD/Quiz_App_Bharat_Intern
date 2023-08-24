import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct": 0
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["Mars", "Venus", "Jupiter", "Mercury"],
                "correct": 0
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
                "correct": 2
            }
        ]
        
        self.question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(fill="x", padx=20, pady=5)
        
        self.next_button = tk.Button(root, text="Next", font=("Helvetica", 12), command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.update_question()

    def update_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            
            self.next_button.config(state="disabled")
        else:
            self.show_results()

    def check_answer(self, selected_option):
        correct_option = self.questions[self.question_index]["correct"]
        if selected_option == correct_option:
            self.score += 1
        self.question_index += 1
        self.update_question()

    def next_question(self):
        if self.question_index < len(self.questions):
            self.question_index += 1
            self.update_question()

    def show_results(self):
        messagebox.showinfo("Quiz Results", f"You scored {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
