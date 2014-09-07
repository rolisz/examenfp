from model.Answer import Answer

__author__ = 'Roland'

class Test:
    """Descriere"""

    noOfQuestions = 5
    def __init__(self, number):
        self.__number = number
        self.__answers = []

    def getNumber(self):
        return self.__number
    def setNumber(self,value):
        self.__number = value 
    number = property(getNumber,setNumber)

    def addAnswer(self,question,answer):
        answ = Answer(answer,question)
        self.__answers.append(answ)

    def getAnswers(self):
        return self.__answers