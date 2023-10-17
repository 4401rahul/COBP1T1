# A program  to read a text file and find all unique words and how many times the word occurrences

# Written by Rahul Joshi

# Import the string module, which contains a string of all ASCII characters that are considered punctuation.
import string

# Now define the count_unique_words function, this function takes a single argument file_path.
def count_unique_words(file_path):
    word_count = {} # This word_count dictionary will be used to keep track of unique words and their counts.

    # Open and Read the file
    with open(file_path, 'r') as file:

        # Read the text and split it into words
        text = file.read()
        words = text.split()  # The result is stored in the words list.

        # To count word occurrences
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # To Print unique words and their occurrences
    for word, count in word_count.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    file_path = r"C:\Users\Lenovo\Desktop\test.txt"

    count_unique_words(file_path)
