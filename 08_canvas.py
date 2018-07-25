import tkinter as tk
window = tk.Tk()


# 创建画布
canvas = tk.Canvas(window,bg='blue',height=100,width=200)
canvas.pack()

# 加载图片
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10,10,anchor='nw',image=image_file)


# 1 画一条直线
x0 = 100;y0=50;x1=180;y1=80
line = canvas.create_line(x0,y0,x1,y1,fill='white')

# 2 一个矩形
rect = canvas.create_rectangle(150,10,200,50,fill='red')


def move_rect():
    canvas.move(image,2,2)

move_btn = tk.Button(window,text='Move',command=move_rect)
move_btn.pack()

window.mainloop()