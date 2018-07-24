import tkinter as tk

window = tk.Tk()

window.title("label and button")


# 定义一个label，text是变量
var = tk.StringVar()

label = tk.Label(window,
                 textvariable=var,
                 bg='green',
                 font=('Arial',12)
                 ,width=15,
                 height=12).grid()

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

btn = tk.Button(window,
                text='hit me',
                width=15,height=12,
                command=hit_me).pack()






window.geometry('200x100+200+100')

window.mainloop()