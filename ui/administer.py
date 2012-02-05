__author__ = 'Roland'

class Administer:

    def __init__(self,contr):
        self.__contr = contr

    def main(self):
        print("Cuvintele din baza de date sunt: ")
        words = self.__contr.getWords()
        for word in words:
            print(word.getValue()+" - "+str(word.getPoints()))
        opt = 0
        while opt != 2:
            print('Alegeti o optiune:')
            print('1. Adauga cuvant')
            print('2. Inapoi')
            goodOpt = False
            while not goodOpt:
                try:
                    nr = int(input())
                    if nr not in [1,2,3]:
                        print("Trebuie sa alegeti una din optiunile date")
                    else:
                        goodOpt = True
                        opt = nr
                except TypeError:
                    print("Trebuie sa dati un numar intreg")
            if opt == 1:
                self.add()

    def add(self):
        value = input("Cuvantul")
        points = input("Points")
        self.__contr.addWord(value,points)