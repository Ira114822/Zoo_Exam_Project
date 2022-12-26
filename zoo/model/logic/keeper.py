from zoo.model.entity import *
from zoo.model.logic import *


# keeper  - a person who is responsible for feeding animals in a zoo
class Keeper:
    @staticmethod
    def calculate_daily_supply_of_food(zoo):
        if not isinstance(zoo, list):
            return -1

        daily_supply = 0  # daily supply of food for all animals
        for animal in zoo:
            if isinstance(animal, Animal):
                daily_supply += animal.daily_portion

        return daily_supply



    @staticmethod
    def calculate_annual_supply_of_food(daily_supply):
        return daily_supply * 365
