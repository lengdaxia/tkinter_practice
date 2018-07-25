import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')



e = tk.Entry(window,show='*')
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)


b1 = tk.Button(window,text='Insert point',width=15,height=2,command=insert_point)
b1.pack()

b1 = tk.Button(window,text='Insert end',width=15,height=2,command=insert_end)
b1.pack()


t = tk.Text(window,height=2,bg='red')
t.pack()


window.mainloop()