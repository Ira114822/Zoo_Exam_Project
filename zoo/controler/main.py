from zoo.model.entity import *
from zoo.model.logic import *


def main():
    zoo = AnimalCreator.creator(55)
    print(DataConvertor.convert_to_string(zoo))

    KILOGRAM = 1000

    daily_supply = Keeper.calculate_daily_supply_of_food(zoo)
    print(f"\nFood supply for the day = {daily_supply} grams or {daily_supply / KILOGRAM} kg\n")

    month = input("Month: ")

    days = int(input("How many days in the month: "))


    print(f"\nNeed for {month} - {daily_supply * days} grams or {(daily_supply * days) / KILOGRAM} kg\n")

    year = Keeper.calculate_annual_supply_of_food(daily_supply)
    print(f"\nFor this year we need - {year} grams or {year / KILOGRAM} kg")


    print(f"\nDo you know who eats the most in our zoo? "
          f"\nI can tell you)))"
          f"\nIt's a {Statist.find_most_voracious_animal(zoo)}")

    print(f"\nEats the least - {Statist.find_animal_that_eats_the_least(zoo)}")

    print(f"\nNow in our zoo {Statist.calculate_all_animals_in_zoo(zoo)} animals")
    del zoo[5]
    print(f"It seems we are less."
          f"\n{zoo[5]} found a new home")
    print(f"\nNow in our zoo {Statist.calculate_all_animals_in_zoo(zoo)} animals")

    daily_supply = Keeper.calculate_daily_supply_of_food(zoo)
    year = Keeper.calculate_annual_supply_of_food(daily_supply)
    print(f"\nNow \nfood supply for the day = {daily_supply} grams or {daily_supply / KILOGRAM} kg"
          f"\nfor month - {daily_supply * days} grams or {(daily_supply * days) / KILOGRAM} kg"
          f"\nfor year - {year} grams or {year / KILOGRAM} kg")







if __name__ == "__main__":
    main()