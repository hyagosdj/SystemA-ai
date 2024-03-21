from interface_grafica import *
import sqlite3


# INSERIR PRODUTOS NO DATABASE
def inserir_db(idproduto, data, hora, valor, modopag, produto, cliente, usuario):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO VENDAS VALUES ('"+str(idproduto)+"', '"+str(data)+"', '"+str(hora)+"', '"+str(modopag)+"', '"+str(round(valor, 2))+"', '"+str(cliente.upper())+"', '"+str(usuario)+"')")
    banco.commit()
    sg.popup(f'FORMA DE PAGAMENTO {modopag} REFERENTE A VENDA DE {produto}, REGISTRADA COM SUCESSO!', font='Arial 15 bold', title='INFO')

def inserir_frutas(fruta, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS FRUTAS (FRUTA text, QUANTIDADE integer, VALOR integer)')
    banco.commit()
    cursor.execute("INSERT INTO FRUTAS VALUES('"+str(fruta)+"', '"+str(quantidade)+"', '"+str(valor)+"')")
    banco.commit()

def inserir_utilidades(produto, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS UTILIDADES(PRODUTO text, QUANTIDADE integer, VALOR integer)')
    banco.commit()
    cursor.execute("INSERT INTO UTILIDADES VALUES ('"+str(produto)+"', '"+str(quantidade)+"', '"+str(valor)+"')")
    banco.commit()

def inserir_gelatos(produto, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS GELATOS(PRODUTO text, QUANTIDADE integer, VALOR integer)')
    banco.commit()
    cursor.execute("INSERT INTO GELATOS VALUES('"+str(produto)+"', '"+str(quantidade)+"', '"+str(valor)+"')")
    banco.commit()

def ver_gelatos():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM GELATOS')
    gelatos = cursor.fetchall()
    for gelato in gelatos:
        print(f'Produto: {gelato[0]}, Quantidade: {gelato[1]}, Investimento: {gelato[2]}.')

    cursor.execute('SELECT VALOR FROM GELATOS')
    resfrutas = cursor.fetchall()
    somagelatos = 0
    for i in resfrutas:
        somagelatos = somagelatos + i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somagelatos}')
        
def ver_utilidades():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM UTILIDADES')
    utilidades = cursor.fetchall()
    for utilidade in utilidades:
        print(f'Produto: {utilidade[0]}, Quantidade: {utilidade[1]}, Investimento: {utilidade[2]}.')

    cursor.execute('SELECT VALOR FROM UTILIDADES')
    resfrutas = cursor.fetchall()
    somautilidades = 0
    for i in resfrutas:
        somautilidades = somautilidades + i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somautilidades}')

def ver_frutas():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM FRUTAS')
    frutas = cursor.fetchall()
    for fruta in frutas:
        print(f'Fruta: {fruta[0]}, Quantidade: {fruta[1]}, Investimento: {fruta[2]}.')

    cursor.execute('SELECT VALOR FROM FRUTAS')
    resfrutas = cursor.fetchall()
    somafrutas = 0
    for i in resfrutas:
        somafrutas = somafrutas + i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somafrutas}')

def relatorio_completo():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM VENDAS')
    vendastotais = cursor.fetchall()
    print('SEGUE RELATÓRIO COMPLETO DE VENDAS\n')
    for vendatt in vendastotais:
        print(f'DATA: {vendatt[1]} - {vendatt[2]}, FORMA DE PAGAMENTO: {vendatt[3]}, VALOR: R$ {vendatt[4]}\n')
    
    cursor.execute('SELECT VALOR FROM VENDAS')
    resvtt = cursor.fetchall()
    somavtt = 0
    for i in resvtt:
        somavtt = somavtt + i[0]
    print(f'O VALOR TOTAL DE VENDAS É R${round(somavtt, 2)}')

def relatorio_acai():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM VENDAS')
    vendasacai = cursor.fetchall()
    print('SEGUE RELATÓRIO DE VENDAS SOMENTE DE AÇAÍ\n')
    for va in vendasacai:
        if va[0] == 1:
            print(f'DATA: {va[1]} - {va[2]}, FORMA DE PAGAMENTO: {va[3]}, VALOR: R$ {va[4]}\n')

    cursor.execute('SELECT VALOR FROM VENDAS WHERE ID = 1')
    resva = cursor.fetchall()
    somava = 0
    for acai in resva:
        somava = somava + acai[0]
    print(f'O VALOR TOTAL DE VENDAS É R${round(somava, 2)}')

def relatorio_sorvete():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT * FROM VENDAS')
    vendassorvete = cursor.fetchall()
    print('SEGUE RELATÓRIO DE VENDAS SOMENTE DE SORVETE\n')
    for vs in vendassorvete:
        if vs[0] == 2:
            print(f'DATA: {vs[1]} - {vs[2]}, FORMA DE PAGAMENTO: {vs[3]}, VALOR: R$ {vs[4]}\n')
    
    cursor.execute('SELECT VALOR FROM VENDAS WHERE ID = 2')
    resvs = cursor.fetchall()
    somavs = 0
    for sorvete in resvs:
        somavs = somavs + sorvete[0]
    print(f'O VALOR TOTAL DE VENDAS É R${round(somavs, 2)}')
