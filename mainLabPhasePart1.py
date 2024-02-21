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


count = 0
mark = ''
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def check_move(number):
    global count
    global mark

    if number == '1' and '1' in digits:
        digits.remove('1')
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        count += 1
        # Mettre à jour le bouton 1 avec la marque (X ou O)
        # Vérifier si le joueur actuel a gagné en appelant la fonction win()
    elif number == '2' and '2' in digits:
        # Répéter le même processus pour les chiffres 2 à 9
    # Répéter pour les chiffres 3 à 9

    if count > 8:
        if not win('X') and not win('O'):
            print("Match nul")
            root.destroy()
root.mainloop()

