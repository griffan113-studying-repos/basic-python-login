from tkinter import *
import yaml
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class Functions:
    _font = ("Helvetica", 10)
    _users = None

    def __init__(self):
        self.read_yaml()

    def read_yaml(self):
        with open("users.yaml", 'r') as stream:
            try:
                self._users = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def error_pop_up(self, msg):
        popup = Tk()
        popup.title("Error")
        popup.geometry("300x100+500+500")
        popup.resizable(False, False)

        label = Label(popup, text=msg, font=self._font)
        label.pack(side="top", fill="x", pady=10)
        b1 = Button(popup, text="Ok", command=popup.destroy)
        b1.pack()

        popup.mainloop()

    def success_pop_up(self, msg):
        popup = Tk()
        popup.title("Sucesso")
        popup.geometry("300x100+50+50")
        popup.resizable(False, False)

        label = Label(popup, text=msg, font=self._font)
        label.pack(side="top", fill="x", pady=10)
        b1 = Button(popup, text="Ok", command=popup.destroy)
        b1.pack()

        popup.mainloop()

    def login(self, username, password):
        if username == '' or password == '':
            self.error_pop_up('Digite todos os campos!')

        else:
            for users, args in self._users.items():

                is_admin = args["admin"]
                username = args["name"]
                password = args["password"]

                if is_admin:
                    if username == username and password == password:
                        self.success_pop_up('Logado!')
                    else:
                        self.error_pop_up('Verifique as credenciais!')
