from random import randint

logo = """
 __    __                          __                                   ______                                          __                             ______                                    
/  \  /  |                        /  |                                 /      \                                        /  |                           /      \                                   
$$  \ $$ | __    __  _____  ____  $$ |____    ______    ______        /$$$$$$  | __    __   ______    _______  _______ $$/  _______    ______        /$$$$$$  |  ______   _____  ____    ______  
$$$  \$$ |/  |  /  |/     \/    \ $$      \  /      \  /      \       $$ | _$$/ /  |  /  | /      \  /       |/       |/  |/       \  /      \       $$ | _$$/  /      \ /     \/    \  /      \ 
$$$$  $$ |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      $$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/ $$ |$$$$$$$  |/$$$$$$  |      $$ |/    | $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |
$$ $$ $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$ |$$$$ |$$ |  $$ |$$    $$ |$$      \$$      \ $$ |$$ |  $$ |$$ |  $$ |      $$ |$$$$ | /    $$ |$$ | $$ | $$ |$$    $$ |
$$ |$$$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |            $$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  |$$ |$$ |  $$ |$$ \__$$ |      $$ \__$$ |/$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/ 
$$ | $$$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |            $$    $$/ $$    $$/ $$       |/     $$//     $$/ $$ |$$ |  $$ |$$    $$ |      $$    $$/ $$    $$ |$$ | $$ | $$ |$$       |
$$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/              $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/  $$/ $$/   $$/  $$$$$$$ |       $$$$$$/   $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ 
                                                                                                                                     /  \__$$ |                                                  
                                                                                                                                     $$    $$/                                                   
                                                                                                                                      $$$$$$/                                                    
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty level. Please restart the game and choose 'easy' or 'hard'.")
    exit()
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1
if attempts == 0:
    print(f"You've run out of guesses, you lose. The number was {number}.")
# End of the game
print("Thanks for playing!")