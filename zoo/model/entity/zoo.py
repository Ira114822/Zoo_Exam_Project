from zoo.model.entity import *
from zoo.model.logic import *


class Zoo(Animal, AnimalCreator):
    # list of all animals in the zoo

    DEFAULT_SIZE = 1500  # maximum number of animals in the zoo

    def __init__(self, size=DEFAULT_SIZE):
        self._zoo = []
        if size > 0:
            self._size = size
        else:
            self._size = Zoo.DEFAULT_SIZE

    @property
    def size(self):
        return self._size

    def __len__(self):
        return len(self._zoo)

    def add(self, animal):
        if isinstance(animal, Animal):
            self._zoo.append(animal)

    def __getitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            return self._zoo[index]
        else:
            raise Exception()

    def __setitem__(self, index, value):
        if (isinstance(index, int)
                and 0 <= index < len(self)
                and isinstance(value, Animal)):
            self._zoo[index] = value
        else:
            raise Exception()

    def __delitem__(self, index):
        if isinstance(index, int) and 0 <= index < len(self):
            del self._zoo[index]
        else:
            raise Exception()

    def __str__(self):
        if not self._zoo:
            return f"Zoo is empty. We can accept {self._size} animals"
        else:
            msg = "Animal:\n"
            for animal in self._zoo:
                msg += str(animal) + "\n"
            msg += f"There are {self._size - len(self)} empty places"
        return msg
