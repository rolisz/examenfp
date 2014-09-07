__author__ = 'Roland'

class Answer:
    """Descriere"""
    def __init__(self, studentAnswer,question):
        self.__studentAnswer = studentAnswer
        self.__question = question

    def getStudentAnswer(self):
        return self.__studentAnswer
    def setStudentAnswer(self,value):
        self.__studentAnswer = value 
    studentAnswer = property(getStudentAnswer,setStudentAnswer)

    def getQuestion(self):
        return self.__question
    def setQuestion(self,value):
        self.__studentAnswer = value
    question = property(getQuestion,setQuestion)

