

class Restaurant:
    def __init__(self, restaurant_name1, cuisine_type):
        self.restaurant_name = restaurant_name1
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant {self.restaurant_name} makes the best {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

rest1 = Restaurant('Five Guys', 'burgers')

rest1.describe_restaurant()