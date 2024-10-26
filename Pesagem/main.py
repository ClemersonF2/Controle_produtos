
from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from view import*
from tkinter import messagebox
import tkinter as tk


#cores
co0 = "#038cfc" # azul 
co1 = "#e9edf5" # branco
co2 = "#feffff" # cinza
co3 = "#403d3d" # preto
co4 = "#3CB371" # verde
co5 = "#FF0000" # vermelho


def janela_principal():



    def abrir_janela():
        janela2 = tk.Toplevel()
        janela2.title('')
        janela2.geometry('400x533')
        janela2.configure(background=co1)
        janela2.resizable(width=False, height=False)

        # criando frames----------------------------------------------------------------------------------------------------------------------------------------------------
        frameCima2 = Frame(janela2, width=1043, height=50, bg=co2, relief=FLAT)
        frameCima2.grid(row=0, column=0)

        frameMeio2 = Frame(janela2, width=1043, height=303, bg=co2, pady=20, relief=FLAT)
        frameMeio2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        frameBaixo2 = Frame(janela2, width=1043, height=300, bg=co2,relief=FLAT)
        frameBaixo2.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)



        # Abrindo imagem ----------------------------------------------------------------------------------------------------------------------------------------------------
        app_img2 = Image.open('tcalculadora.png')
        app_img2 = app_img2.resize((45,45))
        app_img2 = ImageTk.PhotoImage(app_img2)
        #titulo do app-------------------------------------------------------------------------------------------------------------------------------------------------------
        app_logo = Label(frameCima2, image=app_img2, text='Pesagem de Produtos', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('verdana 20 bold'), bg=co2, fg=co3)
        app_logo.place(x=0, y=0)

        # criando as entradas-------------------------------------------------------------------------------------------------------------------------------------------------
        l_pesoBruto = Label(frameMeio2, text='PESO BRUTO', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoBruto.place(x=10, y=10)
        e_pesobruto = Entry(frameMeio2 , width=30, justify='left', relief=SOLID)
        e_pesobruto.place(x=130, y=11)

        l_pesoPalete = Label(frameMeio2, text='PESO PALETE', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoPalete.place(x=10, y=40)
        e_pesoPalete = Entry(frameMeio2, width=30, justify='left', relief=SOLID)
        e_pesoPalete.place(x=130, y=41)

        l_qtdCx = Label(frameMeio2, text='QTD DE CAIXA', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_qtdCx.place(x=10, y=70)
        e_qtdCx = Entry(frameMeio2, width=30, justify='left', relief=SOLID)
        e_qtdCx.place(x=130, y=71)

        l_pesoCaixa= Label(frameMeio2, text='PESO DA CAIXA', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoCaixa.place(x=10, y=100)
        e_pesoCaixa = Entry(frameMeio2, width=30, justify='left', relief=SOLID)
        e_pesoCaixa.place(x=130, y=101)

        l_qtdEmb = Label(frameMeio2, text='QTD EMB p/cx', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_qtdEmb.place(x=10, y=130)
        e_qtdEmb = Entry(frameMeio2, width=30, justify='left', relief=SOLID)
        e_qtdEmb.place(x=130, y=131)

        l_pesoEmb = Label(frameMeio2, text='PESO EMB', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoEmb.place(x=10, y=160)
        e_pesoEmb = Entry(frameMeio2, width=30, justify='left', relief=SOLID)
        e_pesoEmb.place(x=130, y=161)

        # botoes-----------------------------------------------------------------------------------------------------------------------------------------

        def limpar():

            e_pesobruto.delete(0,'end')
            e_pesoPalete.delete(0,'end')
            e_qtdCx.delete(0,'end')
            e_pesoCaixa.delete(0,'end')
            e_qtdEmb.delete(0,'end')
            e_pesoEmb.delete(0,'end')
            l_peso_Liquido['text'] = ""
            l_pesoDesconto['text'] = ""
            l_peso_Totalcx['text'] = ""
            l_peso_Totalemb['text'] = ""

        b_limpar = Button(frameMeio2, command= limpar,width=15, text='LIMPAR'.upper(),compound=LEFT, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
        b_limpar.place(x=150, y=210)


        def voltar():
         janela2.destroy()
        b_voltar = Button(frameMeio2,command= voltar,width=15, text='VOLTAR'.upper(),compound=LEFT, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
        b_voltar.place(x=280, y=210)


        def calcular():

        
            pesoCaixa = float (e_pesoCaixa.get())
            qtdCx = int (e_qtdCx.get())
            pesoPalete = float (e_pesoPalete.get())
            pesoEmb = float (e_pesoEmb.get())
            qtdEmb = int (e_qtdEmb.get())
            pesoBruto = float ( e_pesobruto.get())

            '''totalCaixa = pesoCaixa * qtdCx
            totalEmb1cx = pesoEmb * qtdEmb
            totalEmb = totalEmb1cx * qtdCx
            pesoDescontado = totalCaixa + totalEmb + pesoPalete
            pesoLiquido = pesoBruto - pesoDescontado'''

            totalEmb = pesoEmb * qtdEmb *qtdCx
            totalCaixa = pesoCaixa * qtdCx
            pesoDescontado = totalCaixa + totalEmb + pesoPalete
            pesoLiquido = pesoBruto - pesoDescontado

            l_peso_Liquido['text'] = pesoLiquido
            l_pesoDesconto['text'] = pesoDescontado
            l_peso_Totalcx['text'] = totalCaixa
            l_peso_Totalemb['text'] = totalEmb



            e_peso.delete(0,'end')
            e_peso.insert(index='1', string = pesoLiquido)


        b_calcular =Button(frameMeio2, command= calcular ,width=15, text='CALCULAR'.upper(),compound=LEFT, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
        b_calcular.place(x=10, y=210)


        
        l_pesoDescontado = Label(frameBaixo2, text='PESO DESCONTADO: ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoDescontado.grid(row=2, column=0)
        l_pesoDesconto = Label(frameBaixo2, text='',width=8, height=2, anchor=CENTER, font=('Ivy 12 bold'), bg=co2, fg=co5)
        l_pesoDesconto.grid(row=2, column=1)


        l_pesoLiquido = Label(frameBaixo2, text='PESO LIQUIDO:  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoLiquido.grid(row=3, column=0)
        l_peso_Liquido = Label(frameBaixo2, text='',width=8, height=2, anchor=CENTER, font=('Ivy 12 bold'), bg=co2, fg=co4)
        l_peso_Liquido.grid(row=3, column=1)

        l_pesoTotalcx = Label(frameBaixo2, text='CAIXA:  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoTotalcx.grid(row=1, column=0)
        l_peso_Totalcx= Label(frameBaixo2, text='',width=8, height=2, anchor=CENTER, font=('Ivy 12 bold'), bg=co2, fg=co5)
        l_peso_Totalcx.grid(row=1, column=1)

        l_pesoTotalemb = Label(frameBaixo2, text='EMBALAGEM:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
        l_pesoTotalemb.grid(row=0, column=0)
        l_peso_Totalemb= Label(frameBaixo2, text='',width=8, height=2, anchor=CENTER, font=('Ivy 12 bold'), bg=co2, fg=co5)
        l_peso_Totalemb.grid(row=0, column=1)

        janela2 = mainloop()

    # criando janela
    janela = Tk()
    janela.title('')
    janela.geometry('880x600')
    janela.configure(background=co1)
    janela.resizable(width=False, height=False)

    style = ttk.Style(janela)
    style.theme_use("clam")


    # criando frames--------------------------------------------------------------------------------------------------------------------------------------------------
    frameCima = Frame(janela, width=1043, height=50, bg=co2, relief=FLAT)
    frameCima.grid(row=0, column=0)

    frameMeio = Frame(janela, width=1043, height=303, bg=co2, pady=20, relief=FLAT)
    frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frameBaixo = Frame(janela, width=1043, height=300, bg=co2,relief=FLAT)
    frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

    # criando funcoes--------------------------------------------------------------------------------------------------------------------------------------------------
    global tree
    # funcao inserir---------------------------------------------------------------------------------------------------------------------------------------------------
    def inserir():
        
        nome = e_nome.get()
        codigo = e_codigo.get()
        pesoLiquido = e_peso.get()
        recebimento = e_cal.get()
        notaFiscal = e_notaFiscal.get()

        lista_inserir = [nome, codigo, pesoLiquido, recebimento, notaFiscal]

        for i in lista_inserir:
            if i=='':
                messagebox.showerror('Error','Preencha todos os campos')
                return
        
        inserir_form(lista_inserir)

        messagebox.showinfo('Sucesso','Registro realizado com sucesso!')

        e_nome.delete(0,'end')
        e_codigo.delete(0,'end')
        e_notaFiscal.delete(0,'end')
        e_cal.delete(0,'end')
        e_peso.delete(0,'end')

        mostrar()
        
    # funcao atulizar--------------------------------------------------------------------------------------------------------------------------------------------------
    def atualizar():
     try:
        treev_dados = tree.focus()
        treev_dicionario =tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista


        e_nome.delete(0,'end')
        e_codigo.delete(0,'end')
        e_notaFiscal.delete(0,'end')
        e_cal.delete(0,'end')
        e_peso.delete(0,'end')


        id = int(treev_lista[0])
        e_nome.insert(0,treev_lista[1])
        e_codigo.insert(0,treev_lista[2])
        e_notaFiscal.insert(0,treev_lista[3])
        e_cal.insert(0,treev_lista[4])
        e_peso.insert(0,treev_lista[5])

    
        def update():

            nome = e_nome.get()
            codigo = e_codigo.get()
            pesoLiquido = e_peso.get()
            recebimento = e_cal.get()
            notaFiscal = e_notaFiscal.get()

            lista_atulizar = [nome, codigo, pesoLiquido, recebimento, notaFiscal,id]


            for i in lista_atulizar:
                if i=='':

                    messagebox.showerror('Error','Preencha todos os campos')
                    return

            atualizar_form(lista_atulizar)
            messagebox.showinfo('Sucesso','Os dados foram atualizados com sucesso!')

            e_nome.delete(0,'end')
            e_codigo.delete(0,'end')
            e_notaFiscal.delete(0,'end')
            e_cal.delete(0,'end')
            e_peso.delete(0,'end')

            b_confirmar.destroy()

            mostrar()
            
        
        b_confirmar = Button(frameMeio, command= update ,width=13, text='CONFIRMAR'.upper(),overrelief=RIDGE, font=('Ivy 8 bold'), bg=co4, fg=co2)
        b_confirmar.place(x=330, y=185)



     except IndexError:
        messagebox.showerror('Error','Seleciona um dos dados na tabela')
    # funsao deletar --------------------------------------------------------------------------------------------------------------------------------------------------
    def deletar():
     try:
            treev_dados = tree.focus()
            treev_dicionario =tree.item(treev_dados)
            treev_lista = treev_dicionario['values']
            valor = treev_lista[0] 

            deletar_form([valor])    

        
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')


            mostrar()

     except IndexError:
        messagebox.showerror('Erro','Seleciona um dos dados na tabela')

    # Abrindo imagem ---------------------------------------------------------------------------------------------------------------------------------------------------
    app_img = Image.open('balanca.png')
    app_img = app_img.resize((45,45))
    app_img = ImageTk.PhotoImage(app_img)
    #titulo do app-------------------------------------------------------------------------------------------------------------------------------------------------------
    app_logo = Label(frameCima, image=app_img, text='Controle de Produtos', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('verdana 20 bold'), bg=co2, fg=co3)
    app_logo.place(x=0, y=0)

    # criando as entradas -----------------------------------------------------------------------------------------------------------------------------------------------

    l_nome = Label(frameMeio, text='PRODUTO', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
    l_nome.place(x=10, y=10)
    e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
    e_nome.place(x=130, y=11)

    l_codigo = Label(frameMeio, text='CODIGO', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
    l_codigo.place(x=10, y=40)
    e_codigo = Entry(frameMeio, width=30, justify='left', relief=SOLID)
    e_codigo.place(x=130, y=41)

    l_notaFiscal = Label(frameMeio, text='NOTA FISCAL', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
    l_notaFiscal.place(x=10, y=70)
    e_notaFiscal = Entry(frameMeio, width=30, justify='left', relief=SOLID)
    e_notaFiscal.place(x=130, y=71)

    l_cal = Label(frameMeio, text='RECEBIMENTO', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
    l_cal.place(x=10, y=100)
    e_cal= DateEntry(frameMeio, width=12, Background='darkblue', bordewidth=2, year=2024) 
    e_cal.place(x=130, y=101)

    l_peso = Label(frameMeio, text='PESO LIQUIDO', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
    l_peso.place(x=10, y=130)
    e_peso = Entry(frameMeio, width=30, justify='left', relief=SOLID)
    e_peso.place(x=130, y=131)

    # botao inserir----------------------------------------------------------------------------------------------------------------------------------------------------

    img_add = Image.open('sinal_de_mais.png')
    img_add = img_add.resize((20,20))
    img_add = ImageTk.PhotoImage(img_add)

    b_inserir = Button(frameMeio, command= inserir , image=img_add,width=95, text='  ADICIONAR'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co2, fg=co3)
    b_inserir.place(x=330, y=10)

    # botao deleta -------------------------------------------------------------------------------------------------------------------------------------------------------

    img_delete = Image.open('sinal_delete.png')
    img_delete= img_delete.resize((20,20))
    img_delete = ImageTk.PhotoImage(img_delete)

    b_delete = Button(frameMeio,command=deletar, image=img_delete,width=95, text='  DELETAR'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co2, fg=co3)
    b_delete.place(x=330, y=50)

    # botao atulizar--------------------------------------------------------------------------------------------------------------------------------------------------------

    img_atualizar = Image.open('atualizar.png')
    img_atualizar= img_atualizar.resize((20,20))
    img_atualizar = ImageTk.PhotoImage(img_atualizar)

    b_atualizar = Button(frameMeio,command=atualizar, image=img_atualizar,width=95, text='  ATUALIZAR'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co2, fg=co3)
    b_atualizar.place(x=330, y=90)

    # botao calculadora-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    img_calculadora = Image.open('tcalculadora.png')
    img_calculadora= img_calculadora.resize((20,20))
    img_calculadora = ImageTk.PhotoImage(img_calculadora)

    b_calculadora = Button(frameMeio,command=abrir_janela, image=img_calculadora,width=95, text=' CALCULAR'.upper(),compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co2, fg=co3)
    b_calculadora.place(x=330, y=130)

    # painel quantidade total de produtos-----------------------------------------------------------------------------------------------------------------------------------

    l_total = Label(frameMeio, text='',width=18, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co0, fg=co2)
    l_total.place(x=500, y=17)

    l_total_ = Label(frameMeio, text='       QUANTIDADE TOTAL DE ITENS      ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co2)
    l_total_.place(x=500, y=12)

    #tabela parte de baixo-------------------------------------------------------------------------------------------------------------------------------------------------

    def mostrar():

        global tree

        tabela_head = ['#ITEM','PRODUTO',  'CODIGO','PESO LIQUIDO', 'DATA DE RECEBIMENTO', 'NOTA FISCAL']

        lista_itens = ver_form()

        tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
        #vertical scroll
        vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
        #horizontal scroll
        hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        frameBaixo.grid_rowconfigure(0, weight=12)

        hd=["center","center","center","center","center","center"]
        h=[60,160,160,160,160,160]
        n=0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n],anchor=hd[n])
            n+=1

        #inserindo os itens dentro da tabela
        for item in lista_itens:
            tree.insert('', 'end', values=item)


            quantidade = []
        for item in lista_itens:
            quantidade.append(item[0])

            total_itens= len(quantidade)
            
            l_total['text'] = total_itens

    mostrar()


    janela.mainloop()
janela_principal()


    

                                         