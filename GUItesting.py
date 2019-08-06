import tkinter

window = tkinter.Tk()
window.title('my window')
window.geometry('500x500')

lists = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#窗口

lable_1 = tkinter.Label(window,
    text=str(lists[0][0])+str(lists[0][1])+str(lists[0][2]),    # 标签的文字
    bg='white',                 # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=3, height=3          # 标签长宽
    )
lable_1.pack()

lable_2 = tkinter.Label(window,
    text=str(lists[1][0])+str(lists[1][1])+str(lists[1][2]),    # 标签的文字
    bg='white',                 # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=3, height=3          # 标签长宽
    )
lable_2.pack()

lable_3 = tkinter.Label(window,
    text=str(lists[2][0])+str(lists[2][1])+str(lists[2][2]),                   # 标签的文字
    bg='white',                   # 背景颜色
    font=('Arial', 12),         # 字体和字体大小
    width=3, height=3          # 标签长宽
    )
lable_3.pack()







#结束
window.mainloop()
