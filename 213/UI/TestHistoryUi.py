__author__ = 'Roland'

import UI.console as console

class TestHistoryUi:
    """Descriere"""
    def __init__(self,contr):
        self.__contr = contr

    def show(self):
        tests = self.__contr.getAllTests()
        for test in tests:
            correct = 0
            for answer in test.getAnswers():
                if answer.studentAnswer == self.__contr.getQuestionById(answer.question).correctAnswer:
                    correct +=1
            print("Testul "+str(test.number)+" - " + str(correct) + " raspunsuri corecte din " + str(test.noOfQuestions ))
