__author__ = "Roland" 

class Product:
    """Descriere"""
    def __init__(self, id, name, quantity):
        self.__id = id
        self.__name = name
        self.__quantity = quantity

    def getId(self):
        return self.__id
    def setId(self,value):
        self.__id = value 
    id = property(getId,setId)

    def getName(self):
        return self.__name
    def setName(self,value):
        self.__name = value 
    name = property(getName,setName)

    def getQuantity(self):
        return self.__quantity
    def setQuantity(self,value):
        self.__quantity = value 
    quantity = property(getQuantity,setQuantity)

    def __str__(self):
        return str(self.__id) + " " + self.__name + " " + str(self.__quantity)

    def __add__(self, other):
        if other.name == self.name:
            prod = Product(self.id,self.name,other.quantity + self.quantity)
            return prod
        else:
            raise TypeError("Invalid type added")