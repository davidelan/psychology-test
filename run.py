import gspread
from google.oauth2.service_account import Credentials
import re #Regular expression operations
#from colorama import Fore # for producing colored terminal text and cursor positioning
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('psychology-test')

#sales = SHEET.worksheet('questionnaires')
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
gad7_score = f"{"C2"}:{"C7"}"
sas20_score = f"{"C9"}:{"C14"}"

# position of GAD-7 advices in cells in GoogleSheet
gad7_advice_1 = f"{"C2"}:{"C7"}"
gad7_advice_2 = f"{"C2"}:{"C7"}"
gad7_advice_3 = f"{"C2"}:{"C7"}"
gad7_advice_4 = f"{"C2"}:{"C7"}"

# position of SAS-20 advices in cells in GoogleSheet
sas20_advice_1 = f"{"C2"}:{"C7"}"
sas20_advice_2 = f"{"C2"}:{"C7"}"
sas20_advice_3 = f"{"C2"}:{"C7"}"
sas20_advice_4 = f"{"C2"}:{"C7"}"

    
def get_name():
    """
    Gets name from terminal, validates the input and prints greeting
    using the name provided
    """
    print("\n")

    while True:
        try:
            name = input("Please enter your name: ")

            if not name: # error if no charachter entered
                raise ValueError("Name cannot be empty")

            if " " in name: # error if name contains a space
                raise ValueError("Name cannot contain spaces")

            if not name.isalpha(): # error if name contains characters other than letters
                raise ValueError("Name can only contain letters")

            if len(name) > 20: # error if name is longer than 20 characters
                raise ValueError("Name must be 20 characters or less")

            if not name[0].isupper(): # error if name doesn't start with a capital letter
                raise ValueError("Name must start with a capital letter")

            else:
                print("\n")
                print("Hello " + name + ", Welcome to our psychology-test for fun\n")
                break  # if name follows all rules, exit the while loop

        except ValueError as e:
            print(e)

    return name


def print_description(range):
    """
    Prints the chosen description specified in the passed value range
    Descriptions are contained in GoogleSheet "descriptions" and variables declared 
    at the top of program. 
    example: program_scope = f"{"A2"}:{"A13"}"
    """
    cell_values = descriptions.get(range)

    for row in cell_values:
        print(*row) # The asterix only selects the content and doesn't print the []

    print("\n")



def choose_questionnaire():
    
        while True:
            try:
                print("Please choose a questionnaire:\n")
                print("1. Questionnaire GAD-7. - 7 questions")
                print("2. Questionnaire SAS-20. - 20 questions\n")
                #print("\n")
                choice = input("Enter 1 or 2: ")
                
                if choice in ['1']:
                    os.system('clear')  # Clear Screen For Linux/OS X
                    print("\n")
                    print("You have chosen the questionnaire GAD-7\n")
                    print_description(gad7_description) # Prints the description of the GAD-7 questionnaire
                    return choice           
                if choice in ['2']:
                    os.system('clear')  # Clear Screen For Linux/OS X
                    print("\n")
                    print("You have chosen the questionnaire SAS-20\n")
                    print_description(sas20_description) # Prints the description of the SAS-20 questionnaire
                    return choice
                else:
                    print("\n")
                    raise ValueError("******* Invalid choice. Please enter 1 or 2.\n")
            except ValueError as e:
                print(e)

def run_questionnaire(choice):

    selections = []

    if choice == "1":
        questions = questionnaires.get(gad7_questions)
        answers = questionnaires.get(gad7_answers)
        #print(cell_values)

        print("Over the last 2 weeks, how often have you been bothered by the following problems?\n")

        
        for i in questions:
            print()
            print(*i, "\n") # The asterix only selects the content and doesn't print the []


            for x in answers:
                print(*x)

            print("\n")
            user_answer = input("Please enter your choice (a, b, c or d:) ")

            # Validate user's answer
            while user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Invalid answer. Please choose 'a', 'b', 'c', or 'd'.")
                user_answer = input("Please enter your choice (a, b, c or d:) ")

            # Append user's answer to the list
            selections.append(user_answer)

            print("\n")
            os.system('clear')  # Clear Screen For Linux/OS X
            #print("this is colums: " + str(columns))
            print("\nYour answers:", selections)

        

    elif choice == "2":
        questions = questionnaires.get(sas20_questions)
        answers = questionnaires.get(sas20_answers)
        #print(cell_values)

        print("For each item below, please check the column which best describes")
        print("how often you felt or behaved this way during the past several days.\n")

        for i in questions:
            print(*i, "\n") # The asterix only selects the content and doesn't print the []

            for x in answers:
                print(*x)

            print("\n")
            user_answer = input("Please enter your choice (a, b, c or d:) ")


            # Validate user's answer
            while user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Invalid answer. Please choose 'a', 'b', 'c', or 'd'.")
                user_answer = input("Please enter your choice (a, b, c or d:) ")

            # Append user's answer to the list
            selections.append(user_answer)

            print("\n")
            os.system('clear')  # Clear Screen For Linux/OS X
            #print("this is colums: " + str(columns))
            print("\nYour answers:", selections)

    else:
        print("An error has occured, the program terminates here. Bye\n")  
        exit() 

    return selections


def calculate_score(selection, score):
    if selection == "1":
        result = calculate_gad7_score(score)
        print()
        print("In the GAD-7 questionnaire you have scored: ", result)
        print()
        #print_description(gad7_score)
        print()
        print_gad7_results(result)
    elif selection == "2":
        result = calculate_sas20_score(score)
        print()
        print("In the SAS-20 questionnaire you have scored: ", result)
        print()
        #print_description(sas20_score)
        print()
        print_sas20_results(result)
    else:
        print("An error has occured, the program terminates here. Bye\n")  
        exit()

    return result



def main():
    """
    Run all program functions
    """
    # Gets name of user and displays greeting
    #name = get_name()

    # Print Description and purpose of the Program (in Descriptions GoogleSheet)
    print_description(program_scope) 

  
    selection = choose_questionnaire()
    print(selection)

    score = run_questionnaire(selection)
    print("\n")
    print(score)

    calculate_score(selection, score)
  
    


main()


    #os.system('cls')  # For Windows
    #os.system('clear')  # For Linux/OS X


