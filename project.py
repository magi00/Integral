from random import *
from sympy import *
import math
from sympy.abc import a, x, y
from sympy import init_printing
x, y, z, t = symbols('x y z t')
import tkinter as tk
from tkinter import simpledialog
application_window = tk.Tk()
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox
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
        print("Sinu ülesanne: integreeri funktsiooni ", '\n')
        pprint(funktsioon, '\n')
        mbox.showerror("Vihje","Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47", parent=application_window)
        tulemus = del_tühikud(str(integrate(funktsioon,x,manual=True)))
        vastus = simpledialog.askstring("Sisesta","Sinu ülesanne on kuvatud ekraanil. Sisesta vastust: ",parent=application_window)
        if vastus == tulemus:
            otsus = simpledialog.askstring("Sisesta","Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ",parent=application_window)
            if otsus == 'ei':
                mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                return False
            else:
                teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
        while vastus != str(tulemus):
            mbox.showerror("Vale vastus!","Vale vastus! Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47 ", parent=application_window)
            vastus = del_tühikud(simpledialog.askstring("Sisesta", "Kui soovid näha õiget vastust siis sisesta 'näita'. Kui soovid jätkata siis proovi veel korra! Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47 või sin(x)**4/4. Sisesta vastus uuesti : ",parent=application_window))
            if vastus == str(tulemus):
                otsus = simpledialog.askstring("Sisesta", "Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ",parent=application_window)
                if otsus == 'ei':
                    mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                    return False
            if vastus == 'näita':
                print('\n', "Õige vastus on: ", '\n')
                pprint(integrate(funktsioon,x,manual=True))
                print( '\n', "või: ", '\n', '\n',integrate(funktsioon,x,manual=True), '\n')
                otsus = simpledialog.askstring("Sisesta", "Õige vastus on kuvatud ekraanil. Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window)
                if otsus == 'ei':
                    mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                    return False
                elif otsus == 'jah':
                    teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
                    break
                else:
                    while True:
                        mbox.showerror("Error","Ootasin vastust kas 'jah' või 'ei'.", parent=application_window)
                        otsus = simpledialog.askstring("Sisesta", "Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window)
                        if otsus == 'jah':
                            return test()
                        else:
                            mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                            return False

    while teema=='tuletis':
        funktsioonid=[randint(1,100)*x**randint(2,10),randint(1,100)**x]
        print('Sinu ülesanne: leia funktsiooni tuletis')
        pprint(funktsioonid[i])
        mbox.showerror("Vihje","Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47", parent=application_window)
        vastus=del_tühikud(simpledialog.askstring("Sisesta",'Sinu ülesanne on kuvatud ekraanil. Sisesta vastust: ',parent=application_window))
        tulemus=del_tühikud(str(diff(funktsioonid[i])))
        if vastus == tulemus:
            otsus = simpledialog.askstring("Sisesta","Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ",parent=application_window)
            if otsus == 'ei':
                mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                return False
            else:
                teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
        while vastus != str(tulemus):
            mbox.showerror("Vale vastus!","Vale vastus! Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47 ", parent=application_window)
            vastus = del_tühikud(simpledialog.askstring("Sisesta", "Kui soovid näha õiget vastust siis sisesta 'näita'. Kui soovid jätkata siis proovi veel korra! Selleks, et automaatkontroll loeks sinu vastust õigeks, pead sisestama enda vastust näiteks sellisel kujul: 35*log(x)/47 või sin(x)**4/4. Sisesta vastus uuesti : ",parent=application_window))
            if vastus == str(tulemus):
                otsus = simpledialog.askstring("Sisesta", "Sinu vastus oli õige! Sisesta 'jah' kui soovid jätkata ning 'ei' kui soovid väljuda: ",parent=application_window)
                if otsus == 'ei':
                    mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                    return False
            if vastus == 'näita':
                print('\n', "Õige vastus on: ", '\n')
                pprint(del_tühikud(str(diff(funktsioonid[i]))))
                print( '\n', "või: ", '\n', '\n',del_tühikud(str(diff(funktsioonid[i]))), '\n')
                otsus = simpledialog.askstring("Sisesta", "Õige vastus on kuvatud ekraanil. Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window)
                if otsus == 'ei':
                    mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                    return False
                elif otsus == 'jah':
                    teema = simpledialog.askstring("Sisesta", "Sina saad valida kaks teemat: kas integraal või tuletis. Sisesta 'integraal' selleks, et lahendada integraali ülesandeid, või siis 'tuletis' selleks, et lahendada tuletis ülesandeid. Sisesta teema: ",parent=application_window)
                    break
                else:
                    while True:
                        mbox.showerror("Error","Ootasin vastust kas 'jah' või 'ei'.", parent=application_window)
                        otsus = simpledialog.askstring("Sisesta", "Kas jätkame? Sisesta 'jah' kui soovid jätkata või sisesta 'ei' kui soovid väljuda: ",parent=application_window)
                        if otsus == 'jah':
                            return test()
                        else:
                            mbox.showerror("Viimane sõnum", "Oli meeldiv sinuga töötada, edu õppimises! ", parent=application_window)
                            return False
            
            
   


test()


