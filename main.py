class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}"

    def __repr__(self):
        return f"Vehicle({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r})"

    def honk(self):
        return "Honk!"


# Dunder functions here

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors

    # Add class specific attributes and __str__, __repr__ methods here
    def __str__(self):
        return f"{super().__str__()}\nNum Doors: {self.num_doors}"

    def __repr__(self):
        return f"Car({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.num_doors!r})"

    def honk(self):
        return "Beep beep!"


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, payload_capacity):
        super().__init__(make, model, year, weight)
        self.payload_capacity = payload_capacity

    # Add class specific attributes and __str__, __repr__ methods here
    def __str__(self):
        return f"{super().__str__()}\nPayload capacity: {self.payload_capacity}"

    def __repr__(self):
        return f"Truck({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.payload_capacity!r})"

    def honk(self):
        return "Honk honk!"


class Boat(Vehicle):
    def __init__(self, make, model, year, weight, length):
        super().__init__(make, model, year, weight)
        self.length = length

    # Add class specific attributes and __str__, __repr__ methods here
    def __str__(self):
        return f"{super().__str__()}\nLength: {self.length}"

    def __repr__(self):
        return f"Boat({self.make!r}, {self.model!r}, {self.year!r}, {self.weight!r}, {self.length!r})"

    def honk(self):
        return "Boat horn sound!"


# Test driver function
def main():
    # Create instances of Vehicle, Car, Truck, and Boat
    vehicle = Vehicle("Generic", "Transport", 2020, 1000)
    car = Car("Ford", "Mustang", 1964, 1500, 2)
    truck = Truck("Dodge", "Ram", 2010, 5000, 2000)  # Payload capacity in pounds
    boat = Boat("Yamaha", "242 Limited S", 2018, 3600, 24)  # Length in feet

    # Print the __str__ representation
    print("String Representations:")
    print(str(vehicle))
    print(str(car))
    print(str(truck))
    print(str(boat))

    # Print the __repr__ representation
    print("\nUnambiguous Representations:")
    print(repr(vehicle))
    print(repr(car))
    print(repr(truck))
    print(repr(boat))

    # Demonstrating the honk method
    print("\nVehicle Sounds:")
    print(f"{vehicle.make} Vehicle: {vehicle.honk()}")
    print(f"{car.make} Car: {car.honk()}")
    print(f"{truck.make} Truck: {truck.honk()}")
    print(f"{boat.make} Boat: {boat.honk()}")


# Execute the test driver function
if __name__ == "__main__":
    main()
