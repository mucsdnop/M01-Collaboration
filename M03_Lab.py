class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self,type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

car1 = Automobile(input("Enter vehicle type: "), input("Enter the year it was manufactured: "), input("Enter the make: "), input("Enter the model: "), input("Enter the number of doors: "), input("Enter the type of roof: "))

print(f"Vehicle type: {car1.type}")
print(f"Year: {car1.year}")
print(f"Make: {car1.make}")
print(f"Model: {car1.model}")
print(f"Number of Doors: {car1.doors}")
print(f"Type of roof: {car1.roof}")