from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIC-TAC-TOE")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ''
count = 0

panels = ['panel'] + [' '] * 9
