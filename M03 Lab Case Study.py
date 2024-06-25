"""
Name: Philip Lian
File name: Auto Organizer
Description: This app allows user to enter car/auto information details
and the app display car details in a formatted output.
"""
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobil(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def discription(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


vehicle_type = "car"
year = int(input("Enter the year: "))
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = int(input("Enter the numbers of door (2 or 4): "))
roof = input("Enter the roof type(solid or sun roof): ")

car = Automobil(vehicle_type, year, make, model, doors, roof)

car.discription()
