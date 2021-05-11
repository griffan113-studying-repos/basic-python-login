from tkinter import *
from components import Components

app = Tk()
app.title("Faça Login")
app.minsize("300","400")
app.maxsize("500","400")
app.geometry("500x400")
app.configure(background="#393939")

Components().render_components(app)

app.mainloop()
