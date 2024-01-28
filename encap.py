class person:
    def __init__(self,name,age):
        self._name=name # protected attr
        self.__age=age # private attr
    def display_info(self):
       print(f"Name: {self._name}, Age: {self.__age}")
Person =person(name="woodenfloor",age=22)
Person.display_info() 