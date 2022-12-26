import unittest
from zoo.model.entity import *


class TestAnimal(unittest.TestCase):

    def test_setter_positive(self):
        animal = Animal("Panda", 1000, 3)

        expected = 1000

        actual = animal.serving_size

        self.assertEqual(expected, actual)

    def test_setter_without_serving_size(self):
        animal = Animal("Panda")

        expected = 0

        actual = animal.serving_size

        self.assertEqual(expected, actual)

    def test_setter_negative(self):
        animal = Animal()

        self.assertRaises(ValueError, animal.serving_size, 1000)

    def test_name_positive(self):
        animal = Animal("Panda", 1000, 3)

        expected = "Panda"

        actual = animal.name

        self.assertEqual(expected, actual)

    def test_setter_without_name(self):
        animal = Animal(1000, 2)

        expected = 0

        actual = animal.name

        self.assertEqual(expected, actual)

    def test_wrong_name(self):
        animal = Animal(123, 1000, 2)

        self.assertRaises(TypeError, animal.name, "Panda")

    def test_count_positive(self):
        animal = Animal("Panda", 1000, 3)

        expected = 3

        actual = animal.count

        self.assertEqual(expected, actual)

    def test_setter_without_count(self):
        animal = Animal("Panda", 1000)

        expected = 0

        actual = animal.count

        self.assertEqual(expected, actual)

    def test_wrong_count(self):
        animal = Animal("Panda", 1000, "one")

        self.assertRaises(TypeError, animal.count, 1)

    def test_daily_portion_positive(self):
        animal = Animal("Panda", 1000, 2)
        expected = 2000

        actual = animal.daily_portion

        self.assertEqual(expected, actual)

    def test_daily_portion_without_count(self):
        animal = Animal("Panda", 1000)
        expected = 0

        actual = animal.daily_portion

        self.assertEqual(expected, actual)

    def test_daily_portion_with_wrong_serving_size(self):
        animal = Animal("Panda", -6, 2)

        self.assertRaises(ValueError, animal.serving_size, 6)


if __name__ == "__main__":
    unittest.main()
