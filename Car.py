class Car:
    total_cars=0
    def __init__(self, brand, model):
        self.brand =brand
        self.model =model
        Car.total_cars +=1
    
    def display_info(self):
        return(f"{self.brand} {self.model}")


car1 = Car(brand="Toyota", model="Camry")
car2 = Car(brand="Honda", model="Civic")
car3= Car(brand="Mitsubishi",model="lancer")
cars=[car1,car2,car3]
print(f"Total Cars: {Car.total_cars}")
print(f"Cars are: {', '.join(car.display_info() for car in cars)}")


# my_car = Car(brand="Toyota", model="Camry")
# print(my_car.brand)  # Output: Toyota
# print(my_car.model)  # Output: Camry
#my_car.display_info()  # Output: Toyota Camry
# Creating another instance of the Car class
# another_car = Car(brand="Honda", model="Civic")

# # Accessing attributes of the instances
# print(my_car.brand)       # Output: Toyota
# print(another_car.model)  # Output: Civic

# # Calling the display_info method
# my_car.display_info()     # Output: Toyota Camry
# another_car.display_info()# Output: Honda Civic

