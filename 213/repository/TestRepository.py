__author__ = 'Roland'

class TestRepository:
    """Descriere"""
    def __init__(self):
        self.__list = []

    def save(self,test):
        self.__list.append(test)

    def listTests(self):
        return self.__list
