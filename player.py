# Author: Ayan Ngariya
# Class: CPSC 1050
# Project: Farm Adventure
# Date: April 2025

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100  # Starting money

    def earn_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            print("Not enough cash!")  # Comment: money checking
            return False
