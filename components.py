from tkinter import *
from functions import Functions

# from functions import users

"""ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True"""

funcs = Functions()


class Components:
    def __init__(self):
        pass

    def render_components(self, app):
        # Containers
        usercontainer = Frame(app)
        usercontainer.pack(padx=10, pady=40)

        passcontainer = Frame(app)
        passcontainer.pack(padx=10, pady=10)

        # Widgets

        usuariolabel = Label(usercontainer, text="Digite o usuário")
        usuariolabel.pack(ipadx=20, ipady=20, padx=5, pady=5, side=LEFT)

        usuario_input_var = StringVar()
        usuario_input = Entry(usercontainer, textvariable=usuario_input_var)
        usuario_input.pack(ipadx=10, ipady=10, padx=5, pady=5, side=LEFT)

        pass_label = Label(passcontainer, text="Digite a senha", fg="#000")
        pass_label.pack(ipadx=20, ipady=20, padx=5, pady=5, side=LEFT)

        pass_input_var = StringVar()
        pass_input = Entry(passcontainer, textvariable=pass_input_var, show="*")
        pass_input.pack(ipadx=10, ipady=10, padx=5, pady=5, side=LEFT)

        botao = Button(app, text="Enviar", command=lambda: funcs.login(usuario_input_var.get(), pass_input_var.get()))
        botao.pack(ipadx=10, ipady=7, padx=5, pady=50)
