class Dog:
    '''A simple attempt to model a dog'''

    def __init__(self, name, age):
        '''initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''simulate a dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''simulate rolling over in response to a command'''
        print(f"{self.name} rolled over!")

#instances:
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)


print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age}")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age}")
your_dog.sit()

