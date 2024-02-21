from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIC-TAC-TOE")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ''
count = 0

panels = ['panel'] + [' '] * 9

# Suite
def win(player):
    if (panels[1] == panels[2] == panels[3] == player or
            panels[4] == panels[5] == panels[6] == player or
            panels[7] == panels[8] == panels[9] == player or
            panels[1] == panels[4] == panels[7] == player or
            panels[2] == panels[5] == panels[8] == player or
            panels[3] == panels[6] == panels[9] == player or
            panels[1] == panels[5] == panels[9] == player or
            panels[3] == panels[5] == panels[7] == player):
        return True
    return False


def check(num):
    global count, mark, chiffres
    if num in digits:
        count += 1
        digits.remove(num)

        if count % 2 == 0:
            mark = 'O'
            panels[num] = 'O'
        else:
            mark = 'X'
            panels[num] = 'X'

        if count >= 5:
            if win(mark):
                messagebox.showinfo("Game Over", f"Player {mark} wins!")
                root.destroy()

        if count == 9 and not win(mark):
            messagebox.showinfo("Game Over", "Match Tied")
            root.destroy()

        updatePanelButtons()


def updatePanelButtons():
    for i in range(1, 10):
        if panels[i] != ' ':
            buttons[i - 1].config(text=panels[i])


buttons = []
for i in range(1, 10):
    btn = Button(root, text=' ', width=10, height=5, command=lambda i=i: check(i))
    btn.grid(row=(i - 1) // 3, column=(i - 1) % 3)
    buttons.append(btn)

root.mainloop()
