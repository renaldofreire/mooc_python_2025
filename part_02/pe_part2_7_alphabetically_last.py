# Programming exercise:
# Alphabetically last

word_one = input("Please type in the 1st word: ")
word_two = input("Please type in the 2nd word: ")

if word_one < word_two:
    print(f"{word_two} comes alphabetically last.")
elif word_two < word_one:
    print(f"{word_one} comes alphabetically last.")
elif word_one == word_two:
    print("You gave the same word twice.")

