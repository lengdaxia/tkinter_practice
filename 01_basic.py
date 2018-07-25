
import tkinter as tk

window = tk.Tk()

window.title('basic window')

window.geometry("200x100")




label = tk.Label(window,
                 text='This is a label',
                 bg='green',
                 font=('Arial',12),
                 width=15,height=2)
label.pack()


window.mainloop()


