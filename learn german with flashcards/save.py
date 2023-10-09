def save_to_file(words):
    with open('save_file.txt', 'a', encoding='utf-8') as f:
        for word, translated_word in words.items():
            f.write(f"{word}: {translated_word}\n")

def load_from_file():
    words = {}
    try:
        with open('save_file.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(': ')    # Remove the newline character and split the line into key and value using ":"
                if len(parts) == 2:                 # Check if the line has 2 parts
                    word, translated_word = parts   # Unpack the parts into word and translated_word
                    words[word] = translated_word   # Add the word and its translation to the dictionary
        return words
    except FileNotFoundError:       # If the file is not found, return an empty dictionary so that we can use it 
        return {}                   # in the main menu to check if there are any flashcards and display an error message if there are none
        