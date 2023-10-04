import gspread
from google.oauth2.service_account import Credentials

import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('adventure_sheet')

story = SHEET.worksheet('story1')

introduction_cell = story.acell('A1').value
escape_code_cell = story.acell('A2').value
realization_cell = story.acell('A3').value
goback_cell = story.acell('B1').value
goforward_cell = story.acell('C1').value
goleft_cell = story.acell('D1').value
goright_cell = story.acell('E1').value


print("Would you like to start your adventure? (y/n): ")

def get_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("Invalid name. Please enter only letters for your name.")

def generate_escape_code(name):
    name = name.lower()
    last_letter = name[-1]
    num_letters = len(name)
    alpha_name = ''.join(sorted(name))
    second_letter = alpha_name[1]
    escape_code = f"{last_letter}{num_letters}{second_letter}"
    return escape_code

def start_adventure():
    print("\nWelcome to your adventure {}!".format(player_name))
    time.sleep(1)
    print("Make your choices by typing the value diplayed in brackets.")
    time.sleep(1)
    print(introduction_cell)
    time.sleep(2)
    print(escape_code_cell)
    time.sleep(2)

    escape_code = generate_escape_code(player_name)
    
    code_attempts = 3
    while code_attempts > 0:
        user_code = input("Enter the code to escape: ")
        if user_code == escape_code:
            print("Congratulations! You've successfully escaped the room.")
            break
        else:
            code_attempts -= 1
            if code_attempts > 0:
                print(f"Incorrect code. You have {code_attempts} attempts left.")
            else:
                print("Sorry, you've run out of attempts. The room remains locked.")
                break

    print(realization_cell)   

start_choice = input().lower()

if start_choice == "y":
    player_name = get_name()
    start_adventure()
elif start_choice == "n":
    print("That's too bad, maybe another time.")
else:
    print("Invalid choice. Please enter 'y' or 'n'.")