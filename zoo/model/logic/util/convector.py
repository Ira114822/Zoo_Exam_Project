from zoo.model.entity import *


class DataConvertor:
    @staticmethod
    def convert_to_string(animals):
        r = "List of animals:\n"
        if not isinstance(animals, (list, tuple)):
            return "List is empty"

        for animal in animals:
            if isinstance(animal, Animal):
                r += "\n" + str(animal)

        return r