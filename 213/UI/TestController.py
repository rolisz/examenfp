import random
from model.Test import Test

__author__ = 'Roland'

import UI.console as console

class TestController:
    """Descriere"""
    def __init__(self,qRepo,tRepo):
        self.__qrepo = qRepo
        self.__trepo = tRepo
        self.__testNr = 1

    def nextQuestion(self):
        total = self.__qrepo.getQuestionCount()
        question = -1
        while question == -1:
            questionNr = random.randint(0,total)
            question = self.__qrepo.findByNumber(questionNr)
        print(question)
        return question

    def getAllTests(self):
        return self.__trepo.listTests()

    def newTest(self):
        test = Test(self.__testNr)
        self.__testNr +=1
        return test

    def endTest(self,test):
        self.__trepo.save(test)

    def getQuestionById(self,nr):
        return self.__qrepo.findByNumber(nr)
