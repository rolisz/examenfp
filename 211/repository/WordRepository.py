from model.word import Word

__author__ = 'Roland'

class WordRepository:
    """Reprezinta un container pentru lista de cuvinte. Cuvintele sunt citite din fisierul words.txt"""

    def __init__(self):
        self.__list = []
        self.__maxID = 1
        try:
            file = open('words.txt')
            for line in file:
                line = line.split(" ")
                if len(line) == 3:
                    word = Word((int(line[0])),line[1],int(line[2]))
                    if word.getId() > self.__maxID:
                        self.__maxID = word.getId()
                    self.__list.append(word)
            file.close()
        except IOError as e:
            self.__list = []

    def findByID(self,id):
        for word in self.__list:
            if word[0] == id:
                return word
        else:
            return -1

    def add(self,word):
        for words in self.__list:
            if words.getId() == word.getId():
                raise IndexError("Exista deja cuvant cu acest id")
            if words.getValue() == word.getValue():
                raise ValueError("Exista deja acest cuvant")
        self.__list.append(word)
        self.__maxID = word.getId() +1 if word.getId() > self.__maxID else self.__maxID+1
        file = open('words.txt','a')
        file.write(str(word.getId())+" "+word.getValue()+" "+str(word.getPoints())+"\n")
        file.close()

    def findAll(self):
        return self.__list

    def getNewID(self):
        return self.__maxID + 1