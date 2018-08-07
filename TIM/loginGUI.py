import tkinter as tk
from tkinter import messagebox
import socket
import json
def LoginFuc():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect(('192.168.100.40', 9999))
    up =username.get()+' '+password.get()
    s.send(up.encode('utf-8'))
    re = str(s.recv(1024).decode('utf-8'))
    if  re== '1':
        tk.messagebox.showinfo('提示','登录成功')
    elif re == '2':
        tk.messagebox.showinfo('提示','用户名不存在')
    else:
        tk.messagebox.showinfo('提示','密码错误')
    s.close()
if __name__ == '__main__':
    root = tk.Tk()
    root.title('TIM')
    root.geometry('420x290')
    root.resizable(0, 0)

    f1 = tk.Frame(root, width=420, height=290)

    username = tk.StringVar()
    password = tk.StringVar()

    f11 = tk.Frame(f1)
    l1 = tk.Label(f11, text='用户名').pack(side='left')
    logintext = tk.Entry(f11,textvariable = username).pack(side='left')
    f11.pack()

    f12 = tk.Frame(f1)

    l2 = tk.Label(f12, text='密   码').pack(side='left')
    passwordtext = tk.Entry(f12,textvariable = password,show = '*').pack(side='left')
    f12.pack()

    login_button = tk.Button(f1, text='登录', width=25, command=LoginFuc).pack()
    f1.pack()
    root.mainloop()
