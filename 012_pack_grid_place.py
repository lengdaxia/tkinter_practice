import tkinter as tk

window = tk.Tk()
window.title('frame use')
window.geometry('200x200')
window.minsize(width=200,height=200)
window.maxsize(width=300,height=300)

# pack
# tk.Label(window,text='上').pack(side='top')
# tk.Label(window,text='左').pack(side='left')
# tk.Label(window,text='下').pack(side='bottom')
# tk.Label(window,text='右').pack(side='right')


#grid
for i in range(4):
    for j in range(3):
        tk.Label(window,text='*').grid(row=i,column=j,padx=10,pady=10)



# place
tk.Label(window,text='itkinter',bg='red').place(x=100,y=50,anchor='nw')



# l2 = tk.Label(leftframe,text='this is the leftframe area',bg='yellow')
# l2.pack()
#
# l3 = tk.Label(rightframe,text='this is the rightframe area')
# l3.pack()


window.mainloop()