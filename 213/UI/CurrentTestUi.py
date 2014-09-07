from model.Test import Test

__author__ = 'Roland'

import UI.console as console

class CurrentTestUi:
    """Descriere"""
    def __init__(self,contr):
        self.__contr = contr

    def new(self):
        test = self.__contr.newTest()
        self.__currentQuestion = self.__contr.nextQuestion()
        corecte = 0
        i = 0
        while i < Test.noOfQuestions:
            print(self.__currentQuestion.questionText)
            rasp = input()
            print(len(rasp))
            print(len(self.__currentQuestion.correctAnswer))
            if rasp == self.__currentQuestion.correctAnswer:
                corecte +=1
                print("Ati raspuns corect!")
            else:
                print("Ati gresit. Raspunsul corect era: " + self.__currentQuestion.correctAnswer)
            test.addAnswer(self.__currentQuestion.number,rasp)
            self.__currentQuestion = self.__contr.nextQuestion()
            i +=1
        self.__contr.endTest(test)
        print("Felicitari! Ati raspuns corect la "+str(corecte)+" intrebari din "+str(Test.noOfQuestions))
