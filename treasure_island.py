# 100 Days of Code - Day 2 Treasure Island
from ascii_art import treasure_logo

def play():
    print(treasure_logo)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
    direction = input("Do you want to go left or right?").lower
    if direction == "left":
        direction = input("Do you want to swim or wait")
    else:
        print("You fell down a big hole!\nGame over")
