import random

from hangman_words import word_list
from hangman_art import stages, logo
from hangman_letters import eng_letters

lives = 6

print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in correct_letters and not guessed:
        print(f"You've already guessed {guess}")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in eng_letters:
        print("Please only input ENGLISH LETTERS!!!")
    if guess not in chosen_word and guess not in guessed:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    else:
        print(f"You've already guessed {guess}")
    if lives == 0:
        game_over = True

        print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")
    print("Word to guess: " + display)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
    guessed.append(guess)