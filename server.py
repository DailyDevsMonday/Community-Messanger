# -*- coding: utf-8 -*-

# from imp import reload
import socket
from tkinter import *

# Кирилица
# reload(sys)
# sys.setde
# -----------------------------

tk = Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', 11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

text = StringVar()
name = StringVar()
name.set('')
text.set('')
tk.title('Chat')
tk.geometry('400x300')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both', expand='true')

def loopproc():
    s.setblocking(False)

    try:
        bmessage = s.recv(128)
        message = bmessage.decode()
        log.insert(END, message+ '\n')
    except:
        tk.after(1, loopproc)
        return

    tk.after(1,loopproc)
    return

def sendproc(event):
    message = '{name}:{text}'.format(name=name.get(), text=text.get())
    bmessage = message.encode()
    sock.sendto(bmessage, ('255.255.255.255', 11719))
    text.set('')

msg.bind('<Return>', sendproc)

# msg.focus_set()

tk.after(1, loopproc)
tk.mainloop()