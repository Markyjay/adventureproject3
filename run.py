'''
A free python adventure game for those willing to take on a harrowing challenge.
Author: Mark Young 
'''

import gspread
import time
import pyfiglet
import os
import colorama
from colorama import Fore
from google.oauth2.service_account import Credentials
colorama.init(autoreset=True)


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


cell_names = [
    'A1', 'A2', 'A3', 'A4', 'A5', 'A6',
    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
    'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
]


cell_values = {cell_name: story.acell(cell_name).value for cell_name in cell_names}




def clear_screen():
    '''
    Clears terminal.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def get_name():
    '''
    Get the username input from the user
    Run a while loop to collect a valid alpha username of data from user
    via the terminal. The loop will repeatedly request data, until it is valid
    When the username is valid, then the start adventure function will be called.
    '''
    while True:
        name = input("What is your name?\n")
        if name.isalpha():
            return name
        else:
            print("Invalid name. Please enter only letters for your name.")


def generate_escape_code(name):
    '''
    Generates a code that is created from the valid name that the user inputs.
    '''
    name = name.lower()
    last_letter = name[-1]
    num_letters = len(name)
    alpha_name = ''.join(sorted(name))
    second_letter = alpha_name[1]
    escape_code = f"{last_letter}{num_letters}{second_letter}"
    return escape_code


def start_adventure():
    '''
    Begins the adventure story to the point of escape using the code.
    The user has three attempts to correctly identify the correct code created from their name.
    '''
    print("\nWelcome to your adventure {}!".format(player_name))
    time.sleep(1)
    print(cell_values['A1'])
    time.sleep(2)
    print(cell_values['A2'])
    time.sleep(2)
    escape_code = generate_escape_code(player_name)
    code_attempts = 3
    while code_attempts > 0:
        user_code = input("Enter the code to escape: ")
        if user_code == escape_code:
            print("Congratulations! You've successfully escaped the room.")
            main()
        else:
            code_attempts -= 1
            if code_attempts > 0:
                print(f"Incorrect code. You have {code_attempts} attempts left.")
            else:
                print("Sorry, you've run out of attempts. The room remains locked.")
                retry = input("Do you want to retry? (y/n):\n").lower()
                if retry == "y":
                    start_adventure()
                elif retry == "n":
                    print("That's too bad, maybe another time")
                else:
                    print("Incorrect input try again")


def main():
    '''
    Main story line function. Scene split into manageable functions.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    clear_screen()
    print(cell_values['A3'])
    time.sleep(2)
    print(cell_values['A4'])
    while True:
        choice_cx = input("Type 'c' to continue or 'x' to exit:\n").lower()
        if choice_cx == 'c':
            clear_screen()
            print(cell_values['A5'])
            while True:
                choice_lfr = input("Type 'l' to go left toward river, 'f' to go forward or 'r' to go right in to the forest:\n").lower()
                if choice_lfr == 'f':
                    clear_screen()
                    junction_loop()
                elif choice_lfr == 'r':
                    clear_screen()
                    print(cell_values['B6'])
                    while True:
                        choice_fb = input("Type 'f' to go forward or 'b' to go back:\n").lower()
                        if choice_fb == 'f':
                            clear_screen()
                            print(cell_values['B1'])
                            start_again_loop()
                        elif choice_fb == 'b':
                            clear_screen()
                            print(cell_values['B7'])
                            while True:
                                choice_fl = input("Type 'f' to go forward or 'l' to go to the river:\n").lower()
                                if choice_fl == 'f':
                                    clear_screen()
                                    junction_loop()
                                elif choice_fl == 'l':
                                    clear_screen()
                                    river_loop()
                                else:
                                    print("Invalid input. Try again!")
                elif choice_lfr == 'l':
                    clear_screen()
                    print(cell_values['B5'])
                    river_loop()
                else:
                    print("Invalid input. Try again! ")
        elif choice_cx == 'x':
            print("You lie down and wait for death. Game Over!")
            start_adventure()
        else:
            print("Invalid input. Try again!")


def start_again_loop():
    '''
    A loop function that can be used thoughout the code to restart the adventure in cases of failure to survive.
    '''
    while True:
        start_again = input("Type 's' to start another path:\n").lower()
        if start_again == 's':
            clear_screen()
            start_adventure()
        else:
            print("Invalid input. Try again!")


def junction_loop():
    '''
    As the Juction scenario occurs multiple times in the story a function containing 
    all possible paths from the junction scene is created for easier referral.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['B4'])
    while True:
        choice_123 = input("Type '1', '2' or '3':\n").lower()
        if choice_123 == '1':
            clear_screen()
            print(cell_values['B3'])
            while True:
                choice_tw = input("Type 't' to tend wound or 'w' to limp to the water:\n").lower()
                if choice_tw == 't':
                    clear_screen()
                    print(cell_values['C3'])
                    while True:
                        choice_hc = input("Type 'h' to hide or 'c' to ignore and continue:\n").lower()
                        if choice_hc == 'h':
                            clear_screen()
                            print(cell_values['C2'])
                            while True:
                                choice_sr = input("Type 's' to stay or 'r' to run:\n").lower()
                                if choice_sr == 's':
                                    clear_screen()
                                    print(cell_values['F1'])
                                    start_again_loop()
                                elif choice_sr == 'r':
                                    clear_screen()
                                    print(cell_values['C1'])
                                    while True:
                                        continue_forward = input("Type 'c' to continue forward:\n").lower()
                                        if continue_forward == 'c':
                                            clear_screen()
                                            bridge_loop()
                                else:
                                    print("Invalid input. Try again!")
                        elif choice_hc == 'c':
                            clear_screen()
                            print(cell_values['C1'])
                            while True:
                                choice_c1 = input("Type 'c' to continue:\n").lower()
                                if choice_c1 == 'c':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
                elif choice_tw == 'w':
                    clear_screen()
                    print(cell_values['E1'])
                    while True:
                        continue_forward = input("Type 'c' to continue forward:\n").lower()
                        if continue_forward == 'c':
                            clear_screen()
                            bridge_loop()
                        else:
                            print("Invalid input. Try again!")
                else:
                    print("Invalid input. Try again!")
        elif choice_123 == '2':
            clear_screen()
            print(cell_values['C4'])
            while True:
                choice_gr = input("Type 'g' to enter gate or 'r' to pass and continue down the road:\n").lower()
                if choice_gr == 'g':
                    clear_screen()
                    initial_gate_loop()
                elif choice_gr == 'r':
                    clear_screen()
                    print(cell_values['D2'])
                    while True:
                        choice_gd = input("Type 'g' to go back to gate or 'd' to go further into darkness:\n").lower()
                        if choice_gd == 'g':
                            clear_screen()
                            initial_gate_loop()
                        elif choice_gd == 'd':
                            clear_screen()
                            print(cell_values['E5'])
                            start_again_loop()
                        else:
                            print("Invalid input. Try again!")
                else:
                    print("Invalid input. Try again!")
        elif choice_123 == '3':
            clear_screen()
            print(cell_values['D3'])
            while True:
                choice_iq = input("Type 'i' to investigate or 'q' to move on quickly:\n").lower()
                if choice_iq == 'i':
                    clear_screen()
                    print(cell_values['E6'])
                    while True:
                        choice_cm = input("Type 'c' to climb down or 'm' to move on:\n").lower()
                        if choice_cm == 'c':
                            clear_screen()
                            print(cell_values['F7'])
                            start_again_loop()
                        elif choice_cm == 'm':
                            clear_screen()
                            move_on_loop()
                        else:
                            print("Invalid Input. Try again!")
                elif choice_iq == 'q':
                    clear_screen()
                    move_on_loop()
                else:
                    print("Invalid Input. Try again!")
        else:
            print("Invalid input. Try again!")


def initial_gate_loop():
    '''
    As the initial gate scenario occurs multiple times in the story a function containing 
    all possible paths from the gate scene is created for easier referral throughout the code.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['D1'])
    while True:
        choice_la = input("Type 'l' to open lock or 'a' to find another way:\n").lower()
        if choice_la == 'l':
            clear_screen()
            print(cell_values['E3'])
            while True:
                choice_rc = input("Type 'r' to use rock or 'c' to continue searching:\n").lower()
                if choice_rc == 'r':
                    clear_screen()
                    fence_opening_loop()
                elif choice_rc == 'c':
                    clear_screen()
                    print(cell_values['F4'])
                else:
                    print("Invalid input. Try again!")
        elif choice_la == 'a':
            clear_screen()
            fence_opening_loop()
        else:
            print("Invalid input. Try again!")


def bridge_loop():
    '''
    As the bridge scenario occurs multiple times in the story a function containing 
    all possible paths from the bridge scene is created for easier referral throughout the code.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['E2'])
    while True:
        choice_bj = input("Type 'b' to turn back or 'j' to attempt jump:\n").lower()
        if choice_bj == 'b':
            clear_screen()
            print(cell_values['F2'])
            start_again_loop()
        elif choice_bj == 'j':
            clear_screen()
            print(cell_values['F3'])
            while True:
                choice_jr = input("Type 'j' to jeer your assailant or 'r' to run for safety:\n").lower()
                if choice_jr == 'j':
                    clear_screen()
                    print(cell_values['D8'])
                    start_again_loop()
                elif choice_jr == 'r':
                    clear_screen()
                    print(cell_values['C8'])
                    while True:
                        choice_sc = input("Type 's' to head straight for exit or 'c' to creep along treeline:\n").lower()
                        if choice_sc == 's':
                            clear_screen()
                            print(cell_values['H5'])
                            start_again_loop()
                        elif choice_sc == 'c':
                            clear_screen()
                            print(cell_values['H2'])
                            while True:
                                choice_rw = input("Type 'r' to run for exit or 'w' to wait:\n").lower()
                                if choice_rw == 'r':
                                    clear_screen()
                                    print(cell_values['H4'])
                                elif choice_rw == 'w':
                                    clear_screen()
                                    print(cell_values['H3'])
                                    start_again_loop()
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
            else:
                print("Invalid input. Try again!")


def weapon_loop():
    '''
    As the weapon scenario occurs multiple times in the story a function containing 
    all possible paths from the weapon scene is created for easier referral throughout the code.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['F5'])
    while True:
        choice_we = input("Type 'w' to go for weapon or 'e' to enter RV:\n").lower()
        if choice_we == 'w':
            clear_screen()
            print(cell_values['H6'])
            start_again_loop()
        elif choice_we == 'e':
            clear_screen()
            print(cell_values['H8'])
            while True:
                choice_lw = input("Type 'l' to leave now or 'w' to wait and see:\n").lower()
                if choice_lw == 'l':
                    clear_screen()
                    print(cell_values['B2'])
                    while True:
                        choice_sf = input("Type 's' to stay on road or 'f' to brave the forest:\n").lower()
                        if choice_sf == 's':
                            clear_screen()
                            print(cell_values['G5'])
                            start_again_loop()
                        elif choice_sf == 'f':
                            clear_screen()
                            print(cell_values['G6'])
                            while True:
                                choice_ab = input("Type 'a' to find another route or 'b' to take the bridge:\n").lower()
                                if choice_ab == 'a':
                                    clear_screen()
                                    print(cell_values['H1'])
                                    start_again_loop()
                                elif choice_ab == 'b':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
                elif choice_lw == 'w':
                    clear_screen()
                    print(cell_values['H7'])
                    start_again_loop()
                else:
                    print("Invalid input. Try again!")
        else:
            print("Invalid input. Try again!")


def fence_opening_loop():
    '''
    As the fence opening scenario occurs multiple times in the story a function containing 
    all possible paths from the fence scene is created for easier referral throughout the code.
    Each choice variable is named by the to possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['E4'])
    while True:
        choice_hw = input("Type 'w' to find a weapon or 'h' to find a hiding spot:\n").lower()
        if choice_hw == 'w':
            clear_screen()
            weapon_loop()
        elif choice_hw == 'h':
            clear_screen()
            hide_loop()
        else:
            print("Invalid option. Try again!")


def river_loop():
    '''
    As the river scenario occurs multiple times in the story a function containing 
    all possible paths from the river scene is created for easier referral throughout the code.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['B5'])
    while True:
        choice_hg = input("Type 'h' to hide or 'g' to greet the driver:\n").lower()
        if choice_hg == 'h':
            clear_screen()
            print(cell_values['D4'])
            while True:
                choice_st = input("Type 's' to stay hidden or 't' to sneak into the back of the truck:\n").lower()
                if choice_st == 's':
                    clear_screen()
                    print(cell_values['D7'])
                    while True:
                        choice_wr = input("Type 'w' to wait for truck to move away or 'r' to run for the bridge:\n").lower()
                        if choice_wr == 'w':
                            clear_screen()
                            print(cell_values['G1'])
                            while True:
                                choice_bh = input("Type 'b' to continue to the bridge or 'h' to go back up the hill:\n").lower()
                                if choice_bh == 'b':
                                    clear_screen()
                                    bridge_loop()
                                elif choice_bh == 'h':
                                    clear_screen()
                                    print(cell_values['G2'])
                                else:
                                    print("Invalid input. Try again!")
                        elif choice_wr == 'r':
                            clear_screen()
                            print(cell_values['C7'])
                            start_again_loop()
                        else:
                            print("Invalid input. Try again!")
                elif choice_st == 't':
                    clear_screen()
                    print(cell_values['D5'])
                    while True:
                        choice_c = input("Type 'c' to continue forward:\n").lower()
                        if choice_c == 'c':
                            clear_screen()
                            print(cell_values['C6'])
                            while True:
                                choice_wo = input("Type 'o' to climb out now or 'w' to wait until car is inside the yard:\n").lower()
                                if choice_wo == 'o':
                                    clear_screen()
                                    print(cell_values['D6'])
                                    start_again_loop()
                                elif choice_wo == 'w':
                                    clear_screen()
                                    print(cell_values['E8'])
                                    while True:
                                        choice_wh = input("Type 'w' to find weapon or 'h' to hide amongst the scrap:\n").lower()
                                        if choice_wh == 'w':
                                            clear_screen()
                                            weapon_loop()
                                        elif choice_wh == 'h':
                                            clear_screen()
                                            hide_loop()
                                        else:
                                            print("Invalid input. Try again!")
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
                else:
                    print("Invalid input. Try again!")
        elif choice_hg == 'g':
            clear_screen()
            print(cell_values['C5'])
            start_again_loop()
        else:
            print("Invalid input. Try again!")


def hide_loop():
    '''
    As the hide scenario occurs multiple times in the story a function containing 
    all possible paths from the hide scene is created for easier referral throughout the code.
    Each choice variable is named by the possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['F6'])
    while True:
        choice_be = ("Type 'b' to go for the barn or 'e' to try the RV:\n").lower()
        if choice_be == 'b':
            clear_screen()
            print(cell_values['B8'])
        elif choice_be == 'e':
            clear_screen()
            print(cell_values['H8'])
            while True:
                choice_wl = input("Type 'l' to leave now or 'w' to wait and see:\n").lower()
                if choice_wl == 'l':
                    clear_screen()
                    print(cell_values['B2'])
                    while True:
                        choice_sf = input("Type 's' to stay on road or 'f' to brave the forest:\n").lower()
                        if choice_sf == 's':
                            clear_screen()
                            print(cell_values['G5'])
                            start_again_loop()
                        elif choice_sf == 'f':
                            clear_screen()
                            print(cell_values['G6'])
                            while True:
                                choice_ab = input("Type 'a' to find another route or 'b' to take the bridge:\n").lower()
                                if choice_ab == 'a':
                                    clear_screen()
                                    print(cell_values['H1'])
                                    start_again_loop()
                                elif choice_ab == 'b':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
                elif choice_wl == 'w':
                    clear_screen()
                    print(cell_values['H7'])
                    start_again_loop()
                else:
                    print("Invalid input. Try again!")
        else:
            print("Invalid input. Try again!")


def move_on_loop():
    '''
    As the move on scenario occurs multiple times in the story a function containing 
    all possible paths from the move on scene is created for easier referral throughout the code.
    Each choice variable is named by the to possible values the user can choose. 
    While loops are used to take the user from scene to scene. 
    Each loop has an else section for any invalid inputs the user may use.
    '''
    print(cell_values['F8'])
    while True:
        choice_cb = input("Type 'c' to climb down cliff to the scrapyard or 'b' to go back:\n").lower()
        if choice_cb == 'c':
            clear_screen()
            print(cell_values['G3'])
            while True:
                choice_yb = input("Type 'y' enter the yard or 'b' to skip the yard and go to bridge:\n").lower()
                if choice_yb == 'y':
                    clear_screen()
                    fence_opening_loop()
                elif choice_yb == 'b':
                    clear_screen()
                    print(cell_values['G4'])
                    while True:
                        choice_fs = input("Type 's' to stay on road or 'f' to go through the forest:\n").lower()
                        if choice_fs == 'f':
                            clear_screen()
                            print(cell_values['G6'])
                            while True:
                                choice_ba = input("Type 'a' to look for safer route or 'b' to take the bridge:\n").lower()
                                if choice_ba == 'a':
                                    clear_screen()
                                    print(cell_values['H1'])
                                    start_again_loop()
                                elif choice_ba == 'b':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again!")
                        elif choice_fs == 's':
                            clear_screen()
                            print(cell_values['G5'])
                            start_again_loop()
                        else:
                            print("Invalid input. Try again!")
                else:
                    print("Invalid input. Try again!")
        elif choice_cb == 'b':
            clear_screen()
            print(cell_values['G8'])
            while True:
                choice_rm = input("Type 'r' to retrieve knife or 'm' to move on:\n").lower()
                if choice_rm == 'r':
                    clear_screen()
                    print(cell_values['F6'])
                    start_again_loop()
                elif choice_rm == 'm':
                    clear_screen()
                    print(cell_values['G7'])
                    while True:
                        choice_ch = input("Type 'c' to confront driver or 'h' to hide:\n").lower()
                        if choice_ch == 'c':
                            clear_screen()
                            print(cell_values['G5'])
                            start_again_loop()
                        elif choice_ch == 'h':
                            clear_screen()
                            print(cell_values['E7'])
                            while True:
                                choice_rs = input("Type 'r' to go to the river or 's' to the scrapyard:\n").lower()
                                if choice_rs == 'r':
                                    clear_screen()
                                    print(cell_values['G6'])
                                    while True:
                                        choice_sb = input("Type 's' to find safer route or 'b' to chance the bridge:\n").lower()
                                        if choice_sb == 's':
                                            clear_screen()
                                            print(cell_values['H1'])
                                        elif choice_sb == 'b':
                                            clear_screen()
                                            bridge_loop()
                                        else:
                                            print("Invalid input. Try again!")
                                elif choice_rs == 's':
                                    clear_screen()
                                    initial_gate_loop()
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
                else:
                    print("Invalid input. Try again!")
        else:
            print("Invalid input. Try again!")



 # Initial text



title = (pyfiglet.figlet_format("HUNTERS ARENA"))
print(f"{Fore.CYAN} {title}")
print("A CHOOSE YOUR OWN ADVENTURE FOR THOSE WHO DARE TO RISK IT ALL!!")
print(Fore.CYAN+"----------------------------------------------------\n")
print("Make your choices by typing the values displayed in brackets.")

'''
While loop that begins the program with the initial choice to play or not to play.
If no the program breaks, if yes the adventure begins, if invalid it returns the choices to user.
'''
while True:
    start_choice = input("Would you like to start your adventure? (y/n): ").lower()
    if start_choice == "y":
        player_name = get_name()
        start_adventure()
        break
    elif start_choice == "n":
        print("That's too bad, maybe another time.")
        break  # Exit the loop if the user enters 'n'
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
