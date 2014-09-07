__author__ = 'Roland'

class Question:
    """Descriere"""
    def __init__(self, number, questionText, correctAnswer):
        self.__number = number
        self.__questionText = questionText
        self.__correctAnswer = correctAnswer

    def getNumber(self):
        return self.__number
    def setNumber(self,value):
        self.__number = value 
    number = property(getNumber,setNumber)

    def getQuestionText(self):
        return self.__questionText
    def setQuestionText(self,value):
        self.__questionText = value 
    questionText = property(getQuestionText,setQuestionText)

    def getCorrectAnswer(self):
        return self.__correctAnswer
    def setCorrectAnswer(self,value):
        self.__correctAnswer = value 
    correctAnswer = property(getCorrectAnswer,setCorrectAnswer)

