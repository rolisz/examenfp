__author__ = 'Roland'

def getNr(text="Dati un numar",max = 0):
    while True: 
        try:
            nr = int(input())
            if nr not in range(1,max) and max != 0 : 
                print("Trebuie sa alegeti una din optiunile date")
            else: 
                return nr 
        except TypeError: 
            print("Trebuie sa dati un numar intreg")
