__author__ = "Roland" 

def getNr(text="Dati un numar",max = 0):
    while True: 
        try:
            nr = int(input(text))
            if nr < 0:
                print("You must give a positive integer")
            else: 
                return nr 
        except ValueError:
            print("You must give an integer")

def getCommand(list):
    while True:
        opt = input()
        if opt in list:
            return opt
        else:
             print("You must choose of one those options")
