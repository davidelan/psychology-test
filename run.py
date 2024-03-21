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

#sales = SHEET.worksheet('sales')

#data = sales.get_all_values()

#print(data)

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


def main():
    """
    Run all program functions
    """
    name = get_name()
 
    

main()