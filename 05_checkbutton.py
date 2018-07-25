import tkinter as tk

window = tk.Tk()
window.title('checkButton')

label = tk.Label(window,
                 text='      ',
                 bg='yellow',
                 height=2,
                 width=20)
label.pack()


var1 = tk.IntVar()
var2 = tk.IntVar()

def showtext():
    a = var1.get()
    b = var2.get()
    text = ''
    if a == 1 and b == 1:
        text = 'I love both'
    elif a == 1 and b == 0:
        text = 'I love Pyhton'
    elif a == 0 and b == 1:
        text = 'I love C++'
    else:
        text = ''
    label.config(text=text)


c1 = tk.Checkbutton(window,
                    text='Python',
                    variable=var1,
                    onvalue=1,offvalue=0
                    ,command=showtext)
c1.pack()


c2 = tk.Checkbutton(window,
                    text='C++',
                    variable=var2,
                    onvalue=1,offvalue=0
                    ,command=showtext)
c2.pack()

window.mainloop()