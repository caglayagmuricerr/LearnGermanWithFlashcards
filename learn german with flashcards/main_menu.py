import tkinter as tk
from tkinter import messagebox

import detect_language
import translator
import flashcards
import save

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")

        self.word_entry_label = tk.Label(root, text="Welcome to the German Flashcard App!", font=("Helvetica", 16))
        word_label = tk.Label(root, text="Enter the word you want to translate:", font=("Helvetica", 12))

        self.word_entry_label.grid(row = 0, column = 1, padx = 20, pady = 10)
        word_label.grid(row = 1, column = 0, padx = 20, pady = 10)

        self.word_entry = tk.Entry(root, width = 40, font=("Helvetica", 12))
        self.word_entry.grid(row = 1, column = 1, padx = 20, pady = 10)

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_word)
        self.translate_button.grid(row = 2, column = 1, padx = 20, pady = 10)

        self.open_flashcards_button = tk.Button(root, text="Study My Flashcards", command=self.open_flashcards)
        self.open_flashcards_button.grid(row = 3, column = 1, padx = 20, pady = 10)

    def translate_word(self):
        word = self.word_entry.get()

        if not word:
            messagebox.showerror("Error", "Please enter a word.")
            return

        # Detect the language of the word user entered
        language = detect_language.detectlanguage(word)

        # Translate the word user entered to German
        translation = translator.translate(word, language)

        # Save the word and its translation to a file
        save.save_to_file({word: translation})

    def open_flashcards(self):
        # Load words from the file
        words = save.load_from_file()

        if not words:
            messagebox.showinfo("No Flashcards", "No flashcards found. Please translate a word first.")
            return

        # Create a flashcard app with the loaded words
        flashcard_root = tk.Toplevel(self.root)
        flashcard_app = flashcards.FlashcardApp(flashcard_root, words)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()