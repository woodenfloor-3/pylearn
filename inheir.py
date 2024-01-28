class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"Brand: {self.brand}")
        
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f"Model: {self.model}")

# Creating instances
car1 = Car(brand="Toyota", model="Camry")
car2 = Car(brand="Honda", model="Civic")

# Accessing methods from both Vehicle and Car
car1.display_info()
car2.display_info()