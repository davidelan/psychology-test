import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('psychology-test')

questionnaires = SHEET.worksheet('questionnaires')
descriptions = SHEET.worksheet('descriptions')

program_scope = f"{"A2"}:{"A14"}"
gad7_description = f"{"B2"}:{"B4"}"
sas20_description = f"{"B7"}:{"B10"}"

gad7_questions = f"{"A2"}:{"A8"}"
gad7_answers = f"{"B2"}:{"B5"}"
sas20_questions = f"{"C2"}:{"C21"}"
sas20_answers = f"{"D2"}:{"D5"}"

def get_name():
    """
    Gets name from terminal, validates the input and prints greeting
    using the name provided
    """
    while True:
        try:
            name = input("Please enter your name: ")

            if not name:
                raise ValueError("Name cannot be empty")

            if " " in name:
                raise ValueError("Name cannot contain spaces")

            if not name.isalpha():
                raise ValueError("Name can only contain letters")

            if len(name) > 20:
                raise ValueError("Name must be 20 characters or less")

            if not name[0].isupper():
                raise ValueError("Name must start with a capital letter")

            else:
                print("\n")
                print("Hello " + name + ", Welcome to our psychology-test for fun\n")
                break  # if name follows all rules, exit while loop

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


def main():
    """
    Run all program functions
    """
    # Gets name of user and displays greeting
    name = get_name()

    # Print Description and purpose of the Program (in Descriptions GoogleSheet)
    print_description(program_scope)
 
    

main()