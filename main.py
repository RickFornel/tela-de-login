from cgitb import text
from operator import ne
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from turtle import left

# cores -----------------------------

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# criando janela tkinter

janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.resizable(height=FALSE, width=FALSE)
janela.config(bg=co1)

# criando frames

frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# criando label

label_login = Label(frame_cima, text='LOGIN', fg=co4, bg=co1, anchor=NE, font='Ivy 25 bold')
label_login.place(x=5, y=3)

label_linha = Label(frame_cima, text='', bg=co2, anchor=NW, width=275, font='Ivy 1')
label_linha.place(x=5, y=43)

label_user = Label(frame_baixo, text='NOME: *', font='Ivy 10 bold', fg= co4, bg=co1)
label_user.place(x=15, y=15)

label_pass = Label(frame_baixo, text='SENHA: *', font='Ivy 10 bold', fg= co4, bg=co1)
label_pass.place(x=15, y=100)

# criando entry

entry_user = Entry(frame_baixo, text='', width=40, font='Ivy 10', bg=co0, relief='solid', highlightthickness=1)
entry_user.place(x=10, y=45)

entry_pass = Entry(frame_baixo, text='', width=40, font='Ivy 10', show='*', bg=co0, relief='solid', highlightthickness=1)
entry_pass.place(x=10, y=130)

# criando usuarios

usuario_admin = ['admin', 'admin']
usuario_1 = ['Riquelme', '12345']

# criando funções 

def verificar_user():
    
    user = entry_user.get()
    senha = entry_pass.get()
    
    if user == usuario_admin[0] and senha == usuario_admin[1]:
        messagebox.showinfo('', 'Seja bem vindo Administrador!!!')
        limpar_tela()
        nova_tela()
    elif user == usuario_1[0] and senha == usuario_1[1]:
        messagebox.showinfo('', 'Seja bem vindo ' + usuario_1[0] + '!!!')
        limpar_tela()
        nova_tela()
    else:
        messagebox.showerror('Senha incorreta!', 'Por favor verifique seu usuario e sua senha e tente novamente!')

def limpar_tela():
    for widget in frame_baixo.winfo_children():
        widget.destroy()
    for widget in frame_cima.winfo_children():
        widget.destroy()

def nova_tela():
    label_bv = Label(frame_cima, text='BEM VINDO', fg=co4, bg=co1, anchor=NE, font='Ivy 25 bold')
    label_bv.place(x=5, y=3)

    label_linha1 = Label(frame_cima, text='', bg=co2, anchor=NW, width=275, font='Ivy 1')
    label_linha1.place(x=5, y=43)

    label_nome = Label(frame_baixo, text='É UMA HONRA TE-LO DE VOLTA:  ' + usuario_admin[0], font='Ivy 10 bold', fg= co4, bg=co1)
    label_nome.place(x=15, y=15)


# crinado button

button_entrar = Button(frame_baixo, command=verificar_user, text='ENTRAR', width=35, font='Ivy 10 bold', bg=co2, relief='solid')
button_entrar.place(x=10, y=195)



janela.mainloop()