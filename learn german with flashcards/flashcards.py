import tkinter as tk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root, words):
        self.root = root
        self.words = words
        words = {}
        self.root.title("Flashcard App")

        self.current_flashcard_index = 0

        self.word_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.word_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.show_question()

        self.check_button = tk.Button(root, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=10)

    def show_question(self):
            if self.words:
                keys_list = list(self.words.keys()) 
                if self.current_flashcard_index >= len(keys_list):
                    messagebox.showinfo("End of Flashcards", "You've completed all flashcards!")
                    self.root.destroy()
                else:
                    current_flashcard_key = keys_list[self.current_flashcard_index] # Get the key of the current flashcard
                    if current_flashcard_key not in self.words:
                        messagebox.showerror("Error", f"Flashcard key '{current_flashcard_key}' not found in dictionary.")
                    else:
                        current_flashcard_value = self.words[current_flashcard_key] # Get the value of the current flashcard

                        flashcard_back = current_flashcard_value    # Get the back of the current flashcard (answer)

                        self.word_label.config(text=flashcard_back)
                        self.answer_entry.delete(0, tk.END)


            else:
                self.word_label.config(text="No flashcards found.") # Display an error message if no flashcards are found

    def check_answer(self):
        user_answer = self.answer_entry.get()                       # Get the answer from the entry box
        keys_list = list(self.words.keys())                         # Get the keys of the dictionary as a list (answers)
        correct_answer = keys_list[self.current_flashcard_index]    # Get the correct answer from the list of answers

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")

        # Move to the next flashcard
        self.current_flashcard_index += 1

        # Check if we've reached the end of the flashcards
        if self.current_flashcard_index == len(self.words):
            messagebox.showinfo("End of Flashcards", "You've completed all flashcards!")
            self.root.destroy()
        else:
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()