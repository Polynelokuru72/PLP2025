
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Smartphone: {self.brand} {self.model}")
        print(f"Price: ${self.price}")

    def turn_on(self):
        print(f"{self.brand} {self.model} is now ON!")

    def turn_off(self):
        print(f"{self.brand} {self.model} is now OFF!")


class SmartphoneCamera(Smartphone):
    def __init__(self, brand, model, price, camera_quality):
        super().__init__(brand, model, price)
        self.camera_quality = camera_quality

    def turn_on(self):
        super().turn_on()
        print(f"Camera Quality: {self.camera_quality}MP")

    def take_picture(self):
        print(f"Taking a picture with the {self.camera_quality}MP camera!")


camera_phone = SmartphoneCamera("Samsung", "Galaxy S21", 799, 108)
camera_phone.display_details()
camera_phone.turn_on()
camera_phone.take_picture()


class Animal:
    def move(self):
        print("This animal moves.")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("The bird flies 🐦")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")


dog = Dog()
bird = Bird()
fish = Fish()


animals = [dog, bird, fish]
for animal in animals:
    animal.move()
