from zoo.model.entity.animal import Animal


class Herbivores(Animal):
    def __init__(self, animal_name, serving_size, count, feed="food for herbivores"):
        super().__init__(animal_name, serving_size, count)
        self._feed = feed

    @property
    def feed(self):
        return self._feed

    @feed.setter
    def feed(self, feed):
        self._feed = feed

    @feed.deleter
    def feed(self):
        del self._feed

    def __str__(self):
        return f"{self.animal_name} eats {self.serving_size} grams " \
               f"{self.feed} {self.count} times a day"