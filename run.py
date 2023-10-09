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
forest3_cell = story.acell('A6').value
spikes_cell = story.acell('B1').value
leave_yard_cell = story.acell('B2').value
downhill_cell = story.acell('B3').value
junction_cell = story.acell('B4').value
river_cell = story.acell('B5').value
initial_forest_cell = story.acell('B6').value
goback_cell = story.acell('B7').value
barn_cell = story.acell('B8').value
ignore_cell = story.acell('C1').value
hide_cell = story.acell('C2').value
tend_wound_cell = story.acell('C3').value
light_cell = story.acell('C4').value
car_death1_cell = story.acell('C5').value
inside_truck_cell = story.acell('C6').value
gun_death2_cell = story.acell('C7').value
exit_cell = story.acell('C8').value
initial_gate_cell = story.acell('D1').value
pass_gate_cell = story.acell('D2').value
forest_cell = story.acell('D3').value
hide2_cell = story.acell('D4').value
hide_in_truck_cell = story.acell('D5').value
death1_cell = story.acell('D6').value
truck_pass_cell = story.acell('D7').value
jeer_cell = story.acell('D8').value
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
hide3_cell = story.acell('F6').value
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
baseball_bat_death_cell = story.acell('H6').value
wait_death_cell = story.acell('H7').value
map_find_cell = story.acell('H8').value


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


def start_again_loop():
    while True:
        start_again = input("Type 's' to return to the beginning and try a different path: ").lower()
        if start_again == 's':
            clear_screen()
            start_adventure()
        else:
            print("Invalid input. Try again!")


def junction_loop():
    print(junction_cell)
    while True:
        choice_123 = input("Type '1' to take road 1, '2' to take road 2 or '3' to take road 3: ").lower()
        if choice_123 == '1':
            clear_screen()
            print(downhill_cell)
            while True:
                choice_tw = input("Type 't' to tend wound or 'w' to limp your way to the water: ").lower()
                if choice_tw == 't':
                    clear_screen()
                    print(tend_wound_cell)
                    while True:
                        choice_hc = input("Type 'h' to hide or 'c' to ignore and continue: ").lower()
                        if choice_hc == 'h':
                            clear_screen()
                            print(hide_cell)
                            while True:
                                choice_sr = input("Type 's' to stay or 'r' to run: ").lower()
                                if choice_sr == 's':
                                    clear_screen()
                                    print(car_death2_cell)
                                    while True:
                                        start_again = input("Type 's' to return to the beginning and try a different path: ").lower()
                                        if start_again == 's':
                                            start_adventure()
                                        else:
                                            print("Invalid input. Try again!")
                                elif choice_sr == 'r':
                                    clear_screen()
                                    print(ignore_cell)
                                    while True:
                                        continue_forward = input("Type 'c' to continue forward: ").lower()
                                        if continue_forward == 'c':
                                            clear_screen()
                                            bridge_loop()
                                else:
                                    print("Invalid input. Try again! ")
                        elif choice_hc == 'c':
                            clear_screen()
                            print(ignore_cell)
                        else:
                            print("Invalid input. Please type 'h' to hide or 'c' to ignore and continue: ")
                elif choice_tw == 'w':
                    clear_screen()
                    print(no_tend_wound_cell)
                    while True:
                        continue_forward = input("Type 'c' to continue forward: ").lower()
                        if continue_forward == 'c':
                            clear_screen()
                            bridge_loop()
                        else:
                            print("Invalid input. Try again! ")
                else:
                    print("Invalid input. Try again! ")
        elif choice_123 == '2':
            clear_screen()
            print(light_cell)
            while True:
                choice_gr = input("Type 'g' to enter gate or 'r' to pass and continue down the road: ").lower()
                if choice_gr == 'g':
                    clear_screen()
                    print(initial_gate_cell)
                    while True:
                        choice_la = input("Type 'l' to open lock or 'a' to find another way: ").lower()
                        if choice_la == 'l':
                            clear_screen()
                            print(rock_cell)
                            while True:
                                choice_rc = input("Type 'r' to use rock or 'c' to continue searching: ").lower()
                                if choice_rc == 'r':
                                    clear_screen()
                                    fence_opening_loop()
                                elif choice_rc == 'c':
                                    clear_screen()
                                    print(car_death3_cell)
                                else:
                                    print("Invalid input. Try again.")
                        elif choice_la == 'a':
                            clear_screen()
                            fence_opening_loop()
                        else:
                            print("Invalid input. Try again.")
                elif choice_gr == 'r':
                    clear_screen()
                    print(pass_gate_cell)
                else:
                    print("Invalid input. Try again.")
        elif choice_123 == '3':
            clear_screen()
            print(forest_cell)
            while True:
                choice_iq = input("Type 'i' to investigate or 'q' to move on quickly: ").lower()
                if choice_iq == 'i':
                    clear_screen()
                    print(racoon_scare_cell)
                    while True:
                        choice_cm = input("Type 'c' to climb down or 'm' to move on: ").lower()
                        if choice_cm == 'c':
                            clear_screen()
                            print(retrieve_knife_cell)
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


def bridge_loop():
    print(bridge_cell)
    while True:
        choice_bj = input("Type 'b' to turn back or 'j' to attempt jump: ").lower()
        if choice_bj == 'b':
            clear_screen()
            print(gun_death1_cell)
            start_again_loop()
        elif choice_bj == 'j':
            clear_screen()
            print(bridge_jump_cell)
            while True:
                choice_jr = input("Type 'j' to jeer your assailant or 'r' to run for safety: ").lower()
                if choice_jr == 'j':
                    clear_screen()
                    print(jeer_cell)
                    start_again_loop()
                elif choice_jr == 'r':
                    clear_screen()
                    print(exit_cell)
                    while True:
                        choice_sc = input("Type 's' to head straight for exit or 'c' to creep along treeline: ").lower()
                        if choice_sc == 's':
                            clear_screen()
                            print(go4_exit_cell)
                            start_again_loop()
                        elif choice_sc == 'c':
                            clear_screen()
                            print(creep_cell)
                            while True:
                                choice_rw = input("Type 'r' to run for exit or 'w' to wait: ").lower()
                                if choice_rw == 'r':
                                    clear_screen()
                                    print(victory_cell)
                                elif choice_rw == 'w':
                                    clear_screen()
                                    print(hunters_cell)
                                    start_again_loop()
                                else:
                                    print("Invalid input. Try again!")
                        else:
                            print("Invalid input. Try again!")
            else:
                print("Invalid input. Try again!")


def weapon_loop():
    print(weapon_cell)
    while True:
        choice_we = input("Type 'w' to go for weapon or 'e' to enter RV: ").lower()
        if choice_we == 'w':
            clear_screen()
            print(baseball_bat_death_cell)
            start_again_loop()
        elif choice_we == 'e':
            clear_screen()
            print(map_find_cell)
            while True:
                choice_lw = input("Type 'l' to leave now or 'w' to wait and see: ").lower()
                if choice_lw == 'l':
                    clear_screen()
                    print(leave_yard_cell)
                    while True:
                        choice_sf = input("Type 's' to stay on road or 'f' to brave the forest: ").lower()
                        if choice_sf == 's':
                            clear_screen()
                            print(car_death4_cell)
                            start_again_loop()
                        elif choice_sf == 'f':
                            clear_screen()
                            print(forest2_cell)
                            while True:
                                choice_ab = input("Type 'a' to find another route or 'b' to take the bridge: ").lower()
                                if choice_ab == 'a':
                                    clear_screen()
                                    print(car_death5_cell)
                                    start_again_loop()
                                elif choice_ab == 'b':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again.")
                        else:
                            print("Invalid input. Try again.")
                elif choice_lw == 'w':
                    clear_screen()
                    print(wait_death_cell)
                    start_again_loop()
                else:
                    print("Invalid input. Try again.")
        else:
            print("Invalid input. Try again.")


def fence_opening_loop():
    print(fence_opening_cell)
    while True:
        choice_hw = input("Type 'w' to find a weapon or 'h' to find a hiding spot: ").lower()
        if choice_hw == 'w':
            clear_screen()
            print(weapon_cell)
        elif choice_hw == 'h':
            clear_screen()
            hide_loop()
        else:
            print("Invalid option. Try again.")


def river_loop():
    print(river_cell)
    while True:
        choice_hg = input("Type 'h' to hide or 'g' to greet the driver: ").lower()
        if choice_hg == 'h':
            clear_screen()
            print(hide2_cell)
            while True:
                choice_st = input("Type 's' to stay hidden or 't' to sneak into the back of the truck: ").lower()
                if choice_st == 's':
                    clear_screen()
                    print(truck_pass_cell)
                    while True:
                        choice_wr = input("Type 'w' to wait for truck to move away or 'r' to run for the bridge: ").lower()
                        if choice_wr == 'w':
                            clear_screen()
                            print(wait_cell)
                            while True:
                                choice_bh = input("Type 'b' to continue to the bridge or 'h' to go back up the hill: ").lower()
                                if choice_bh == 'b':
                                    clear_screen()
                                    bridge_loop()
                                elif choice_bh == 'h':
                                    clear_screen()
                                    print(retreat_cell)
                                else:
                                    print("Invalid input. Try again!")
                        elif choice_wr == 'r':
                            clear_screen()
                            print(gun_death2_cell)
                            start_again_loop()
                        else:
                            print("Invalid input. Try again!")
                elif choice_st == 't':
                    clear_screen()
                    print(hide_in_truck_cell)
                    while True:
                        choice_c = input("Type 'c' to continue forward: ").lower()
                        if choice_c == 'c':
                            clear_screen()
                            print(inside_truck_cell)
                            while True:
                                choice_wo = input("Type 'o' to climb out now or 'w' to wait until car is inside the yard: ").lower()
                                if choice_wo == 'o':
                                    clear_screen()
                                    print(death1_cell)
                                    start_again_loop()
                                elif choice_wo == 'w':
                                    clear_screen()
                                    print(inside_gate_cell)
                                    while True:
                                        choice_wh = input("Type 'w' to find weapon or 'h' to hide amongst the scrap: ").lower()
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
            print(car_death1_cell)
            start_again_loop()
        else:
            print("Invalid input. Try again!")


def hide_loop():
    print(hide3_cell)
    while True:
        choice_be = ("Type 'b' to go for the barn or 'e' to try the RV: ").lower()
        if choice_be == 'b':
            clear_screen()
            print(barn_cell)
        elif choice_be == 'e':
            clear_screen()
            print(map_find_cell)
            while True:
                choice_wl = input("Type 'l' to leave now or 'w' to wait and see: ").lower()
                if choice_wl == 'l':
                    clear_screen()
                    print(leave_yard_cell)
                    while True:
                        choice_sf = input("Type 's' to stay on road or 'f' to brave the forest: ").lower()
                        if choice_sf == 's':
                            clear_screen()
                            print(car_death4_cell)
                            start_again_loop()
                        elif choice_sf == 'f':
                            clear_screen()
                            print(forest2_cell)
                            while True:
                                choice_ab = input("Type 'a' to find another route or 'b' to take the bridge: ").lower()
                                if choice_ab == 'a':
                                    clear_screen()
                                    print(car_death5_cell)
                                    start_again_loop()
                                elif choice_ab == 'b':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again.")
                        else:
                            print("Invalid input. Try again.")
                elif choice_wl == 'w':
                    clear_screen()
                    print(wait_death_cell)
                    start_again_loop()
                else:
                    print("Invalid input. Try again!")
        else:
            print("Invalid input. Try again!")


def move_on_loop():
    print(move_on_cell)
    while True:
        choice_cb = input("Type 'c' to climb down cliff to the scrapyard or 'b' to go back: ").lower()
        if choice_cb == 'c':
            clear_screen()
            print(climb_down_cell)
            while True:
                choice_yb = input("Type 'y' enter the yard or 'b' to skip the yard and go to bridge: ").lower()
                if choice_yb == 'y':
                    clear_screen()
                    fence_opening_loop()
                elif choice_yb == 'b':
                    clear_screen()
                    print(skip_yard_cell)
                    while True:
                        choice_fs = input("Type 's' to stay on road or 'f' to go through the forest: ").lower()
                        if choice_fs == 'f':
                            clear_screen()
                            print(forest2_cell)
                            while True:
                                choice_ba = input("Type 'a' to look for safer route or 'b' to take the bridge: ").lower()
                                if choice_ba == 'a':
                                    clear_screen()
                                    print(car_death5_cell)
                                    start_again_loop()
                                elif choice_ba == 'b':
                                    clear_screen()
                                    bridge_loop()
                                else:
                                    print("Invalid input. Try again!")
                        elif choice_fs == 's':
                            clear_screen()
                            print(car_death4_cell)
                            start_again_loop()
                        else:
                            print("Invalid input. Try again!")
                else:
                    print("Invalid input. Try again!")
        elif choice_cb == 'b':
            clear_screen()
            print(turnback_cell)
        else:
            print("Invalid input. Try again!")


start_choice = input().lower()

if start_choice == "y":
    player_name = get_name()
    start_adventure()
elif start_choice == "n":
    print("That's too bad, maybe another time.")
else:
    print("Invalid choice. Please enter 'y' or 'n'.")
    retry = input("Do you want to retry? (y/n): ").lower()
    if retry == "y":
        start_adventure()
    elif retry == "n":
        print("That's too bad, maybe another time")
    else:
        print("Incorrect input try again")


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


clear_screen()
print(escape_holding_cell)
time.sleep(2)
print(realization_cell)
while True:
    choice_cx = input("Type 'c' to continue or 'x' to exit: ").lower()
    if choice_cx == 'c':
        clear_screen()
        print(initial_descision_cell)
        while True:
            choice_lfr = input("Type 'l' to go left toward river, 'f' to go forward or 'r' to go right in to the forest: ").lower()
            if choice_lfr == 'f':
                clear_screen()
                junction_loop()
            elif choice_lfr == 'r':
                clear_screen()
                print(initial_forest_cell)
                while True:
                    choice_fb = input("Type 'f' to go forward or 'b' to go back: ").lower()
                    if choice_fb == 'f':
                        clear_screen()
                        print(spikes_cell)
                        start_again_loop()
                    elif choice_fb == 'b':
                        clear_screen()
                        print(goback_cell)
                        while True:
                            choice_fl = input("Type 'f' to go forward or 'l' to go to the river: ").lower()
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
                print(river_cell)
                river_loop()
            else:
                print("Invalid input. Try again! ")
    elif choice_cx == 'x':
        print("You lie down and wait for death. Game Over!")
        start_adventure()
    else:
        print("Invalid input. Try again!")
