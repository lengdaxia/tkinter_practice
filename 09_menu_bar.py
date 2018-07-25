import tkinter as tk

window = tk.Tk()
window.title('custom menu bar')
window.geometry('200x200')


label = tk.Label(window,
                 text='menu handle',
                 bg='yellow',
                 height=2)
label.pack()

useVar = tk.IntVar()

def show_menu():
    print(useVar.get())
    print(radiobtnvar.get())

# 定义menu。注意，不同系统的menu样式不同

# 1 定义menubar
menubar = tk.Menu(window)
# 2 定义menu
filemenu = tk.Menu(menubar,tearoff=0)
# 3 将menu加入到menubar中
menubar.add_cascade(label='自定义菜单',menu=filemenu)

# 4 添加menuitem
filemenu.add_command(label='新建',command=show_menu)
filemenu.add_command(label='打开',command=show_menu)
filemenu.add_command(label='保存',command=show_menu)


radiobtnvar = tk.StringVar()
# r1 = tk.Radiobutton(window,
filemenu.add_radiobutton(label='radio btn',variable=radiobtnvar,value='哈哈哈',command=show_menu)

# 5 添加分割线 seperator
filemenu.add_separator()

# 6 退出
filemenu.add_command(label='退出',command=window.quit)


# 视图菜单
viewmenu = tk.Menu(menubar,tearoff=0)

# 创建第二项菜单
menubar.add_cascade(label='视图',command=show_menu,menu=viewmenu)

# 命令1
viewmenu.add_command(label='全屏',command=show_menu)
viewmenu.add_checkbutton(label='是否使用？',command=show_menu,variable=useVar,onvalue=999,offvalue=888)

# 分割线
viewmenu.add_separator()

# 定义viewmenu的子菜单
submenu = tk.Menu(viewmenu)
submenu.add_command(label='子菜单1')
submenu.add_command(label='子菜单2')

# viewmen增加子菜单
viewmenu.add_cascade(label='其他',menu=submenu,underline=9)




# final window 设置menu
window.config(menu=menubar)
window.mainloop()