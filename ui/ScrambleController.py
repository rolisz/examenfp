import random
from model.word import Word

__author__ = 'Roland'

class ScrambleController:

    def __init__(self,repo):
        self.__score = 0
        self.__repo = repo
        self.__currentWord = Word(0,"",0)

    def getWords(self):
        return self.__repo.findAll()

    def getScore(self):
        return self.__score

    def addWord(self,value, points):
        if value == "":
            print("Cuvantul trebuie sa fie nevid")
        try:
            word = Word(self.__repo.getNewID(),value,int(points))
            self.__repo.add(word)
        except TypeError as e:
            print(e)
            print("Points trebuie sa fie intreg")
        except IndexError as e:
            print(e)
        except  ValueError as e:
            print(e)

    def newGame(self):
        words = self.__repo.findAll()
        print(words)
        self.__currentWord = random.sample(words,1)[0]
        listRepr = list(self.__currentWord.getValue())
        random.shuffle(listRepr)
        return "".join(listRepr)

    def guess(self,wordValue):
        if wordValue == self.__currentWord.getValue():
            self.__score += self.__currentWord.getPoints()
            return True
        else:
            self.__score -= 1
            return False
