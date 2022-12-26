import random
from zoo.model.entity import *


class AnimalCreator:

    def creator(size):
        NAME = ("Panda", "Crocodile", "Lion", "Tiger", "Wolf", "Fox", "Bear",
                "Doe", "Sheep", "Goat", "Pig", "Elephant",
                "Horse", "Bison", "Donkey", "Monkey", "Hyena",
                "Varan", "Alligator")

        ls = []
        MIN_SIZE = 500   #minimum serving size
        MAX_SIZE = 5000  #maximum serving size
        MIN_COUNT = 1   # minimum number of meals per day
        MAX_COUNT = 4   # maximum number of meals per day

        for _ in range(size):
            name = random.choice(NAME)
            serving_size = random.randint(MIN_SIZE, MAX_SIZE)
            count = random.randint(MIN_COUNT, MAX_COUNT)

            animal = Animal(name, serving_size, count)

            ls.append((animal))

        return ls
