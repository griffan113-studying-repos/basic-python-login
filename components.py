from tkinter import *
from functions import login

"""ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True"""

def renderComponents(app):
    # Containes

    userContainer = Frame(app)
    userContainer.pack(padx=10, pady=40)

    passContainer = Frame(app)
    passContainer.pack(padx=10, pady=10)

    # Widgets

    usuarioLabel = Label(userContainer, text="Digite o usuário")
    usuarioLabel.pack(ipadx=20, ipady=20, padx=5, pady=5, side=LEFT)

    usuarioInputVar = StringVar()
    usuarioInput = Entry(userContainer, textvariable=usuarioInputVar)
    usuarioInput.pack(ipadx=10, ipady=10, padx=5, pady=5, side=LEFT)

    passLabel = Label(passContainer, text="Digite a senha", fg="#000")
    passLabel.pack(ipadx=20, ipady=20, padx=5, pady=5, side=LEFT)

    passInputVar = StringVar()
    passInput = Entry(passContainer, textvariable=passInputVar, show="*")
    passInput.pack(ipadx=10, ipady=10, padx=5, pady=5, side=LEFT)

    botao = Button(app, text="Enviar", command=lambda: login(usuarioInputVar.get(), passInputVar.get()))
    botao.pack(ipadx=10, ipady=7, padx=5, pady=50)
