__author__ = 'Roland'

class Play:

    def __init__(self,contr):
        self.__contr = contr

    def main(self):
        opt = 0
        while opt != 2:
            print("Scorul este: ")
            print(self.__contr.getScore())

            print('Alegeti o optiune:')
            print('1. Ghiceste cuvant')
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
                self.guess()

    def guess(self):
        print(self.__contr.newGame())
        trial = input("Care este acest cuvant?")
        while not self.__contr.guess(trial):
            print("Ati gresit. Mai incercati o data")
            trial = input("Care este acest cuvant?")

