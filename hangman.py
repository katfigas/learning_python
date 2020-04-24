import random
import sys

def print_game_state(secret_word, correct_indexes, letters_incorrect):
    for i in range(len(secret_word)):
        if i in correct_indexes:
            sys.stdout.write(secret_word[i] + " ")
        else:
            sys.stdout.write("_ ")
    sys.stdout.write("\n")
    sys.stdout.write("Nietrafione litery to: ")
    for letter in letters_incorrect:
        sys.stdout.write(letter + " ")
    sys.stdout.write("\n")
    print("Wykorzystana ilość szans: " + str(len(letters_incorrect)))

    sys.stdout.flush()


list_of_words = ['konstantynopol', 'domino', 'jajko', 'demokracja', 'filharmonia']

secret_word = random.choice(list_of_words)
word_found = False
hangman_finished = False
correct_indexes = []
letters_incorrect = []
while not (word_found or hangman_finished):
    print_game_state(secret_word, correct_indexes, letters_incorrect)
    letter = input("Podaj litere: ")
    if letter in secret_word:
        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                correct_indexes.append(i)

    if letter not in secret_word:
        letters_incorrect.append(letter)

    hangman_finished = len(letters_incorrect) >= 10
    word_found = len(correct_indexes) == len(secret_word)
if word_found:
    print("Gratulacje!")
else:
    print("Trudno, przegrałeś. ")

print_game_state(secret_word, correct_indexes, letters_incorrect)

