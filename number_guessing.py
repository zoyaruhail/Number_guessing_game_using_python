import random
def guessing():
    print("Welcome to the Number Guessing Game !!")
    score = 0
    comp_score = 0
    while True:
        try:
            menu = int(input("Menu \n1. Start \n2. exit\nChoose from the Menu: "))
            if menu == 1:
                while True:
                    num = random.randint(0,10)
                    num1 = int(input("Guess the number from 0 - 10: "))
                    if num == num1:
                        score += 1
                        comp_score += 0
                        print(f"Wohooooo! Correct Guess you got a score!\n Your guess: {num1} || Computer Guess: {num}\nYour Score = {score} || Computer Score = {comp_score}")
                    else:
                        score += 0
                        comp_score += 1
                        print(f"Oppsie! Better luck next time :( Computer gets the score!\n Your guess: {num1} || Computer Guess: {num}\nYour Score = {score} || Computer Score = {comp_score}")
                    again = input("Do you want to play again?? (y/n): ").lower()
                    if again != 'y':
                        break
            elif menu == 2:
                print(f"Thank You For Playing the Game !\nFinal Scores \nYour Score = {score} || Computer Score = {comp_score}")
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Enter the required output")


guessing()
