"""
Assignment 1: Design Your Own Class
-----------------------------------
This file demonstrates:
- Class creation
- Attributes & methods
- Constructors (__init__)
- Inheritance
- Polymorphism (method overriding)
- Encapsulation (private attributes)
"""

# Base Class
class Device:
    def __init__(self, brand, battery_life):
        self.brand = brand
        self.battery_life = battery_life  # in hours

    def info(self):
        return f"Brand: {self.brand}, Battery Life: {self.battery_life} hours"


# Derived Class with inheritance & polymorphism
class Smartphone(Device):
    def __init__(self, brand, battery_life, model, storage):
        super().__init__(brand, battery_life)  # Inherit Device properties
        self.model = model
        self.storage = storage  # in GB
        self.__secret_code = "1234"  # Encapsulation: private attribute

    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo 📸")

    # Overriding parent method (Polymorphism)
    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage, Battery: {self.battery_life} hrs"

    # Encapsulation: secure method to access private data
    def unlock_phone(self, code):
        if code == self.__secret_code:
            print("Phone unlocked 🔓")
        else:
            print("Wrong code! 🔒")


# --- Demo ---
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", 20, "Galaxy S21", 128)
    phone2 = Smartphone("Apple", 18, "iPhone 13", 256)

    print(phone1.info())
    phone1.take_photo()
    phone1.unlock_phone("1234")

    print(phone2.info())
    phone2.take_photo()
    phone2.unlock_phone("0000")   # Wrong code