import random

game_play = True

while game_play:
    difficulty_level = str.upper(input("please select preferred difficulty level (EASY or MEDIUM or HARD): "))
    difficulty_level_list = ["EASY", "MEDIUM", "HARD"]

    if difficulty_level == "EASY":
        secret_number = random.randint(1, 10)
        guess_count = 0
        guess_limit = 6
        guesses_left = 5
        guessing_range = range(11)

        while guess_count < guess_limit:
            try:
                guess = int(input("guess a number from 1-10: "))
                if guess == secret_number:
                    print("You got it right!")
                    game_play = False
                    break
                elif guess not in guessing_range:
                    print("Your response should be a number ranging from 1 to 10")
                    print(f"You have {guesses_left} guesses left")
                    guess_count += 1
                    guesses_left -= 1
                else:
                    print("That was wrong")
                    print(f"You have {guesses_left} guesses left")
                    guess_count += 1
                    guesses_left -= 1
            except ValueError:
                print("Invalid value, please enter an integer(a positive whole number)")
                print(f"You have {guesses_left} guesses left")
                guess_count += 1
                guesses_left -= 1
        else:
            print("Game over!")
            print(f"Correct answer is {secret_number}")
            game_play = False

    elif difficulty_level == "MEDIUM":
        secret_number = random.randint(1, 20)
        guess_count = 0
        guess_limit = 4
        guesses_left = 3
        guessing_range = range(21)

        while guess_count < guess_limit:
            try:
                guess = int(input("guess a number from 1-20: "))
                if guess == secret_number:
                    print("You got it right!")
                    game_play = False
                    break
                elif guess not in guessing_range:
                    print("Your response should be a number ranging from 1 to 20")
                    print(f"You have {guesses_left} guesses left")
                    guess_count += 1
                    guesses_left -= 1
                else:
                    print("That was wrong")
                    print(f"You have {guesses_left} guesses left")
                    guess_count += 1
                    guesses_left -= 1
            except ValueError:
                print("Invalid value, please enter an integer(a positive whole number)")
                print(f"You have {guesses_left} guesses left")
                guess_count += 1
                guesses_left -= 1
        else:
            print("Game over!")
            print(f"Correct answer is {secret_number}")
            game_play = False

    elif difficulty_level == "HARD":
        secret_number = random.randint(1, 50)
        guess_count = 0
        guess_limit = 3
        guesses_left = 2
        guessing_range = range(51)

        while guess_count < guess_limit:
            try:
                guess = int(input("guess a number from 1-50: "))
                if guess == secret_number:
                    print("You got it right!")
                    game_play = False
                    break
                elif guess not in guessing_range:
                    print("Your response should be a number ranging from 1 to 50")
                    print(f"You have {guesses_left} guesses left")
                    guess_count += 1
                    guesses_left -= 1
                else:
                    print("That was wrong")
                    print(f"You have {guesses_left} guesses left")
                    guess_count += 1
                    guesses_left -= 1
            except ValueError:
                print("Invalid value, please enter an integer(a positive whole number)")
                print(f"You have {guesses_left} guesses left")
                guess_count += 1
                guesses_left -= 1
        else:
            print("Game over!")
            print(f"Correct answer is {secret_number}")
            game_play = False

    elif difficulty_level not in difficulty_level_list:
        print("Invalid response. please type 'easy' to select EASY, 'medium' to select MEDIUM or 'hard' to select HARD")
