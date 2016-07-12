# -*- coding:utf-8 -*-

from Tkinter import *
from tkMessageBox import *
import os


filename = ''
#
def about():
    tkMessageBox.showinfo('关于记事本，版权归属呵呵所有')
# 新建文件
def New():
    global filename
    filemenu = None
    root.title('无标题')
    txt.delete(1.0,END)

def Open():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title(os.path.basename(filename)+' - 记事本')
        txt.delete(1.0,END)
        f = open(filename)
        txt.insert(1.0,f.read().decode('gbk'))
        f.close()
def Save():
    global filename
    try:
        f = open(filename,'w')
        msg = txt.get(1.0,END)
        f.write(msg.encode('gbk'))
        f.close()
    except Exception:
        Saves()

def Saves():
    global filename
    filename = asksaveasfilename(initialtfile=u'未命名.txt',defaultextension='.txt')
    f = open(filename,'w')
    msg = txt.get(1.0,END)
    f.write(msg)
    f.close()
    root.title(os.path.basename())

# -------------------------主窗体 ----------------------------------
root = Tk()     # 窗口
root.title('个人记事本\\')
root.geometry('1024x768')
root.mainloop() # 结尾

# --------------------------菜单--------------------------------
me = Menu()
root.config(menu=me)
filemenu = Menu(me)
filemenu.add_command(label='新建',accelerator='Ctrl+N', command=New)
filemenu.add_command(label='打开',accelerator='Ctrl+O', command=Open)
filemenu.add_command(label='保存',accelerator='Ctrl+S', command=Save)
filemenu.add_command(label='另存为',accelerator='Ctrl+Shift+S', command=Saves)
filemenu.add_separator()    #下划线
filemenu.add_command(label='页面设置',accelerator='U')
filemenu.add_command(label='打印',accelerator='Ctrl+P')
filemenu.add_separator()    #下划线
filemenu.add_command(label='退出',accelerator='X', command=root.quit)

me.add_cascade(label='文件',menu=filemenu)




txt = Text(root,undo=True)
txt.pack(expand=YES, fill=BOTH)



