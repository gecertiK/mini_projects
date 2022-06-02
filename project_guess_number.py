# guess number

from random import randint
from num2words import num2words

greetings_and_rules = """Welcome to the game "Guess number"!
Instruction:
Our program guess the number.
You should guess that number.\n"""
print(greetings_and_rules)

def repeat_the_game():
    question = input("Would you like to repeat the game write yes or no?\n")
    if question == "yes":
        guees_number()
    else:
        print("Good luck!")


def guees_number():
    n = int(input("Please enter the range from 1 to n\n"))
    random_value = randint(1, n)
    print(random_value)
    print("Please input number from 1 to 100\n")
    count = 0
    while True:
        try:
            person_var = int(input())
            if person_var > random_value:
                print("Your number is bigger hidden number, try it one more time.")
                count += 1
            elif person_var < random_value:
                print("Your number is lower hidden number, try it one more time.")
                count += 1
            else:
                print("Yeah, you guessed the number, congratulations!")
                count += 1
                if count == 1:
                    print(f"It took you {num2words(count)} attempt.")
                    repeat_the_game()
                    break
                else:
                    print(f"It took you {num2words(count)} attempts.")
                    repeat_the_game()
                    break
        except ValueError:
            print("Please enter the number from 1 to 100?")


guees_number()
