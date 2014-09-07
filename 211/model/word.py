__author__ = 'Roland'

class Word:
    """Reprezinta o entitate cuvant, cu proprietatile id, value, points"""

    def __init__(self,id,value,points):
        self.__id = id
        self.__value = value
        self.__points = points

    def getId(self): return self.__id

    def setId(self,id): self.__id = id

    def getValue(self): return self.__value

    def setValue(self,value): self.__value = value

    def getPoints(self): return self.__points

    def setPoints(self,points): self.__points = points

