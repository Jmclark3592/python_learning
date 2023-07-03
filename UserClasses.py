class User:
    def __init__(self, first_name, last_name, age, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"User's name is {self.first_name.title()} {self.last_name.title()}, is {self.age} and {self.status}"
        )

    def greet_user(self):
        print(f"Hello, {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"number of login attempts {(self.login_attempts)}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"login attempts reset to {self.login_attempts}")


user1 = User("justin", "clark", 36, "single")
user2 = User("ryan", "clark", 32, "has a baby mama")
user3 = User("todd", "clark", "ancient", "married")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
