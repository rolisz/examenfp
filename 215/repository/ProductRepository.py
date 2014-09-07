__author__ = "Roland"
from domain.Product import Product

class RepositoryException(Exception):
    pass

class ProductRepository:
    """Repository pentru aplicatie"""

    def __init__(self, validator):
        self.__validator = validator
        self.__list = []
        self.__maxID = 0
        self.read() 

    def findAll(self):
        return self.__list


    def update(self,product):
        if self.__validator.validate(product):
            for prod in self.__list:
                if prod.name == product.name:
                    self.__list[self.__list.index(prod)] = prod + product
                    self.save()
                    return
            #daca nu a fost gasit adaugam
            self.__list.append(product)
            self.__maxID +=1
            self.save()

    def remove(self,productId):
        for prod in self.__list:
            if prod.id == productId:
                del self.__list[self.__list.index(prod)]
                self.save()
                if self.__maxID == prod.id:
                    self.__maxID -=1
                return
        raise RepositoryException("Product with id "+str(productId)+" could not be found" )

    def newID(self):
        return self.__maxID + 1

    def read(self):
        try:
            file = open("Product.txt")
            line = file.readline()
            while line!='':
                id = int(line)
                if self.__maxID < id:
                    self.__maxID = id + 1
                name = file.readline()
                name = name.strip()
                quantity = int(file.readline())
                product = Product(id,name,quantity)
                self.__list.append(product)
                line = file.readline()
            file.close()
        except IOError as e:
            print("S-a intamplat o eroare la citirea fisierului.")
        except ValueError as e:
            print("Fisierul nu contine date valide")

    def save(self):
        try:
            file = open("Product.txt",'w')
            for prod in self.__list:
                file.write(str(prod.id) + "\n")
                file.write(prod.name + "\n")
                file.write(str(prod.quantity) + "\n")
        except IOError as e:
            print ("A aparut o problema la scrierea fisierului")
        finally:
            file.close()

