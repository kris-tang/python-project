# -*- coding: UTF-8 -*-
import os
import tkMessageBox
import win32api
from Tkinter import*
#提前安装所需要的库，win32api,Tkinter,以及其他依赖包

ip1='10.55.1.213'#门店打印服务器ip
ip2='10.8.153.253'#门店打印服务器ip
ip3='10.78.38.99'#门店打印服务器ip
ip4='10.78.39.99'#门店打印服务器ip
ip5='10.78.30.99'#门店打印服务器ip
ip6='10.78.4.99'#门店打印服务器ip

def PING(IP):
    return os.system('ping %s -n 1'%IP)

root = Tk() # 创建窗口
#root.geometry('350x300+500+200')#设置窗口的大小宽x高+偏移量，本例不设置
root.iconbitmap('c:/Python27/DLLs/py.ico')#设置窗口左上角图标
root.title("同程打印机安装程序")#设置窗口标题
root['bg'] = 'gray'#设置窗口背景色

Button(text="请选择门店",command=lambda:PING() ).grid(row=0,column=0)
Button(text="确保网络畅通",command=lambda:PING() ).grid(row=0,column=1)
Button(text="太原区域中心",width=15,command=lambda: TYQY()).grid(row=1,column=0)
Button(text="太原人民路",width=15,command=lambda: TYRML()).grid(row=1,column=1)
Button(text="太原水西关",width=15,command=lambda: TYSXG()).grid(row=2,column=0)
Button(text="太原胜利街",width=15,command=lambda: TYSLJ()).grid(row=2,column=1)
Button(text="大同魏都大道",width=15,command=lambda: DAWDDD()).grid(row=3,column=0)
Button(text="临汾花果街",width=15,command=lambda: LFHGJ()).grid(row=3,column=1)
def TYQY():#定义一个无参函数
    if PING(ip1) == 0 :#判断能否与打印机通讯
        win32api.ShellExecute(0,'open','C:\\dayinji\\tyqy.bat','','',1)#路径为两斜杠\\
        tkMessageBox.showwarning(title='提示', message='安装成功')
        exit()
    else:
        tkMessageBox.showerror('警告', '网络不通，请检查后重试')
def TYRML():#定义一个无参函数
    if PING(ip2) == 0 :#判断能否与打印机通讯
        win32api.ShellExecute(0,'open','C:\\dayinji\\tyrml.bat','','',1)##路径为两斜杠\\
        tkMessageBox.showwarning(title='提示', message='安装成功')
        exit()
    else:
        tkMessageBox.showerror('警告', '网络不通，请检查后重试')

def TYSXG():#定义一个无参函数
    if PING(ip3) == 0 :#判断能否与打印机通讯
        win32api.ShellExecute(0,'open','C:\\dayinji\\tysxg.bat','','',1)##路径为两斜杠\\
        tkMessageBox.showwarning(title='提示', message='安装成功')
        exit()
    else:
        tkMessageBox.showerror('警告', '网络不通，请检查后重试')

def TYSLJ():#定义一个无参函数
    if PING(ip4) == 0 :#判断能否与打印机通讯
        win32api.ShellExecute(0,'open','C:\\dayinji\\tyslj.bat','','',1)##路径为两斜杠\\
        tkMessageBox.showwarning(title='提示', message='安装成功')
        exit()
    else:
        tkMessageBox.showerror('警告', '网络不通，请检查后重试')

def DAWDDD():#定义一个无参函数
    if PING(ip5) == 0 :#判断能否与打印机通讯
        win32api.ShellExecute(0,'open','C:\\dayinji\\dtwddd.bat','','',1)##路径为两斜杠\\
        tkMessageBox.showwarning(title='提示', message='安装成功')
        exit()
    else:
        tkMessageBox.showerror('警告', '网络不通，请检查后重试')
def LFHGJ():#定义一个无参函数
    if PING(ip6) == 0 :#判断能否与打印机通讯
        win32api.ShellExecute(0,'open','C:\\dayinji\\lfhgj.bat','','',1)##路径为两斜杠\\
        tkMessageBox.showwarning(title='提示', message='安装成功')
        exit()
    else:
        tkMessageBox.showerror('警告', '网络不通，请检查后重试')




root.mainloop()


