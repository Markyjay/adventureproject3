import gspread
from google.oauth2.service_account import Credentials

import time
import os


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
escape_holding_cell = story.acell('A3').value
realization_cell = story.acell('A4').value
initial_descision_cell = story.acell('A5').value
spikes_cell = story.acell('B1').value
return_cell = story.acell('B2').value
downhill_cell = story.acell('B3').value
junction_cell = story.acell('B4').value
river_cell = story.acell('B5').value
initial_forest_cell = story.acell('B6').value
goback_cell = story.acell('B7').value
ignore_cell = story.acell('C1').value
hide_cell = story.acell('C2').value
tend_wound_cell = story.acell('C3').value
light_cell = story.acell('C4').value
car_death1_cell = story.acell('C5').value
inside_truck_cell = story.acell('C6').value
gun_death2_cell = story.acell('C7').value
initial_gate_cell = story.acell('D1').value
pass_gate_cell = story.acell('D2').value
forest_cell = story.acell('D3').value
hide2_cell = story.acell('D4').value
hide_in_truck_cell = story.acell('D5').value
death1_cell = story.acell('D6').value
truck_pass_cell = story.acell('D7').value
no_tend_wound_cell = story.acell('E1').value
bridge_cell = story.acell('E2').value
rock_cell = story.acell('E3').value
fence_opening_cell = story.acell('E4').value
cold_death_cell = story.acell('E5').value
racoon_scare_cell = story.acell('E6').value
move_on2_cell = story.acell('E7').value
inside_gate_cell = story.acell('E8').value
car_death2_cell = story.acell('F1').value
gun_death1_cell = story.acell('F2').value
bridge_jump_cell = story.acell('F3').value
car_death3_cell = story.acell('F4').value
weapon_cell = story.acell('F5').value
hide2_cell = story.acell('F6').value
retrieve_knife_cell = story.acell('F7').value
move_on_cell = story.acell('F8').value
wait_cell = story.acell('G1').value
retreat_cell = story.acell('G2').value
climb_down_cell = story.acell('G3').value
skip_yard_cell = story.acell('G4').value
car_death4_cell = story.acell('G5').value
forest2_cell = story.acell('G6').value
car_engine_cell = story.acell('G7').value
turnback_cell = story.acell('G8').value
car_death5_cell = story.acell('H1').value
creep_cell = story.acell('H2').value
hunters_cell = story.acell('H3').value
victory_cell = story.acell('H4').value
go4_exit_cell = story.acell('H5').value



print("Would you like to start your adventure? (y/n): ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
                retry = input("Do you want to retry? (y/n): ").lower()
                if retry == "y":
                    start_adventure()
                elif retry == "n": 
                    print("That's too bad, maybe another time")
                else:
                    print("Incorrect input try again")
                    retry = input("Do you want to retry? (y/n): ").lower()
                return

    clear_screen()
    print(escape_holding_cell)
    time.sleep(2)
    print(realization_cell) 
    
    while True:
        choice = input("Type 'c' to continue or 'x' to exit: ").lower()
        if choice == 'c':
            clear_screen()
            print(initial_descision_cell)
            while True:
                choice_1 = input("Type 'l' to go left toward river, 'f' to go forward or 'r' to go right in to the forest: ").lower() 
                if choice_1 == 'l':
                    clear_screen()
                    print(junction_cell)
                    while True:
                        choice_1_a = input("Type '1' to take road 1, '2' to take road 2 or '3' to take road 3: ").lower()
                        if choice_1_a == '1':
                            clear_screen()
                            print(downhill_cell)
                            while True:
                                choice_2_a = input("Type 't' to tend wound or 'w' to limp your way to the water: ").lower()
                                if choice_2_a == 't':
                                    clear_screen()
                                    print(tend_wound_cell)
                                elif choice_2_a == 'w':
                                    clear_screen()
                                    print(no_tend_wound_cell)
                                else: 
                                    print("Invalid input. Please type 'f' to go forward or 'l' to go to the river: ")
                                
                        elif choice_1_a == '2':
                            clear_screen()
                            print(light_cell)
                        elif choice_1_a == '3':
                            clear_screen
                            print(forest_cell)
                elif choice_1 == 'f':
                    clear_screen()
                    print(initial_forest_cell)
                    while True:
                        choice_1_b == input("Type 'f' to go forward or 'b' to go back: ").lower()
                        if choice_1_b == 'f':
                            clear_screen()
                            print(spikes_cell)
                            print(return_cell)
                            while True:
                                choice_death = input("Type 's' to return to the beginning: ").lower()
                                if choice_death == 's':
                                    start_adventure()
                                else: 
                                    print("Invalid input. Please type 's' to return to the beginning: ")
                        elif choice_1_b == 'b':
                            clear_screen()
                            print(goback_cell) 
                            while True:
                                choice_1_ba == input("Type 'f' to go forward or 'l' to go to the river: ").lower()
                                if choice_1_ba == 'f':
                                    clear_screen()
                                    print(junction_cell)
                                elif choice_1_ba == 'l':
                                    clear_screen()
                                    print(river_cell)
                                else: 
                                    print("Invalid input. Please type 'f' to go forward or 'l' to go to the river: ")
                                
                elif choice_1 == 'r':
                    clear_screen()
                    print(river_cell)
                    while True:
                        choice_1_c == input("Type 'h' to hide or 'c' to take your chances with the car: ").lower()
                        if choice_1_c == 'h':
                            clear_screen()
                            print(hide2_cell)
                        elif choice_1_c == 'c':
                            clear_screen()
                            print(car_death1_cell)
                            while True:
                                choice_death = input("Type 's' to return to the beginning: ").lower()
                                if choice_death == 's':
                                    start_adventure()
                                else: 
                                    print("Invalid input. Please type 's' to return to the beginning: ")
                else:
                    print("Invalid input. Please type 'l', 'f' or 'r'.")
            break
        elif choice == 'x':
            print("You lie down and wait for death. Game Over!")
            return
        else:
            print("Invalid input. Please type 'c' or 'x'.")


start_choice = input().lower()

if start_choice == "y":
    player_name = get_name()
    start_adventure()
elif start_choice == "n":
    print("That's too bad, maybe another time.")
else:
    print("Invalid choice. Please enter 'y' or 'n'.")