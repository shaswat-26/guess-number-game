import random

def play_num_guessing_game():
    secret_num = random.randint(1, 100)
    guesses_left = 7
    
    print("Welcome to the game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have a maximum of 7 chances. Play smart!")

    while guesses_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if guess < secret_num:
            print("Too low, try again!")
        elif guess > secret_num:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed it right!")
            break
        
        guesses_left -= 1
        print(f"You have {guesses_left} guesses left.")
    
    if guesses_left == 0:
        print("Game over! You ran out of guesses.")
        print(f"The correct number was: {secret_num}")

play_num_guessing_game()
