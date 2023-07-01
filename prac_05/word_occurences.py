"""Estimated time: 20 minutes
Actual time: 54 minutes"""


def main():
    collection_of_words = input("Enter a collection of words: ")
    word_occurrences = count_word_occurrences(collection_of_words)
    display_word_occurrences(word_occurrences)


def count_word_occurrences(input_string):
    word_counts = {}
    # didn't call it word_string as the word "word" occurs too many times in the code and is becoming hard to read.
    # input string shows where it

    words = input_string.split()

    for word in words:
        # A word at the start of a sentence will have a capital, however will still be the same word.
        # Words ending in a question mark or full stop should still be counted.
        cleaned_word = word.strip(".,!?\"'()").lower()
        word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    return word_counts


def display_word_occurrences(word_counts):
    print("Word occurrences in the string:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
