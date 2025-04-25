# Author: Ayan Ngariya
# Class: CPSC 1050
# Project: Farm Adventure
# Date: April 2025
#- W3Schools - Python Classes and Objects: https://www.w3schools.com/python/python_classes.asp
# - GeeksforGeeks - Python User Input and Exception Handling: https://www.geeksforgeeks.org/taking-input-in-python/, https://www.geeksforgeeks.org/python-exceptions/
# - RealPython - Building Simple Command Line Games: https://realpython.com/python-command-line-games/
# - https://github.com/Scarlettsang/Simple-Farm-Game


from crop import Crop
from animal import Animal

class Farm:
    #defines diffrient animals
    def __init__(self, player):
        self.player = player
        self.crops = []
        self.animals = [Animal("Cow"), Animal("Chicken")]

    def log_action(self, action):
        try:
            with open("farm_log.txt", "a") as log_file:
                log_file.write(action + "\n")
        except Exception as e:
            print(f"Failed to log action: {e}")

    def plant_crop(self):
        #Asks User the input he wants to put in 
        crop_name = input("Enter the name of the crop you want to plant (like Corn): ")
        if crop_name.strip() != "":
            #Deducts money onhow much the crop costs
            planting_cost = 5
            if self.player.spend_money(planting_cost):
                crop = Crop(crop_name)
                self.crops.append(crop)
                print(f"You planted {crop.name}! (${planting_cost} deducted)")
                self.log_action(f"Planted {crop.name} for ${planting_cost}")
            else:
                print("Planting failed, not enough money.")
        else:
            print("Crop name can't be empty.")

    def feed_animals(self):
        #feeds The 2 animals that are made 
        for animal in self.animals:
            animal.feed()
            self.log_action(f"Fed {animal.name}")

    def harvest_crops(self):
        if self.crops:
            harvest_income = 10 * len(self.crops)
            for crop in self.crops:
                crop.harvest()
                self.log_action(f"Harvested {crop.name}")
            self.crops.clear()
            self.player.earn_money(harvest_income)
            print(f"You earned ${harvest_income} from the harvest!")
        else:
            print("No crops to harvest!")

    def show_farm(self):
        #lets the User know that what is going on their farm 
        print("\n-- Farm Status --")
        print(f"Farmer: {self.player.name} | Money: ${self.player.money}")
        print("Animals:")
        for animal in self.animals:
            print(f"{animal.name} - {'Fed' if animal.fed else 'Hungry'}")
        print("Crops:")
        if self.crops:
            for crop in self.crops:
                print(f"{crop.name} (Growing)")
        else:
            print("No crops currently growing.")
        print("--------------------")
