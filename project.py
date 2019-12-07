from random import *
from sympy import *
import math
from sympy.abc import a, x, y
from sympy import init_printing
x, y, z, t = symbols('x y z t')

def del_tühikud(a):
    b=''
    for i in a:
        if i==' ':
            continue
        b+=i
    return b  
def test():
    i=0
    j=0
    teema = input("Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ")
    while teema == 'integraal':
        funktsioonid = [((randint(1,100)*x+randint(1,100))**randint(2,10)),(randint(1,100)/(randint(1,100)*x)),((cos(x)**randint(1,3))*(sin(x)**randint(1,3))), (log(pi+randint(1,10))*cos(x)**randint(0,3)),]
        i =randint(0,3)
        funktsioon = funktsioonid[i]
        esimene_ülesanne = print("Sinu ülesanne: integreeri funktsiooni ")
        esimene_ülesanne = pprint(funktsioon)
        esimene_ülesanne = print("Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47")
        tulemus = del_tühikud(str(integrate(funktsioon,x,manual=True)))
        from tkinter import *


def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="black")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")

        display = StringVar()
        # relief can be FLAT or RIDGE or RAISED or SUNKEN GROOVE
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='darkgray').pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in (["CE"], ["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(""))
        for numBut in ("789/", "456*", "123-", "0.+"):
            functionNum = iCalc(self, TOP)
            for char in numBut:
                button(functionNum, LEFT, char, lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))
        equalButton = iCalc(self, TOP)
        for iEqual in "=":
            if iEqual == "=":
                btniEqual = button(equalButton, LEFT, iEqual)
                btniEqual.bind("<ButtonRelease-1>", lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btniEqual = button(equalButton, LEFT, iEqual, lambda storeObj=display, s='%s' % iEqual: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    app().mainloop()

        vastus = del_tühikud(input("Sisesta vastust: "))
        if vastus == tulemus:
            otsus = input("Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ")
            if otsus == 'ei':
                print("Oli meeldiv sinuga töötada, edu õppimises! ")
                return False
            else:
                teema = input("Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ")
        while vastus != str(tulemus):
            vastus = del_tühikud(input("Vale vastus! Kui soovid näha õiget vastust siis sisesta 'näita'. Kui soovid jätkata siis proovi veel korra! Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47 või sin(x)**4/4. Sisesta vastus uuesti : "))
            if vastus == str(tulemus):
                otsus = input("Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ")
                if otsus == 'ei':
                    print("Oli meeldiv sinuga töötada, edu õppimises! ")
                    return False
            if vastus == 'näita':
                print("Õige vastus on: ")
                pprint(integrate(funktsioon,x,manual=True))
                print("või: ", '\n',integrate(funktsioon,x,manual=True), '\n')
                otsus = input("Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ")
                if otsus == 'ei':
                    print("Oli meeldiv sinuga töötada, edu õppimises! ")
                    return False
                else:
                    teema = input("Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ")
                    break
    while teema=='tuletis':
        funktsioonid=[randint(1,100)*x**randint(2,10),randint(1,100)**x]
        print('Sinu ülesanne: leia funktsiooni tuletis')
        pprint(funktsioonid[i])
        vastus=del_tühikud(input('Sisesta vastust: '))
        tulemus=del_tühikud(str(diff(funktsioonid[i])))
        if vastus!= str(tulemus):
            while vastus!=str(tulemus):
                vastus = input("Vale vastus! Kui soovid näha õiget vastust siis sisesta 'näita'. Kui soovid jätkata siis proovi veel korra! Sisesta vastus uuesti : ")
                if vastus=='näita':
                    print("Õige vastus on: ")
                    pprint(diff(funktsioonid[i]))
                    print("või: ", '\n',diff(funktsioonid[i]), '\n')
                    break
            otsus = input("Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ").strip()
        if vastus==str(tulemus):
            otsus = input("Sinu vastus oli õige! Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ").strip()
        if otsus == 'ei':
            print("Oli meeldiv sinuga töötada, edu õppimises! ")
            break
        else:
            teema = input("Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ").strip()
        i+=1


test()

