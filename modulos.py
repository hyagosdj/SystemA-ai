from interface_grafica import *
import sqlite3

# INSERIR VENDAS
def inserir_db(idproduto, data, hora, valor, modopag, produto, cliente, usuario):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO VENDAS VALUES ('"+str(idproduto)+"', '"+str(data)+"', '"+str(hora)+"', '"+str(modopag)+"', '"+str(round(valor, 2))+"', '"+str(cliente.upper())+"', '"+str(usuario)+"')")
    banco.commit()
    sg.popup(f'FORMA DE PAGAMENTO {modopag} REFERENTE A VENDA DE {produto}, REGISTRADA COM SUCESSO!', font='Arial 15 bold', title='INFO')

# INSERIR PRODUTOS NO TABELA DE CONTROLE DE ESTOQUE
def inserir_frutas(fruta, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS FRUTAS (FRUTA text, QUANTIDADE integer, VALOR integer)')
    banco.commit()
    cursor.execute("INSERT INTO FRUTAS VALUES('"+str(fruta)+"', '"+str(quantidade)+"', '"+str(valor)+"')")
    banco.commit()

def inserir_utilidades(utilidade, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS UTILIDADES (UTILIDADE text, QUANTIDADE integer, VALOR integer)')
    banco.commit()
    cursor.execute("INSERT INTO UTILIDADES VALUES ('"+str(utilidade)+"', '"+str(quantidade)+"', '"+str(valor)+"')")
    banco.commit()

def inserir_gelatos(gelato, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS GELATOS (GELATO text, QUANTIDADE integer, VALOR integer)')
    banco.commit()
    cursor.execute("INSERT INTO GELATOS VALUES('"+str(gelato)+"', '"+str(quantidade)+"', '"+str(valor)+"')")
    banco.commit()

# RELATÓRIOS DE CONTROLE DE ESTOQUE
def ver_gelatos():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT ROWID, GELATO, QUANTIDADE, VALOR FROM GELATOS')
    gelatos = cursor.fetchall()
    for gelato in gelatos:
        print(f'ID: {gelato[0]}, Produto: {gelato[1]}, Quantidade: {gelato[2]}, Investimento: {gelato[3]}.')

    cursor.execute('SELECT VALOR FROM GELATOS')
    resgelatos = cursor.fetchall()
    somagelatos = 0
    for i in resgelatos:
        somagelatos = somagelatos + i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somagelatos}')
        
def ver_utilidades():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT ROWID, UTILIDADE, QUANTIDADE, VALOR FROM UTILIDADES')
    utilidades = cursor.fetchall()
    for utilidade in utilidades:
        print(f'ID: {utilidade[0]}, Utilidade: {utilidade[1]}, Quantidade: {utilidade[2]}, Investimento: {utilidade[3]}.')

    cursor.execute('SELECT VALOR FROM UTILIDADES')
    resutilidades = cursor.fetchall()
    somautilidades = 0
    for i in resutilidades:
        somautilidades = somautilidades + i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somautilidades}')

def ver_frutas():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT ROWID, FRUTA, QUANTIDADE, VALOR FROM FRUTAS')
    frutas = cursor.fetchall()
    for fruta in frutas:
        print(f'ID: {fruta[0]}, Fruta: {fruta[1]}, Quantidade: {fruta[2]}, Investimento: {fruta[3]}.')

    cursor.execute('SELECT VALOR FROM FRUTAS')
    resfrutas = cursor.fetchall()
    somafrutas = 0
    for i in resfrutas:
        somafrutas = somafrutas + i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somafrutas}')

# RELATÓRIOS DE VENDAS
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


def conexao_db():
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()

"""
    MÉTODOS NÃO UTILIZADOS ATÉ O MOMENTO
    TESTAR A FUNCIONALIDADE NO CÓDIGO FONTE DANDO PREFERENCIA PARA AS VERIFICAÇÕES.
                26/03/2024 ~feita a integração dos Métodos dentro do Código Fonte. FUNCIONANDO CORRETAMENTE
    VERIFICAR A POSSIBILIDADE DE ALTERAR ATRAVES DO .FORMAT AS REFERENCIAS DA COLUNA E DA TABELA DO BANCO DE DADOS
                26/03/2024 ~verificado a possibilidade e o codigo segue funcionando corretamente e eliminado dois blocos de códigos repetidos.
"""
def del_item(coluna, tabela, id, produto):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()

    cursor.execute('SELECT ROWID, {} FROM {}'.format(coluna, tabela))
    gall = cursor.fetchall()
    if not gall:
        sg.popup('GELATO NÃO ENCONTRADO.', font='Arial 13 bold', title='INFORMAÇÃO')
    for g in gall:
        if g[0] == int(id) and g[1] == produto:
            cursor.execute('DELETE FROM GELATOS WHERE ROWID = {}'.format(int(id)))
            banco.commit()
            sg.popup(f'Removido com sucesso: {produto}', font='Arial 13 bold', title='INFORMAÇÃO')
        else:
            sg.popup('NÃO ENCONTRADO, FAVOR VERIFICAR', font='Arial 13 bold', title='INFORMAÇÃO')
