import tkinter as tk
import time

def TalkSet():

    def send():
        recv_text.config(state = 'normal')
        recv_text.insert(tk.END,'{}'.format(time.ctime())+'\n')
        recv_text.insert(tk.END,'{}'.format(send_text.get(0.0,tk.END))+'\n')
        recv_text.config(state='disable')
        send_text.delete(1.0,tk.END)
    root = tk.Tk()
    root.title('修真聊天群')
    root.geometry('600x500')

    recv_text = tk.Text(root,stat = 'disable')
    recv_text.pack()

    send_text = tk.Text(root,height = 10)
    send_text.pack()
    send_button = tk.Button(root,command = send ,text = '发送',width = 10).pack()
    root.mainloop()


if __name__ == '__main__':
    TalkSet()