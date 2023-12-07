import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # chooses any word randomly from the list
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # keping track of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # keeping track of letters what user has gussed
    lives = len(word_letters) + 2

    while len(word_letters) > 0 and lives > 0:
        # what current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word :", " ".join(word_list))
        # letters used
        print(
            f"You have {lives} lives left and You have used the letters :",
            " ".join(used_letters),
        )
        user_letter = input("Guess the letter :").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # takes away a life if wrong
                print("\nYour letter,", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print("You have already used this letter.Please type another letter")

        else:
            print("Invalid character. Please try again")
        # gets when the length of word_letters == 0 or when lives == 0
    if lives == 0:
        print("Sorry,You died! The word was ", word)
    else:
        print("You have gussed the word ", word, "!!")


if __name__ == "__main__":
    hangman()
