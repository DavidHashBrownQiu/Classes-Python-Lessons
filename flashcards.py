import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}

"""my_car = Car("Toyota", "Camry", 2023, "car1.jpg")
print(my_car.display_info())  # Output: 2023 Toyota Camry"""

cars = [
    Car("Toyota", "Camry", 2023, "camry_image.jpg"), #Examples of instances in classes
    Car("Honda", "Civic", 2022, "civic_image.jpg"),
    Car("Ford", "Mustang", 2021, "mustang_image.jpg")
]

# Convert objects to dictionaries
cars_data = [car.to_dict() for car in cars]
print(cars_data)

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)



"""class Mynumber:
    def __init__(self, value):
        self.value = value
    
    def print_value(self):
        print(self.value)

obj1 = Mynumber(170)
obj1.print_value()"""