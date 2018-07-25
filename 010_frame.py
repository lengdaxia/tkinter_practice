import tkinter as tk

window = tk.Tk()
window.title('frame use')
window.geometry('200x200')

l1 = tk.Label(window,text='this is the window area')
l1.pack()

bgframe = tk.Frame(window,bg='gray')
bgframe.pack()


leftframe = tk.Frame(bgframe,bg = 'red')
leftframe.pack(side='left')

rightframe = tk.Frame(bgframe,bg = 'blue')
rightframe.pack(side='right')


l2 = tk.Label(leftframe,text='this is the leftframe area',bg='yellow')
l2.pack()

l3 = tk.Label(rightframe,text='this is the rightframe area')
l3.pack()


window.mainloop()