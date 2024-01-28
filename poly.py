class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("eoof")
class Cat(Animal):
    def speak(self):
        print("Meow")
#instance        
dog=Dog()
cat=Cat()
#ploy behavior
dog.speak()
cat.speak()
