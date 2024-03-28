import gspread  # Python API for Google Sheets
from google.oauth2.service_account import Credentials
import re  # Regular expression operations
from colorama import init, Fore
import os  # to use clear screen cls
import sys  # to use clear screen cls
import time  # for slow typing


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('psychology-test')

# sales = SHEET.worksheet('questionnaires')
questionnaires = SHEET.worksheet('questionnaires')
descriptions = SHEET.worksheet('descriptions')

# position of descriptions of scope of the program in cells in GoogleSheet
program_scope = f"{"A2"}:{"A14"}"

# position of descriptions in cells in GoogleSheet
gad7_description = f"{"B2"}:{"B9"}"
sas20_description = f"{"B12"}:{"B18"}"

# position of questions and answers in cells in GoogleSheet
gad7_questions = f"{"A2"}:{"A8"}"
gad7_answers = f"{"B2"}:{"B5"}"
sas20_questions = f"{"C2"}:{"C21"}"
sas20_answers = f"{"D2"}:{"D5"}"

# position of scores in cells in GoogleSheet
gad7_score_1 = f"{"D4"}:{"D8"}"
gad7_score_2 = f"{"D10"}:{"D17"}"
gad7_score_3 = f"{"D19"}:{"D26"}"
gad7_score_4 = f"{"D28"}:{"D35"}"
sas20_score_1 = f"{"E4"}:{"E8"}"
sas20_score_2 = f"{"E10"}:{"E15"}"
sas20_score_3 = f"{"E17"}:{"E22"}"
sas20_score_4 = f"{"E24"}:{"E29"}"


# position of GAD-7 advices in cells in GoogleSheet
gad7_advice_1 = f"{"F4"}:{"F8"}"
gad7_advice_2 = f"{"F10"}:{"F15"}"
gad7_advice_3 = f"{"F17"}:{"F22"}"
gad7_advice_4 = f"{"F24"}:{"F30"}"

# position of SAS-20 advices in cells in GoogleSheet
sas20_advice_1 = f"{"G4"}:{"G8"}"
sas20_advice_2 = f"{"G10"}:{"G15"}"
sas20_advice_3 = f"{"G17"}:{"G23"}"
sas20_advice_4 = f"{"G25"}:{"G32"}"

# position of saved name on GoogleSheet
user_name = "A17"


# function for Slow Typing Instructions time.sleep 0.05
def type_print(text):
    """
    Slows down Typing Instructions time.sleep 0.05
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    # print('')


# function for (slower) Slow Typing Instructions time.sleep 0.3
def type_print_slow(text):
    """
    Slows down Typing Instructions time.sleep 0.3
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    print('')


def get_name():
    """
    Gets name from terminal, validates the input and prints greeting
    using the name provided
    """
    print("\n")

    while True:
        try:
            name = input("Please enter your name: ")
            if not name:  # no charachter entered
                raise ValueError("Name cannot be empty")

            if " " in name:  # name contains a space
                raise ValueError("Name cannot contain spaces")

            if not name.isalpha():  # name contains other than letters
                raise ValueError("Name can only contain letters")

            if len(name) > 20:  # name is longer than 20 characters
                raise ValueError("Name must be 20 characters or less")

            if not name[0].isupper():  # name must start with a capital letter
                raise ValueError("Name must start with a capital letter")

            else:
                os.system('clear')  # Clear Screen Command for Linux/OS X
                print("\n")
                type_print("Hello " + Fore.GREEN + name + Fore.RESET)
                type_print(", Welcome to our psychology-test for fun :-)")
                descriptions.update_acell(user_name, name)  # Update the cell
                break  # if name follows all rules, exit the while loop

        except ValueError as e:
            print(e)

    return name


def print_description(range):
    """
    Prints the chosen description specified in the passed value range
    Descriptions are contained in GoogleSheet "descriptions" and variables
    declared at the top of program.
    example: program_scope = f"{"A2"}:{"A13"}"
    """
    cell_values = descriptions.get(range)

    for row in cell_values:
        type_print_slow(row)
    print("\n")


def choose_questionnaire():
    """
    Chooses questionnaire between two options
    and calls function to prints
    chosen questionnaire description
    """
    while True:
        try:
            print("\n")
            type_print("Please choose a questionnaire:\n")
            print("\n")
            type_print("1. Questionnaire GAD-7. - 7 questions\n")
            print()
            type_print("2. Questionnaire SAS-20. - 20 questions\n")
            print("\n")
            choice = input("Enter 1 or 2: ")
            if choice in ['1']:
                os.system('clear')  # Clear Screen Command for Linux/OS X
                print("\n")
                type_print("You have chosen the questionnaire GAD-7\n")
                print("\n")
                # Prints the description of the GAD-7 questionnaire
                print_description(gad7_description)
                return choice
            if choice in ['2']:
                os.system('clear')  # Clear Screen Command for Linux/OS X
                print("\n")
                type_print("You have chosen the questionnaire SAS-20\n")
                print("\n")
                # Prints the description of the SAS-20 questionnaire
                print_description(sas20_description)
                return choice
            else:
                print("\n")
                raise ValueError("**** Invalid choice. Please enter 1 or 2.\n")
        except ValueError as e:
            print(e)


def run_questionnaire(choice):
    """
    Runs questionnaire: Dysplays questions and
    possible answers (a,b,c or d)
    """
    selections = []  # contains user selections

    if choice == "1":
        questions = questionnaires.get(gad7_questions)
        answers = questionnaires.get(gad7_answers)
        type_print("Over the last 2 weeks, ")
        type_print("how often have you been bothered by")
        type_print("the following problems?\n")

        for i in questions:
            # Prints the questions taken from the Google Sheet
            print()
            print(*i, "\n")  # The asterix doesn't print the []

            for x in answers:
                # Prints the options (a, b, c or d) for questions
                print(*x)

            print("\n")
            user_answer = input("Please enter your choice (a, b, c or d:) ")

            # Validate user's answer
            while user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Invalid answer. Please choose 'a', 'b', 'c', or 'd'.")
                print("Please enter your choice (a, b, c or d:) ", end=' ')
                user_answer = input()

            # Append user's answer to the list
            selections.append(user_answer)

            print("\n")
            os.system('clear')  # Clear Screen Command for Linux/OS X

    elif choice == "2":
        questions = questionnaires.get(sas20_questions)
        answers = questionnaires.get(sas20_answers)

        type_print("For each item below, ")
        type_print("please check the statement which best describes\n")
        type_print("how often you felt or behaved this way ")
        type_print("during the past several days.\n")

        for i in questions:
            print()
            print(*i, "\n")  # The asterix doesn't print the []

            for x in answers:
                print(*x)

            print("\n")
            user_answer = input("Please enter your choice (a, b, c or d:) ")

            # Validate user's answer
            while user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Invalid answer. Please choose 'a', 'b', 'c', or 'd'.")
                print("Please enter your choice (a, b, c or d:) ", end=' ')
                user_answer = input()

            # Append user's answer to the list
            selections.append(user_answer)

            print("\n")
            os.system('clear')  # Clear Screen Command for Linux/OS X

    else:
        print("An error has occured, the program terminates here. Bye\n")
        exit()
    return selections


def calculate_score(selection, score):
    """
    Calculates and displays score
    based on user answers
    """
    if selection == "1":
        result = calculate_gad7_score(score)
        print()
        print("In the GAD-7 questionnaire you have scored: ", result)
        print()
        print_gad7_results(result)
    elif selection == "2":
        result = calculate_sas20_score(score)
        print()
        print("In the SAS-20 questionnaire you have scored: ", result)
        print()
        print_sas20_results(result)
    else:
        print("An error has occured, the program terminates here. Bye\n")
        exit()

    return result


def calculate_gad7_score(score):
    """
    Calculates score specifically
    for GAD-7 questionnaire
    """
    # Dictionary to map answer options to scores
    answer_scores = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    # Calculate total score
    total_score = sum(answer_scores[answer] for answer in score)
    return total_score


def calculate_sas20_score(score):
    """
    Calculates score specifically
    for SAS-20 questionnaire
    """
    # Dictionary to map answer options to scores
    answer_scores = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # Calculate total score
    total_score = sum(answer_scores[answer] for answer in score)
    return total_score


def print_gad7_results(total_score):
    """
    Prints score specifically
    for GAD-7 questionnaire
    """
    if total_score >= 0 and total_score <= 4:
        print_description(gad7_score_1)
    elif total_score >= 5 and total_score <= 9:
        print_description(gad7_score_2)
    elif total_score >= 10 and total_score <= 14:
        print_description(gad7_score_3)
    elif total_score >= 15 and total_score <= 21:
        print_description(gad7_score_4)
    else:
        print("Invalid total score")


def print_sas20_results(total_score):
    """
    Prints score specifically
    for SAS-20 questionnaire
    """
    if total_score >= 1 and total_score < 45:
        print_description(sas20_score_1)
    elif total_score >= 45 and total_score < 60:
        print_description(sas20_score_2)
    elif total_score >= 60 and total_score < 74:
        print_description(sas20_score_3)
    elif total_score >= 75 and total_score <= 80:
        print_description(sas20_score_4)
    else:
        print("Invalid total score")


def advise(selection, total_score):
    """
    Asks user if they want to see
    a professional advice based on
    their results
    """
    print()
    while True:
        print("Would you like to get a NON PROFESSIONAL advice ", end=' ')
        print("according to your results? (yes/no): ", end=' ')
        answer = input().lower()
        if answer == "yes":

            if selection == "1":
                print_gad7_advice(total_score)
                break
            elif selection == "2":
                print_sas20_advice(total_score)
                break
            else:
                print("An error has occured, program terminates here. Bye\n")
                exit()
        elif answer == "no":
            print("\n")
            type_print("Thank you for taking part in our psychological test.")
            print("\n")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def print_gad7_advice(total_score):
    """
    Prints advice specifically
    for GAD-7 questionnaire
    """
    if total_score >= 0 and total_score <= 4:
        print()
        print_description(gad7_advice_1)
    elif total_score >= 5 and total_score <= 9:
        print()
        print_description(gad7_advice_2)
    elif total_score >= 10 and total_score <= 14:
        print()
        print_description(gad7_advice_3)
    elif total_score >= 15 and total_score <= 21:
        print()
        print_description(gad7_advice_4)
    else:
        print("Invalid total score")


def print_sas20_advice(total_score):
    """
    Prints advice specifically
    for SAS-20 questionnaire
    """
    if total_score >= 1 and total_score < 45:
        print()
        print_description(sas20_advice_1)

    elif total_score >= 45 and total_score < 60:
        print()
        print_description(sas20_advice_2)

    elif total_score >= 60 and total_score < 74:
        print()
        print_description(sas20_advice_3)

    elif total_score >= 75 and total_score <= 80:
        print()
        print_description(sas20_advice_4)

    else:
        print("Invalid total score")


def re_run_main():
    """
    Asks user if they want
    to retake one of the questionnaires
    """
    run = True

    while run:
        print("Would you like to re-take one of the ", end=' ')
        print("psychological tests? (yes/no): ", end=' ')
        answer = input().lower()
        if answer == "yes":
            os.system('clear')  # Clear Screen Command for Linux/OS X
            run = False
            main("Second time")
        elif answer == "no":
            name = descriptions.acell(user_name).value
            print("\n")
            type_print(Fore.YELLOW + "Thank you " + Fore.GREEN + name)
            type_print(Fore.YELLOW + " for taking part ")
            type_print("in our psychological test. Goodbye")
            type_print(Fore.RESET)

            print("\n")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main(condition):
    """
    Run all program functions
    """

    if condition == "First time":

        init()  # Initialisation for colorama import

        print("\n")
        type_print(Fore.YELLOW + "Welcome to our psychology-test for fun! :-)")
        type_print(Fore.RESET)
        print("\n")

        # Print Description and purpose
        # of the Program (in Descriptions GoogleSheet)
        print_description(program_scope)

        # Gets name of user and displays greeting
        name = get_name()
    elif condition == "Second time":
        name = descriptions.acell(user_name).value
        print("\n")
        type_print("Hello " + Fore.GREEN + name + Fore.RESET)
        type_print(", Welcome back to our psychology-test for fun\n")

    selection = choose_questionnaire()

    score = run_questionnaire(selection)

    # calculate_score(selection, score)
    total_score = calculate_score(selection, score)

    advise(selection, total_score)

    re_run_main()


main("First time")
