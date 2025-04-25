# Author: Ayan Ngariya
# Class: CPSC 1050
# Project: Farm Adventure
# Date: April 2025

class Animal:
    def __init__(self, name):
        self.name = name
        self.fed = False

    def feed(self):
        if not self.fed:
            print(f"You fed the {self.name}.")
            self.fed = True
        else:
            print(f"The {self.name} is already full.")  
