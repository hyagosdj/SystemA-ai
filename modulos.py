from interface_grafica import *
import sqlite3

# INSERIR VENDAS
def inserir_venda(idproduto, data, hora, valor, modopag, produto, cliente, usuario):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO VENDAS VALUES ('"+str(idproduto)+"', '"+str(data)+"', '"+str(hora)+"', '"+str(modopag)+"', '"+str(round(valor, 2))+"', '"+str(cliente.upper())+"', '"+str(usuario)+"')")
    banco.commit()
    sg.popup(f'FORMA DE PAGAMENTO {modopag} REFERENTE A VENDA DE {produto}, REGISTRADA COM SUCESSO!', font='Arial 15 bold', title='INFO')

# INSERIR ITEM NA TABELA DE CONTROLE DE ESTOQUE
def inserir_item(tabela, coluna, item, quantidade, valor):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS {} ({} text, QUANTIDADE integer, VALOR integer)'.format(tabela, coluna))
    banco.commit()
    cursor.execute(f'INSERT INTO "'+str(tabela)+'" VALUES("'+str(item)+'", "'+str(quantidade)+'", "'+str(valor)+'")')
    banco.commit()

# RELATÓRIOS DE CONTROLE DE ESTOQUE
def ver_itens(coluna, tabela):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()
    cursor.execute('SELECT ROWID, {}, QUANTIDADE, VALOR FROM {}'.format(coluna, tabela))
    itens = cursor.fetchall()
    for item in itens:
        print(f'ID: {item[0]}, Produto: {item[1]}, Quantidade: {item[2]}, Investimento: {item[3]}.')

    cursor.execute('SELECT VALOR FROM {}'.format(tabela))
    valor_itens = cursor.fetchall()
    somaitens = 0
    for v_i in valor_itens:
        somaitens = somaitens + v_i[0]
    print(f'\nVALOR TOTAL DO INVESTIMENTO: {somaitens}')
        
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
    
    cursor.execute('SELECT VALOR FROM VENDAS WHERE ID = 2') # .format(id)
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
def remover_item(coluna, tabela, id, item):
    banco = sqlite3.connect('acai_database.db')
    cursor = banco.cursor()

    cursor.execute('SELECT ROWID, {} FROM {}'.format(coluna, tabela))
    itens = cursor.fetchall()

    # Campo Em Branco -> Erro será sinalizado!
    if not itens: 
        sg.popup('{} NÃO ENCONTRADO(A).'.format(coluna), font='Arial 13 bold', title='INFORMAÇÃO')
    try:
        for i in itens:
            if i[0] == int(id) and i[1] == item:
                cursor.execute('DELETE FROM {} WHERE ROWID = {}'.format(tabela, int(id)))
                banco.commit()
                sg.popup(f'Removido com sucesso: {item}', font='Arial 13 bold', title='INFORMAÇÃO')
        else:
            sg.popup('{} NÃO ENCONTRADO(A).'.format(coluna), font='Arial 13 bold', title='INFORMAÇÃO')

    except:
        sg.popup(f'{item}, com id: {id}, não localizado.', font='Arial 13 bold', title='INFORMAÇÃO')
    finally:
        pass
