from repository.WordRepository import WordRepository
from ui.ScrambleController import ScrambleController
from ui.Administer import Administer
from ui.Play import Play

__author__ = 'Roland'

class ScrambleApplication:

    def __init__(self,administer,play):
        self.__admin = administer
        self.__play = play

    def main(self):
        opt = 0
        while opt != 3:
            print('Alegeti o optiune:')
            print('1. Administer')
            print('2. Play')
            print('3. Iesire')
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
                self.__admin.main()
            if opt == 2:
                self.__play.main()

repo = WordRepository()
contr = ScrambleController(repo)
app = ScrambleApplication(Administer(contr),Play(contr))
app.main()

