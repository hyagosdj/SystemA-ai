from PySimpleGUI import PySimpleGUI as sg
from datetime import date, datetime


# CRIAR TELA LOGIN
def criar_janela_login():
    sg.theme('DarkBlue')

    layout = [
        [sg.Text('NOME DE USUÁRIO:', font='Arial 13 bold')],
        [sg.Input('', key='usuario', font='Arial 13 bold')],
        [sg.Text('SENHA:', font='Arial 13 bold')],
        [sg.Input('', key='senha', font='Arial 13 bold', password_char='*')],
        [sg.Button('ENTRAR', font='Arial 13 bold', size=(40, 2))]
    ]
    
    return sg.Window('TELA DE LOGIN', size=(450, 200), layout= layout, finalize=True)

# CRIAR ABERTURA DE CAIXA
def criar_abertura_caixa():
    sg.theme('DarkPurple7')

    coluna= [
        [sg.Text('ABERTURA DE CAIXA', font='Arial 14 bold')],
        [sg.Text('DIGITE A DATA DE HOJE:', font='Arial 13 bold')],
        [sg.Input(key='dia', font='Arial 14 bold', size=(3)), sg.Input(key='mes', font='Arial 14 bold', size=(3)), sg.Input(key='ano', font='Arial 14 bold', size=(5))],
        [sg.Text('SUPRIMENTO R$:', font='Arial 13 bold')],
        [sg.Input('', key='aberturasupri', font='Arial 14 bold', size=(20))],
        [sg.Text('\n', font='Arial 14 bold')],
        [sg.Button('ABRIR', size=(30, 10))]
    ]

    layout = [
        [sg.Frame(title='ABERTURA DE CAIXA', layout= coluna, pad=(75, 5))]
    ]

    return sg.Window('ABERTURA DE CAIXA', size=(400, 300), layout= layout, finalize=True, resizable=False)

# CRIAR TELA PRINCIPAL
def criar_janela_prin():
    sg.theme('DarkPurple')

    menu = [
        ['ARQUIVOS', ['RELATÓRIO COMPLETO', 'RELATÓRIO AÇAÍ', 'RELATÓRIO SORVETE']],
        ['SISTEMA', ['CONTROLE DE ESTOQUE']],
        ['AJUDA', ['INFORMAÇÕES']]
    ]

    col1 = [
        [sg.Button('DÉBITO', pad=(10, 20), size=(30, 7))],
        [sg.Button('CRÉDITO', pad=(10, 20), size=(30, 7))],
        [sg.Button('DINHEIRO', pad=(10, 20), size=(30, 7))],
        [sg.Button('PIX', pad=(10, 20), size=(30, 7))]
    ]

    col2 = [
        [sg.Text('\nNOME DO CLIENTE:', font='Arial 25 bold')],
        [sg.Input(key='cliente', font='Arial 25 bold', size= (31), pad=(0, 10))],
        [sg.Text('\nPRODUTO:  [1] AÇAÍ  [2] SORVETE', font='Arial 25 bold')],
        [sg.Input(key='idproduto', font='Arial 25 bold', size= (31), pad=(0, 10))],
        [sg.Text('GRAMAS DO PEDIDO:', font='Arial 25 bold'), sg.Input(key= 'gramas', font='Arial 25 bold', size=(11), pad=(0, 10))],
        [sg.Text(' ' * 84), sg.Button('CALCULAR', font='Arial 20 bold', size=(12, 2))],
        [sg.Text('VALOR DO PEDIDO: ', font='Arial 25 bold'), sg.Text('0.00', font='Arial 35 bold', background_color='white', key='saidapedido', pad=(0, 5))],
        [sg.Text('VALOR PAGO: ', font='Arial 25 bold'), sg.Input(key= 'valorpago', font='Arial 25 bold', size=(17), pad=(0, 10))],
        [sg.Text('TROCO: ', font='Arial 25 bold', text_color='White'), sg.Text('0.00', background_color='white', text_color='black', font='Arial 35 bold',
            key='saidatroco', pad=(0,0, (10,6)))],
        [sg.Text('\n\n\n\n')],
        [sg.Button('CONFIRMAR', pad=(10, 5), font='Arial 15 bold', size=(14, 3)), sg.Button('CANCELAR PEDIDO', pad=(10, 5), font='Arial 15 bold', size=(14, 3)),
        sg.Button('NOVO PEDIDO', pad=(10, 5), font='Arial 15 bold', size=(14,3))]

    ]

    col3 = [
        [sg.Text('AÇAÍ TEST SYSTEM', font='Arial 20 bold', pad=(250, 5))],
        [sg.Output(background_color= 'White', size=(70, 40), font= 'Arial 14 bold', text_color= 'Black', key= 'saida')]
    ]

    layout = [
        [sg.Menu(menu)],
        [sg.Text((f'{date.today().day}/{date.today().month}/{date.today().year}'), font='Arial 15 bold', text_color='White')],
        [sg.Text('Última Atividade:', font='Arial 13 bold', text_color='White'), sg.Text('', key='hora', font='Arial 13 bold', text_color='White', background_color='black')],
        [sg.Text('Atendente:', font='Arial 13 bold', text_color='White'), sg.Text('', key='usuario', font='Arial 13 bold', text_color='White')],
        [sg.Text(' ' * 10), sg.Frame('FORMAS DE PAGAMENTO:', font='Arial 15 bold', layout=col1), sg.Text(' ' * 20),
            sg.Frame('REGISTRAR', font='Arial 15 bold', layout=col2, pad=(7)), sg.Text(' ' * 10), sg.Column(col3)]
    ]

    return sg.Window('SYSTEM AÇAÍ', layout= layout, finalize=True, resizable= True)

# CRIAR TELA CONTROLE DE ESTOQUE
def criar_janela_controle():
    sg.theme('DarkBlue')

    menu = [
        ['CATEGORIAS', ['VOLTAR']]
    ]

    col1 = [
        [sg.Combo(['','BANANA', 'MORANGO', 'BAUNILHA', 'CHOCOLATE', 'TAPIOCA', 'NAPOLITANO', 'MENTA', 'NUTELLA',
                   'CHICLETE', 'CASTANHA', 'CREME COM PASSAS', 'ABACAXI', 'AÇAÍ'], font='Arial 20 bold', size=20, key='gelatos')],
        [sg.Text('\n\n\n\n\n\n\n\n')],
        [sg.Text('QUANTIDADE:', font='Arial 14 bold')],
        [sg.Input(key='qntgelatos', font='Arial 14 bold', size=20)],
        [sg.Text('VALOR:', font='Arial 14 bold')],
        [sg.Input(key='valorgelatos', font='Arial 14 bold', size=20)],
        [sg.Button('ADD GELATO', font='Arial 14 bold', size=14), sg.Button('VER GELATOS', font='Arial 14 bold', size=14)]

    ]

    col2 = [
        [sg.Combo(['','CASQUINHAS', 'COLHERES', 'COPOS 450ml', 'COPOS 500ml', 'VASILHA 450ml', 'VASILHA 750'],
                  font='Arial 20 bold', size=20, key='utilidades')],
        [sg.Text('\n\n\n\n\n\n\n\n')],
        [sg.Text('QUANTIDADE:', font='Arial 14 bold')],
        [sg.Input(key='qntutilidades', font='Arial 14 bold', size=20)],
        [sg.Text('VALOR:', font='Arial 14 bold')],
        [sg.Input(key='valorutilidades', font='Arial 14 bold', size=20)],
        [sg.Button('ADD UTILIDADE', font='Arial 14 bold', size=14), sg.Button('VER UTILIDADES', font='Arial 14 bold', size=14)]

    ]

    col3 = [
        [sg.Combo(['','BANANA', 'KIWI', 'MANGA', 'MORANGO', 'PITAYA', 'UVA'], font='Arial 20 bold', size=20, key='frutas')],
        [sg.Text('\n\n\n\n\n\n\n\n')],
        [sg.Text('QUANTIDADE:', font='Arial 14 bold')],
        [sg.Input(key='qntfrutas', font='Arial 14 bold', size=20)],
        [sg.Text('VALOR:', font='Arial 14 bold')],
        [sg.Input(key='valorfrutas', font='Arial 14 bold', size=20)],
        [sg.Button('ADD FRUTA', font='Arial 14 bold', size=12), sg.Button('VER FRUTAS', font='Arial 14 bold', size=12)]
        
    ]

    col4 = [
        [sg.Output(key='mostrarproduto', font='Arial 13 bold', background_color='White', text_color='Black', size=(70, 30))]
    ]

    layout = [
        [sg.Text('CONTROLE DE ESTOQUE AÇAÍ TECH SYSTEM', font='Arial 23 bold', pad=(270, 0))],
        [sg.Menu(menu), sg.Frame('GELATOS:', font='Arial 15 bold', layout=col1), 
        sg.Frame('UTILIDADES:', font='Arial 15 bold', layout=col2), 
        sg.Frame('FRUTAS:', font='Arial 15 bold', layout=col3), sg.Frame('DISPLAY:', font='Arial 15 bold', layout=col4)]
    ]

    return sg.Window('CONTROLE DE ESTOQUE', layout=layout, finalize=True, resizable=True)

# CRIAR TELA DE CANCELAMENTO
def janela_cancelar():
    sg.theme('DarkBlue13')

    col1 = [
        [sg.Text('AGORA PRESSIONE PROCURAR PARA VERIFICAR SUAS VENDAS E APÓS SELECIONE A LINHA QUE O MESMO SE ENCONTRA PARA EFETUAR O CANCELAMENTO DA VENDA', font='Arial 13 bold')],
        #[sg.Input('',font='Arial 13 bold', key='valorcancelar')],
        [sg.Text('INFORME A LINHA QUE O ITEM SE ENCONTRAR:', font='Arial 13 bold')],
        [sg.Input('',font='Arial 13 bold', key='idcancelar')],
        [sg.Button('PROCURAR', font='Arial 13 bold', size=(9, 3)), sg.Button('CANCELAR', font='Arial 13 bold', size=(9, 3)), 
        sg.Button('VOLTAR', font='Arial 13 bold', size=(9, 3))]
    ]

    col2 = [
        [sg.Output(font='Arial 13 bold', background_color='Black', text_color='White', size=(60, 15), key='saidacancelar')]
    ]

    layout = [
        [sg.Column(col1), sg.Column(col2)]
    ]

    return sg.Window('CANCELAMENTO DE VENDAS', layout=layout, finalize=True, resizable=False)
