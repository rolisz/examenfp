from model.Question import Question

__author__ = 'Roland'

class QuestionRepository:
    """Descriere"""
    def __init__(self):
        self.__list = [] 
        self.read() 

    def read(self):
        try:
            file = open("Question.txt")
            line = file.readline()
            while line != "":
                try:
                    number = int(line)
                    text = file.readline()
                    answer = file.readline().strip()
                    question = Question(number,text,answer)
                    self.__list.append(question)
                except TypeError as e:
                    pass
                line = file.readline()
            file.close()
        except IOError as e:
            print("Nu a fost gasit fisierul de date Question.txt")

    def getQuestionCount(self):
        return len(self.__list)

    def findByNumber(self,nr):
        for q in self.__list:
            if q.number == nr:
                return q
        return -1
