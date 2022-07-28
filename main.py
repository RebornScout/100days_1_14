# Menu program for days 1 to 15 of 100 Days of Code
from functions import clear
from band_name_generator import band_name_generator

days = [
    {"Day" : "Day 1", "project" : "Band Name Generator", "function" : band_name_generator},
    {"Day" : "Day 2", "project" : "Tip Calculator", "function" : "tip_calculator()"}
]

def menu():
    clear()
    for day in days:
        print(day["Day"], day["project"])

while True:
    menu()
    choice = 20
    while choice < 1 or choice > 15:
        try:
            choice = int(input("Enter the day number for the project you would like to see. \n"))
        except ValueError:
            choice = 20
            continue
    if choice == 0:
        break
    else:
        days[choice-1]["function"]()
