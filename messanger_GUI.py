from tkinter import *
import server

tk = Tk()

text = StringVar()
name = StringVar()
name.set(b'Jungerschaft')
text.set(b'')
tk.title('MegaChat')
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
        message = s.recv(128)
        log.insert(END, message+'\n')
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

msg.focus_set()

tk.after(1, loopproc)
tk.mainloop()