from UI.CurrentTestUi import CurrentTestUi
from UI.TestController import TestController
from UI.TestHistoryUi import TestHistoryUi
from repository.QuestionRepository import QuestionRepository
from repository.TestRepository import TestRepository

__author__ = 'Roland'

import UI.console as console

class TestApplication:
    """Descriere"""
    def __init__(self):
        self.__contr = TestController(QuestionRepository(),TestRepository())
        self.__history = TestHistoryUi(self.__contr)
        self.__current = CurrentTestUi(self.__contr)

    def main(self):
        opt = 0
        while opt != 3:
            print("Alegeti o optiune")
            print("1. Test nou")
            print("2. Sumar al rezultatelor")
            print("3. Inapoi")
            opt = console.getNr()
            if opt == 1:
                self.__current.new()
            if opt == 2:
                self.__history.show()

app = TestApplication()
app.main()