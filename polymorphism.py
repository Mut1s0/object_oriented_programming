"""
Activity 2: Polymorphism Challenge
-----------------------------------
This file demonstrates polymorphism:
- Different classes with the same method name (move)
- Each behaves differently depending on the class
"""

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

# --- Demo ---
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()