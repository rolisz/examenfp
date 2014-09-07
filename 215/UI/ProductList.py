__author__ = "Roland"

import UI.console as console
from repository.ProductRepository import RepositoryException
from domain.ProductValidator import ValidationException

class ProductListUi:
    """Interfata cu utilizatorul"""

    def __init__(self,contr):
        self.__contr = contr

    def run(self):
        opt = ''
        while opt != 'E':
            products = self.__contr.getAllProducts()
            products.sort(key = lambda prod: prod.name)
            print("Product List (id, name, quantity):")
            for prod in products:
                print(prod)
            print("Command: A - Add product; R - Remove Product; E - Exit")
            opt = console.getCommand(['A','E','R'])
            if opt == 'A':
                print("Add a product: ")
                self.add()
            if opt == 'R':
                print("Remove a product: ")
                self.remove()
            print(" ")

    def add(self):
        nume = input("Name: ")
        cantitate = console.getNr("Quantity: ")
        try:
            self.__contr.addProduct(nume,cantitate)
        except RepositoryException as e:
            print(e.args)
        except ValidationException as e:
            for i in e.args:
                print(i[0])

    def remove(self):
        id = console.getNr("Product Id: ")
        try:
            self.__contr.removeProduct(id)
        except RepositoryException as e:
            print(e.args[0])
