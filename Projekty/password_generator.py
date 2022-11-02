# autor: Piotr Waksmundzki
# pobranie wymaganych biblitek

from tkinter import *
import random, string
import pyperclip

#/utworzenie okna GUI

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Password Generator by Piotr Waksmundzki") # ribbon /wstązka

#paramentry nagłówka

head = Label(root, text = "Password Generator", font = 'arial 15 bold').pack()

#określenie długości hasła

pass_label = Label(root, text = "Password Lenght", font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width = 15).pack()

#funkcja generator hasła

pass_str = StringVar()

def Generator():
    password = ""

    for x in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)
    return password
#przycisk

Button(root, text = "Generate Password", command = Generator).pack(pady = 5)
Entry(root, textvariable = pass_str).pack()

#uncja kopiowanie hasła
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'Copy to clipboard', command = Copy_password).pack(pady = 5)

#petla uruchamiająca program
root.mainloop()