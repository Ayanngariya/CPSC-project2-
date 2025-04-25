# Author: Ayan Ngariya
# Class: CPSC 1050
# Project: Farm Adventure
# Date: April 2025
# GitHub Repo: https://github.com/yourname/FarmAdventure
#- W3Schools - Python Classes and Objects: https://www.w3schools.com/python/python_classes.asp
# - GeeksforGeeks - Python User Input and Exception Handling: https://www.geeksforgeeks.org/taking-input-in-python/, https://www.geeksforgeeks.org/python-exceptions/
# - RealPython - Building Simple Command Line Games: https://realpython.com/python-command-line-games/
# - https://github.com/Scarlettsang/Simple-Farm-Game


from farm import Farm
from player import Player

def main():
    print("Welcome to Farm Adventure!")
    name = input("Enter your farmer's name: ")
    player = Player(name)
    farm = Farm(player)

    while True:
        print("\nWhat would you like to do?")
        print("1. Plant Crop")
        print("2. Feed Animal")
        print("3. Harvest Crops")
        print("4. View Farm")
        print("5. Quit Game")

        choice = input("> ")

        if choice == "1":
            farm.plant_crop()
        elif choice == "2":
            farm.feed_animals()
        elif choice == "3":
            farm.harvest_crops()
        elif choice == "4":
            farm.show_farm()
        elif choice == "5":
            print(f"Thanks for playing, {player.name}! Goodbye.")
            break
        else:
            print("Invalid choice. Please try agian.")  

if __name__ == "__main__":
    main()
