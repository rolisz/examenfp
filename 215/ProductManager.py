from domain.ProductValidator import ProductValidator

__author__ = "Roland"

import UI.console as console
from UI.ProductController import ProductController
from UI.ProductList import ProductListUi
from repository.ProductRepository import ProductRepository

class ProductManager:
    """Coordonatorul aplicatiei"""

    def __init__(self):
        self.__validator = ProductValidator()
        self.__repo = ProductRepository(self.__validator)
        self.__contr = ProductController(self.__repo)
        self.__prodUi = ProductListUi(self.__contr)

    def main(self):
        self.__prodUi.run()



app = ProductManager()
app.main()
