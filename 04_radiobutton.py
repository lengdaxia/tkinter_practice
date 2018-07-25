import tkinter as tk

window = tk.Tk()

window.title('randio button')
# window.geometry('150x250')

var = tk.StringVar()

label = tk.Label(window,textvariable=var,bg='yellow',width=20)

label.pack()



def print_selection():
    label.config(text=str('you have selected ' + var.get()))

r1 = tk.Radiobutton(window,
                    text='Option A',
                    variable=var,
                    value='A Button',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window,
                    text='Option B',
                    variable=var,
                    value='B Button',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window,
                    text='Option C',
                    variable=var,
                    value='C Button',
                    command=print_selection)
r3.pack()






window.mainloop()