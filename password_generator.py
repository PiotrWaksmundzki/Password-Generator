# autor: Piotr Waksmundzki

# pobranie wymaganych biblitek
from tkinter import *
import random, string
import pyperclip

#funkcja generator hasła
def Generator():
    password = ""

    for x in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)
    return password

#funcja kopiowanie hasła
def Copy_password():
    pyperclip.copy(pass_str.get())


#utworzenie okna GUI
root = Tk()
root.geometry("350x400")
root.resizable(True,True)
root.title("Password Generator by Piotr Waksmundzki") # wstążka

#stworzenie dynamicznej siatki w układzie NSEW
Grid.rowconfigure(root,0,weight=1)
Grid.rowconfigure(root,1,weight=1)
Grid.rowconfigure(root,2,weight=1)
Grid.rowconfigure(root,3,weight=1)
Grid.rowconfigure(root,4,weight=1)
Grid.rowconfigure(root,5,weight=1)
Grid.rowconfigure(root,6,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,2,weight=1)


#paramentry nagłówka
head = Label(root, text = "Password Generator", font = 'arial 15 bold').grid(row=0,column=1, sticky=N+S+E+W)

#określenie długości hasła
pass_label = Label(root, text = "Password Lenght", font = 'arial 10 bold').grid(row=1,column=1, sticky=N+S+E+W)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width = 20).grid(row=2,column=1, sticky=N+S+E+W)

#przyciski
pass_str = StringVar()
Button(root, text = "Generate Password", command = Generator).grid(row=3,column=1, sticky=N+S+E+W)
Entry(root, textvariable = pass_str).grid(row=4,column=1, sticky=N+S+E+W)

Button(root, text = 'Copy to clipboard', command = Copy_password).grid(row=5,column=1, sticky=N+S+E+W)

#petla uruchamiająca program
root.mainloop()