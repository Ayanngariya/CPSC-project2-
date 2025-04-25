# Author: Ayan Ngariya
# Class: CPSC 1050
# Project: Farm Adventure
# Date: April 2025

class Crop:
    def __init__(self, name):
        self.name = name

    def harvest(self):
        print(f"You harvested {self.name}!")  # harvests the planted crop
