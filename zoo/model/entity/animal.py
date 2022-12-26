class Animal:

    def __init__(self, animal_name, serving_size, count):
        self._animal_name = animal_name
        self._serving_size = serving_size   # portion weight in grams
        self._count = count                 # number of meals per day


    @property
    def daily_portion(self):
        return self._count * self._serving_size

    @daily_portion.setter
    def daily_portion(self, _count, _serving_size):
        self.daily_portion = self._count * self._serving_size

    @property
    def animal_name(self):
        return self._animal_name

    @animal_name.setter
    def animal_name(self, animal_name):
        self._animal_name = animal_name

    @animal_name.deleter
    def animal_name(self):
        del self._animal_name

    @property
    def serving_size(self):
        return self._serving_size

    @serving_size.setter
    def serving_size(self, serving_size):
        if isinstance(serving_size, int) and serving_size > 0:
            self._serving_size = serving_size
        else:
            raise Exception()

    @serving_size.deleter
    def serving_size(self):
        del self._serving_size

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if isinstance(count, int) and count > 0:
            self._count = count
        else:
            raise Exception()

    @count.deleter
    def count(self):
        del self._count

    def __str__(self):
        return f"{self._animal_name}: " \
               f"\neats {self._count} times a day {self._serving_size} grams"
