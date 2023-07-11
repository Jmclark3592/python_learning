import unittest
from city_functions import formatted


class Testing(unittest.TestCase):
    def test_city_country(self):
        formatted_place = formatted("edina", "minnesota")
        self.assertEqual(formatted_place, "Edina, Minnesota")


if __name__ == "__main__":
    unittest.main()
