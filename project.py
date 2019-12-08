from random import *
from sympy import *
import math
from sympy.abc import a, x, y
from sympy import init_printing
x, y, z, t = symbols('x y z t')
import tkinter as tk
from tkinter import simpledialog
application_window = tk.Tk()
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
    teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
    while teema == 'integraal':
        funktsioonid = [((randint(1,100)*x+randint(1,100))**randint(2,10)),(randint(1,100)/(randint(1,100)*x)),((cos(x)**randint(1,3))*(sin(x)**randint(1,3))), (log(pi+randint(1,10))*cos(x)**randint(0,3)),]
        i =randint(0,1)
        funktsioon = funktsioonid[i]
        esimene_ülesanne = print("Sinu ülesanne: integreeri funktsiooni ")
        esimene_ülesanne = pprint(funktsioon)
        esimene_ülesanne = print("Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47")
        tulemus = del_tühikud(str(integrate(funktsioon,x,manual=True)))
        vastus = simpledialog.askstring("Sisesta","Sisesta vastust: ",parent=application_window)
        if vastus == tulemus:
            otsus = simpledialog.askstring("Sisesta","Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ",parent=application_window)
            if otsus == 'ei':
                print("Oli meeldiv sinuga töötada, edu õppimises! ")
                return False
            else:
                teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
        while vastus != str(tulemus):
            vastus = del_tühikud(simpledialog.askstring("Sisesta", "Vale vastus! Kui soovid näha õiget vastust siis sisesta 'näita'. Kui soovid jätkata siis proovi veel korra! Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47 või sin(x)**4/4. Sisesta vastus uuesti : ",parent=application_window))
            if vastus == str(tulemus):
                otsus = simpledialog.askstring("Sisesta", "Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ",parent=application_window)
                if otsus == 'ei':
                    print("Oli meeldiv sinuga töötada, edu õppimises! ")
                    return False
            if vastus == 'näita':
                print("Õige vastus on: ")
                pprint(integrate(funktsioon,x,manual=True))
                print("või: ", '\n',integrate(funktsioon,x,manual=True), '\n')
                otsus = simpledialog.askstring("Sisesta", "Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window)
                if otsus == 'ei':
                    print("Oli meeldiv sinuga töötada, edu õppimises! ")
                    return False
                else:
                    teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
                    break
    while teema=='tuletis':
        funktsioonid=[randint(1,100)*x**randint(2,10),randint(1,100)**x]
        print('Sinu ülesanne: leia funktsiooni tuletis')
        pprint(funktsioonid[i])
        vastus=del_tühikud(simpledialog.askstring("Sisesta",'Sisesta vastust: ',parent=application_window))
        tulemus=del_tühikud(str(diff(funktsioonid[i])))
        if vastus!= str(tulemus):
            while vastus!=str(tulemus):
                vastus = simpledialog.askstring("Sisesta","Vale vastus! Kui soovid näha õiget vastust siis sisesta 'näita'. Kui soovid jätkata siis proovi veel korra! Sisesta vastus uuesti : ",parent=application_window)
                if vastus=='näita':
                    print("Õige vastus on: ")
                    pprint(diff(funktsioonid[i]))
                    print("või: ", '\n',diff(funktsioonid[i]), '\n')
                    break
            otsus = simpledialog.askstring("Sisesta","Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window).strip()
        if vastus==str(tulemus):
            otsus = simpledialog.askstring("Sisesta","Sinu vastus oli õige! Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window).strip()
        if otsus == 'ei':
            print("Oli meeldiv sinuga töötada, edu õppimises! ")
            break
        else:
            teema = simpledialog.askstring("Sisesta","Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window).strip()
        i+=1


test()


