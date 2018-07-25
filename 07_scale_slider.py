import tkinter as tk

window = tk.Tk()
window.title('scale-slider')


var = tk.StringVar()

label = tk.Label(window,
                 text='slider value 50',
                 bg='yellow',
                 height=2)
label.pack()


def slide_scaler(v):
    label.config(text='slider value %s' % v)


slider = tk.Scale(window,
                  label='this a slider',
                  from_=1,to=10,
                  orient=tk.HORIZONTAL,
                  length=200,
                  showvalue=50,
                  tickinterval=1,resolution=0.01,
                  command=slide_scaler)
slider.pack()



window.mainloop()