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
SHEET = GSPREAD_CLIENT.open('adventure_sheet')

story = SHEET.worksheet('story1')

data = story.get_all_values()

print("Would you like to start your adventure? (yes/no): ")

def get_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("Invalid name. Please enter only letters for your name.")

def start_adventure():
    print("\nWelcome to your adventure, {}!".format(player_name))


start_choice = input().lower()

if start_choice == "yes":
    player_name = get_name()
    start_adventure()
elif start_choice == "no":
    print("That's too bad, maybe another time.")
else:
    print("Invalid choice. Please enter 'yes' or 'no'.")