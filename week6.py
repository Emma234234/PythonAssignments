#QN1
# Base Class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self._strength_level = strength_level  # Encapsulated attribute

    def show_details(self):
        print(f"Hero: {self.name}")
        print(f"Power: {self.power}")
        print(f"Strength Level: {self._strength_level}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


# Inherited Class 1
class FlyingHero(Superhero):
    def __init__(self, name, strength_level, fly_speed):
        super().__init__(name, "Flight", strength_level)
        self.fly_speed = fly_speed

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.fly_speed} km/h!")


# Inherited Class 2
class SpeedHero(Superhero):
    def __init__(self, name, strength_level, run_speed):
        super().__init__(name, "Super Speed", strength_level)
        self.run_speed = run_speed

    def use_power(self):
        print(f"{self.name} runs at lightning speed: {self.run_speed} km/h!")


# Create objects
hero1 = FlyingHero("SkyWing", 80, 500)
hero2 = SpeedHero("Blaze", 90, 700)

# Show details and use powers
hero1.show_details()
hero1.use_power()
print()
hero2.show_details()
hero2.use_power()


# QN2
# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclasses with their own version of move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for v in vehicles:
    v.move()

