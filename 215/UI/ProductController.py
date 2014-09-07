__author__ = "Roland"

import UI.console as console
from domain.Product import Product

class ProductController:
    """Controllerul aplicatiei"""

    def __init__(self, ProductRepository):
        self.__repo = ProductRepository

    def getAllProducts(self):
        return self.__repo.findAll()

    def addProduct(self,name,quantity):
        product = Product(self.__repo.newID(),name.strip(),quantity)
        self.__repo.update(product)

    def removeProduct(self,productId):
        self.__repo.remove(productId)




