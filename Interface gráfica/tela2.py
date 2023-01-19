from tkinter import *
janela = Tk()

rotulo = Label(janela,text="Olá, Mundo!")
rotulo.grid(row=0, column=0)
rotulo["font"] = ("Arial", "18","bold","italic")
rotulo["fg"] = "red"
rotulo["bg"] = "yellow"

pergunta = Label(janela,text="Tudo bem?")
pergunta.grid(row=1, column=1)

botao_sair = Button(janela)
botao_sair.grid(row=2, column=2)
botao_sair["text"] ="SAIR"
botao_sair["width"] = 10
botao_sair["command"] = quit
botao_sair["fg"] = "blue"
janela.mainloop()