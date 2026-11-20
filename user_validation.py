def validation_for_yes_no(prompt):
    """validates user input by a while loop that only exits when the user gives yes or no.
    
    Input: the prompt question for the user to type yes or no.
    Output: "yes" or "no".
    Side effects: none
    """
    while True:
        answer = input(prompt).lower()
        if answer == "yes" or answer == "no":
            return answer
        print("Please type 'yes' or 'no'.")


def validation_for_choice(prompt, choices):
    """validates user input by a while loop that only exits when the user gives a valid choice.
        
    Input: the prompt question for the user to choose between a given amount of choices.
    Output: one of the available choices.
    Side effects: none
    """
    while True:
        answer = input(prompt).lower()
        if answer in choices:
            return answer
        print(f"Please choose one of the valid choices.")


def validation_for_int(prompt):
    """validates user input by a while loop that only exits when the user gives an integer.
    
    Input: the prompt question for the user to enter an integer.
    Output: the user's answer as an integer.
    Side effects: none
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")