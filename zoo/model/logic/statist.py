from zoo.model.entity import *


class Statist:

    @staticmethod
    def find_most_voracious_animal(zoo):

        if not isinstance(zoo, (list, tuple)):
            return -1

        ieater = 0

        for index in range(1, len(zoo)):
            if isinstance(zoo[index], Animal):
                first = zoo[index].serving_size
                heavy_eater = zoo[ieater].serving_size

                if first > heavy_eater:
                    ieater = index

        return zoo[ieater]

    @staticmethod
    def find_animal_that_eats_the_least(zoo):

        if not isinstance(zoo, (list, tuple)):
            return -1

        ieater = 0

        for index in range(1, len(zoo)):
            if isinstance(zoo[index], Animal):
                first = zoo[index].serving_size
                least_eater = zoo[ieater].serving_size

                if first < least_eater:
                    ieater = index

        return zoo[ieater]

    @staticmethod
    def calculate_all_animals_in_zoo(zoo):
        if not isinstance(zoo, (list, tuple)):
            return -1

        count = len(zoo)

        return count



