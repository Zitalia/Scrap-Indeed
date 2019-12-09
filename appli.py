# coding: utf-8
 
from tkinter import * 
from pagination import *

fenetre = Tk()

letout = LabelFrame(fenetre, text="Indeed GrowthHacker", padx=20, pady=20, background ='black', fg="white")
letout.pack(fill="both", expand="yes")
 
Label(letout, text="Entrez une URL Indeed.fr et recuperez toutes les données de vos recherches en 1 clic", background ='black', fg="white").pack()

framesaisie = LabelFrame(letout, borderwidth=2, text="Entrez votre url", relief=GROOVE, background ='black', fg="white")
framesaisie.pack(side=LEFT, padx=10, pady=10)

valueurl = StringVar() 
entreeurl = Entry(framesaisie, textvariable= valueurl , width=50, bg="grey", font='Helvetica 12 bold')
entreeurl.pack(side=TOP, padx=10, pady=10)
Button(framesaisie, text ='Ourir le Fichier', bg="green").pack(side=LEFT, padx=5, pady=5)
#nbrdetruc = recherchedescrap.__get__
#print(recherchedescrap)
Label(framesaisie, text = "salut" , bg="black", fg="green").pack()

Framebouton = Frame(letout, bg="green", borderwidth=2, relief=GROOVE)
Framebouton.pack(side=RIGHT, padx=10, pady=10)

Button(Framebouton, text ='Recherchez', command = lambda : recherchegroupe(valueurl), relief=SUNKEN, background ='black', fg="white").pack(side=TOP, padx=5, pady=5)
Button(Framebouton, text ='Réinitialisé', command = lambda : entreeurl.delete(0, 'end'), relief=SUNKEN, background ='black', fg="white").pack( padx=5, pady=5)
Button(Framebouton, text ='Quitter', command = fenetre.quit, relief=SUNKEN, background ='black', fg="white").pack(side=BOTTOM, padx=5, pady=5)


fenetre.mainloop()