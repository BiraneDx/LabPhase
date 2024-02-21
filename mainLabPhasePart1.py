from tkinter import *
from tkinter import messagebox

#  fenêtre Tkinter
root = Tk()
root.title("TIC-TAC-TOE")

#  liste chiffres avec les numéros 1 à 9
chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialisation des variables
mark = ''
count = 0

# liste panneaux avec 10 éléments
panneaux = ['panneau', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

