# YuliaTarima_Chapter11_Assignment1

"""
This program simulates a Magic 8 Ball - a fortune-telling toy
that displays a random response to a 'yes or no' question.

The first part of the program creates a file named 8ball_responses.txt
with predefined phrases written to the file.

The second part of the program reads the responses
from the file into a list.

Then it prompts the user to ask a yes/no type question
and randomly displays one of the responses.
This repeats until the user is ready to quit.

 """

import random


def magic_8_ball():
    # Function to create the responses file from a list
    def create_responses_file():
        # list of responses to be fed into a file
        responses = [
            "Yes, of course!",
            "Without a doubt, yes.",
            "You can count on it.",
            "For sure!",
            "Ask me later!",
            "I'm not sure.",
            "I can't tell you right now.",
            "I'll tell you after my nap.",
            "No way!",
            "I don't think so.",
            "Without a doubt, no.",
            "The answer is clearly NO!"
        ]

        # write each list item into a file on a new line
        with open("8ball_responses.txt", "w") as file:
            for response in responses:
                file.write(response + "\n")

    # Function to read the responses from the file into a list
    def read_responses_file_into_list():
        with open("8ball_responses.txt", "r") as file:
            responses = file.read().splitlines()
        return responses

    # Create the responses file
    create_responses_file()

    # Load the responses into a list
    responses = read_responses_file_into_list()

    print("Welcome to the Magic 8 Ball!")

    while True:
        # Prompt the user for a yes/no question
        question = input(
            "Ask a yes/no question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            # Display a random response from the responses list
            print(f"{random.choice(responses)}\n")


# Execute the magic_8_ball function
magic_8_ball()
