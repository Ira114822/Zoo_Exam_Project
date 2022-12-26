import unittest

from zoo.model.entity import *
from zoo.model.logic import *


class KeeperTests(unittest.TestCase):

    def test_calculate_daily_supply_of_food(self):
        zoo = []
        zoo.append(Animal("Panda", 3000, 3))
        zoo.append(Animal("Lion", 15000, 1))
        zoo.append(Animal("Fox", 2000, 3))
        zoo.append(Animal("Panda", 3000, 2))

        expected = 36000

        actual = Keeper.calculate_daily_supply_of_food(zoo)

        self.assertEqual(expected, actual)

    def test_calculate_daily_supply_of_food_with_wrong_serving_size(self):
        zoo = []
        zoo.append(Animal("Panda", -3000, 3))
        zoo.append(Animal("Lion", 15000, 1))
        zoo.append(Animal("Fox", 2000, 3))
        zoo.append(Animal("Panda", 3000, 2))

        self.assertRaises(ValueError)

    def test_calculate_daily_supply_of_food_without_list(self):
        zoo = " "

        self.assertRaises(TypeError, zoo, [])


if __name__ == "__main__":
    unittest.main()
