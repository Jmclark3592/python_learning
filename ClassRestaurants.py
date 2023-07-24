# checking out git stash


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant, {self.restaurant_name}, serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = "chocolate", "vanilla"

    def flavor_types(self):
        flavors = " and ".join(self.flavors)
        print(f"The stand offers {flavors}.")


restaurant = Restaurant("Five Guys", "burgers")
restaurant2 = IceCreamStand("Baskin Robbins", "ice cream")

restaurant2.flavor_types()
