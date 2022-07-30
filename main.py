# Menu program for days 1 to 15 of 100 Days of Code
from functions import clear
import band_name_generator
import tip_calculator
import treasure_island
import rock_paper_scissors
import password_generator
import hangman
import caesar_cipher

days = [
    {"Day": "Day 1", "project": "Band Name Generator", "function": band_name_generator},
    {"Day": "Day 2", "project": "Tip Calculator", "function": tip_calculator},
    {"Day": "Day 3", "project": "Treasure Island (Incomplete)", "function": treasure_island},
    {"Day": "Day 4", "project": "Rock, Paper, Scissors", "function": rock_paper_scissors},
    {"Day": "Day 5", "project": "Password Generator", "function": password_generator},
    {"Day": "Day 6", "project": "No final project"},
    {"Day": "Day 7", "project": "Hangman", "function": hangman},
    {"Day": "Day 8", "project": "Caesar Cipher", "function": caesar_cipher},
]


def menu():
    clear()
    for day in days:
        print(day["Day"], day["project"])


while True:
    menu()
    choice = 20
    while choice < 0 or choice > 15:
        try:
            choice = int(input("Enter the day number for the project you would like to run or '0' to exit. \n"))
        except ValueError:
            choice = 20
            continue
    if choice == 0:
        break
    elif choice == 6:
        print(f"Day {choice} of 100 Days of code did not have a final project.")
        continue
    else:
        days[choice - 1]["function"].play()
        return_to_menu = input("Return to the menu? Type 'y' or 'n'")
        if return_to_menu != "y":
            break
