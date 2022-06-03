from random import choice
import json

filename = "magic_ball_answers.json"


def read_json():
    with open(filename, 'r') as file:
        data = json.load(file)
    return data["positive"], data["hesitantly positive"], data["neutral"], data["negative"]


def greetings():
    print("Hello World, I am a Magic ball and i know every answer that you could ask me.")
    global ask_name
    ask_name = str(input("Please enter your name: "))
    print(f"Hello, {ask_name.capitalize()}")


while True:
    def ask_question():
        str(input("Enter the question: "))
        answer_to_question = choice(choice(read_json()))
        print(answer_to_question)
        try_again = str(input(f"Would you like to ask again {ask_name.capitalize()}, input yes or no?\n"))
        if try_again == "yes":
            ask_question()
        else:
            print("Come back if you have any questions!")


    break

greetings()
ask_question()
