import random

available_words = ["python", "java", "swift", "javascript", "kotlin", "Ruby", "typescript", "visualbasic"]
games_won = 0
games_lost = 0

while True:
    print("H A N G M A N")
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    user_choice = input().strip().lower()

    if user_choice == 'exit':
        break
    elif user_choice == 'results':
        print(f"You won: {games_won} times.")
        print(f"You lost: {games_lost} times.")
        continue
    elif user_choice != 'play':
        print("Invalid choice. Please choose 'play', 'results', or 'exit'.")
        continue

    random_words = random.choice(available_words)
    word_length = len(random_words)
    guessed_letters = set()
    attempts = 8


    while attempts > 0:
        word_display = ''.join([letter if letter in guessed_letters else '-' for letter in random_words])

        if word_display == random_words:
            print(word_display)
            print(f"You guessed the word {random_words}!")
            print("You survived!\n")
            games_won += 1
            break

        print(word_display)

        user_word = input("Input a letter: ")

        if ' ' in user_word:
            print("Please, input a single letter.")
            continue

        if not user_word:
            print("Please, input a single letter.")
            continue

        if user_word.islower():
            if len(user_word) == 1 and user_word.isalpha():
                if 'a' <= user_word <= 'z' and user_word.isascii():
                    if user_word in guessed_letters:
                        print("You've already guessed this letter.")
                    else:
                        guessed_letters.add(user_word)
                        if user_word in random_words:
                            for i in range(word_length):
                                if random_words[i] == user_word:
                                    word_display = word_display[:i] + user_word + word_display[i + 1:]
                        else:
                            print(f"That letter doesn't appear in the word.  # {attempts - 1} attempts")
                            attempts -= 1
                else:
                    print("Please, enter a lowercase letter from the English alphabet.")
            else:
                print("Please, input a single letter.")
        else:
            print("Please, enter a lowercase letter from the English alphabet.")
    else:
        print(f"\nYou lost! The word was: {random_words}\n")
        games_lost += 1

