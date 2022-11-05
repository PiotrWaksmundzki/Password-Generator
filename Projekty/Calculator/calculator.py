#author: Piotr Waksmundzki
from tkinter import *
import parser
from math import factorial

i = 0
#funkcja wprowadzenia cyfr
def get_variables(num):
    global i
    display.insert(i,num)
    i += 1
#funcja wprowadzenia operatora mat.
def get_operation(operator):
    global i 
    length = len(operator)
    display.insert(i,operator)
    i+=length
#funcja "wyczyść wszystko"
def clear_all():
    display.delete(0,END)
#funkcja obliczenia
def calcualte():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
#funkcja kasowania znaku
def undo():
    entire_string = display.get()
    if len (entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#utworzenie okna
root = Tk()
root.geometry("350x500")
root.resizable(True,True)
root.title("Calculator by P.Waksmundzki")

display = Entry(root, font = 'arial 20 bold', justify= RIGHT)
display.grid(row = 1, columnspan = 6, sticky = N+E+W+S)

#tworzenie przycisków cyfry

Button(root, text= "1", height= 5, width=10, command = lambda :get_variables(1)).grid(row=2,column=0, sticky=N+S+E+W)
Button(root, text= "2", height= 5, width=10, command = lambda :get_variables(2)).grid(row=2,column=1, sticky=N+S+E+W)
Button(root, text= "3", height= 5, width=10, command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)

Button(root, text= "4", height= 5, width=10, command = lambda :get_variables(4)).grid(row=3,column=0, sticky=N+S+E+W)
Button(root, text= "5", height= 5, width=10, command = lambda :get_variables(5)).grid(row=3,column=1, sticky=N+S+E+W)
Button(root, text= "6", height= 5, width=10, command = lambda :get_variables(6)).grid(row=3,column=2, sticky=N+S+E+W)

Button(root, text= "7", height= 5, width=10, command = lambda :get_variables(7)).grid(row=4,column=0, sticky=N+S+E+W)
Button(root, text= "8", height= 5, width=10, command = lambda :get_variables(8)).grid(row=4,column=1, sticky=N+S+E+W)
Button(root, text= "9", height= 5, width=10, command = lambda :get_variables(9)).grid(row=4,column=2, sticky=N+S+E+W)

Button(root, text= "AC", height= 5, width=10, command = lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W)
Button(root, text= "0", height= 5, width=10, command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(root, text= ".", height= 5, width=10, command = lambda :get_variables(".")).grid(row=5,column=2, sticky=N+S+E+W)

#tworzenie przycisków operatrów matemtycznych

Button(root, text= "+", height= 5, width=10, command = lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(root, text= "-", height= 5, width=10, command = lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(root, text= "*", height= 5, width=10, command = lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(root, text= "/", height= 5, width=10, command = lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)

Button(root,text="=", height= 5, width=10, command= lambda :calcualte()).grid(row=6,column=0, sticky=N+S+E+W)
Button(root, text= "(", height= 5, width=10, command = lambda :get_variables("(")).grid(row=6,column=1, sticky=N+S+E+W)
Button(root, text= ")", height= 5, width=10, command = lambda :get_variables(")")).grid(row=6,column=2, sticky=N+S+E+W)
Button(root,text="<-", height= 5, width=10, command= lambda :undo()).grid(row=6,column=3, sticky=N+S+E+W)

root.mainloop()