from tkinter import *

NORM_FONT = ("Helvetica", 10)

def errorPopUp(msg):
    popup = Tk()
    popup.title("Error")
    popup.geometry("300x100+500+500")
    popup.resizable(False, False)

    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command=popup.destroy)
    B1.pack()

    popup.mainloop()

def successPopUp(msg):
    popup = Tk()
    popup.title("Sucesso")
    popup.geometry("300x100+50+50")
    popup.resizable(False, False)

    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command=popup.destroy)
    B1.pack()

    popup.mainloop()

def login(userName, password):
    if userName == '' or password == '':
        errorPopUp('Digite todos os campos!')
    elif userName == 'admin' and password == '12345':
        successPopUp('Logado!')
    else:
        errorPopUp('Verifique as credenciais!')
