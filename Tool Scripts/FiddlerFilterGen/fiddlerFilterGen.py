# -*- coding:utf8 -*-
import Tkinter
import tldextract
import tkMessageBox

def ctext_selectall(self, callback):
    """Select all text in the text widget"""
    self.txt_text.tag_add('sel', '1.0', 'end')  //TODO

def convert():

    result = ""

    if e1.get()=="":
        tkMessageBox.showinfo("错误","请粘贴网址列表！")
    else:
        urls = e1.get()
        urllist =  urls.split('\n')
        for i in urllist:
            if i != "":
                t = tldextract.extract(i)
                if t.suffix != "":
                    if t.subdomain == "":
                        result += t.domain+"."+t.suffix+";"
                    i = "*."+t.domain+"."+t.suffix
                    result=result+i+";"
                else:
                    i = t.domain
                    result=result+i+";"
    print result
    print type(result)
    text1.delete(1.0, Tkinter.END)
    text1.insert(Tkinter.END,result)

    r = Tkinter.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(result)
    r.destroy()


top = Tkinter.Tk()
top.title("Fiddler过滤列表生成器")
top.geometry("+400+400")
top.resizable(width=True,height=True)#

Tkinter.Label(top,text="粘贴待转换列表：").grid(row=0)
Tkinter.Label(top,text="生成到剪贴板：").grid(row=1)

e1 = Tkinter.Entry(top,fg='#000',bg='#204030')  
text1 = Tkinter.Text(top,height=20, width=30,bg='beige')
#text1 = Tkinter.ScrolledText(top, wrap='word',height=20, width=30,bg='beige')
# scroll = Scrollbar(top, command=text1.yview)
# text1.configure(yscrollcommand=scroll.set)


e1.grid(row=0,column=1)
text1.grid(row=1,column=1)

b1 = Tkinter.Button(top,text='转换',width='12',height='1',command = convert)
b1.grid(columnspan=2,row=2)

top.mainloop()