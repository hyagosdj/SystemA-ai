# type: ignore
from modulos import *  # noqa 403

criar_janela_login()  # noqa 405
while True:
    window, events, values = sg.read_all_windows()  # noqa 405
    # CRIAR O DATABASE
    banco = sqlite3.connect('logins.db')  # noqa 405
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(ID integer primary key, USUARIO text, SENHA text)')
    banco.commit()

    if events == sg.WINDOW_CLOSED:  # noqa 405
        break

    # AUTENTICA O LOGIN
    elif events == 'ENTRAR':
        window['usuario'].set_focus()
        window['usuario'].update('')
        window['senha'].update('')

        usuario = values['usuario']
        senha = values['senha']

        banco = sqlite3.connect('logins.db')  # noqa 405
        cursor = banco.cursor()

        try:
            cursor.execute(f"SELECT SENHA FROM usuarios WHERE USUARIO ='{usuario}'")
            senha_db = cursor.fetchall()
            banco.close()
            if senha == senha_db[0][0]:
                sg.popup(f"Olá {usuario.title()}, Seja Bem Vindo!", # noqa 405
                         font='Arial 14 bold', title='BEM VINDO!')  

                # INICIA A TELA DE ABERTURA DE CAIXA
                criar_abertura_caixa()  # noqa: F405
                window.close()

                while True:
                    window, events, values = sg.read_all_windows()  # noqa: F405

                    dia = values['dia']
                    mes = values['mes']
                    ano = values['ano']
                    aberturasupri = values['aberturasupri']

                    diahoje = f'{date.today().day}'  # noqa: F405
                    meshoje = f'{date.today().month}'  # noqa: F405
                    anohoje = f'{date.today().year}'  # noqa: F405

                    if events == sg.WINDOW_CLOSED:  # noqa: F405
                        criar_janela_login()  # noqa: F405
                        window.close()
                        break

                    if events == 'ABRIR':
                        if dia.isdigit() and mes.isdigit() and ano.isdigit() \
                            and aberturasupri.isdigit():
                            if not int(dia) != int(diahoje) and not int(mes) != int(meshoje) and not int(ano) != int(anohoje) and int(aberturasupri) >= 100:
                                sg.popup(f"{usuario.title()} abriu O CAIXA em {dia}/{mes}/{ano} com R$ {aberturasupri} para suprimento.",  # noqa: F405
                                         font='Arial 13 bold', title='ABERTURA DO CAIXA')

                            # INICIA A TELA PRINCIPAL DO SISTEMA QUE GERENCIA AS VENDAS
                                criar_janela_prin()  # noqa: F405
                                window.close()
                                while True:
                                    window, events, values = sg.read_all_windows()  # noqa: F405

                                    # VARIAVEIS DA TELA PRINCIPAL
                                    window['usuario'].update(usuario)
                                    kg = 1000
                                    gramas = values['gramas']
                                    acai = 17
                                    sorvete = 19
                                    idproduto = values['idproduto']
                                    data = f'{date.today().day}/{date.today().month}/{date.today().year}'  # noqa: F405
                                    hora = datetime.now()  # noqa: F405
                                    window['hora'].update(hora.strftime('%H:%M:%S'))
                                    cliente = values['cliente']

                                    # CONEXÃO DE BANCO DE DADOS DE VENDAS
                                    banco = sqlite3.connect('acai_database.db')  # noqa: F405
                                    cursor = banco.cursor()
                                    cursor.execute('CREATE TABLE IF NOT EXISTS VENDAS(ID integer, DATA text, HORA text, FORMA text, VALOR integer, CLIENTE text, USUARIO text)')
                                    banco.commit()

                                    if events == sg.WINDOW_CLOSED:  # noqa: F405
                                        criar_janela_login()  # noqa: F405
                                        window.close()
                                        break

                                    # CAUCULAR A QUANTIDADE DE GRAMAS E MOSTRAR O VALOR A SER PAGO
                                    if events == 'CALCULAR':

                                        if idproduto == '1' or idproduto == '2':

                                            if cliente.isalpha():

                                                if idproduto == '1' and gramas.isdigit():
                                                    valoracai = (int(gramas) * acai) / kg
                                                    window['saidapedido'].update(round(valoracai, 2))
                                                    window['saida'].update('')
                                                    window['saidatroco'].update('0.00')
                                                    window['valorpago'].update('')
                                                    print('*' * 102)
                                                    print(' ' * 57 + f'COMANDA DE {cliente.upper()}\n')
                                                    print('*' * 102)
                                                    print(' ' * 15 + 'AÇAÍ TECH SYSTEM AGRADECE A SUA PREFERÊNCIA\n')
                                                    print('PEDIDO: ' + ' ' * 75 + f'{gramas}g de AÇAÍ')
                                                    print('VALOR A SER PAGO: ' + ' ' * 72 + f'R$ {round(valoracai, 2)}')

                                                elif idproduto == '2' and gramas.isdigit():
                                                    valorsorvete = (int(gramas) * sorvete) / kg
                                                    window['saidapedido'].update(round(valorsorvete, 2))
                                                    window['saida'].update('')
                                                    window['saidatroco'].update('0.00')
                                                    window['valorpago'].update('')
                                                    print('*' * 102)
                                                    print(' ' * 57 + f'COMANDA DE {cliente.upper()}\n')
                                                    print('*' * 102)
                                                    print(' ' * 15 + 'AÇAÍ TECH SYSTEM AGRADECE A SUA PREFERÊNCIA\n')
                                                    print('PEDIDO: ' + ' ' * 75 + f'{gramas}g de SORVETE')
                                                    print('VALOR A SER PAGO: ' + ' ' * 72 + f'R$ {round(valorsorvete, 2)}')

                                                else:
                                                    sg.popup('VERIFIQUE O VALOR DAS GRAMAS!',  # noqa: F405
                                                        font='Arial 15 bold', title='ERRO!')

                                            else:
                                                sg.popup('VERIFIQUE SE PREENCHEU O NOME DO CLIENTE',  # noqa: F405
                                                         font='Arial 15 bold', title='ERRO!')

                                        else:
                                            sg.popup('VERIFIQUE SE DIGITOU: [1] ou [2]',  # noqa: F405
                                                     font='Arial 15 bold', title='ERRO!')

                                    if events == 'CONFIRMAR':
                                        try:
                                            valorpago = values['valorpago'].replace(',', '.')

                                            if cliente.isalpha():

                                                if idproduto == '1' or idproduto == '2':

                                                    if idproduto == '1' and gramas.isdigit() and float(valorpago) and not valorpago == None:

                                                        valoracai = (int(gramas) * acai) / kg
                                                        trocoacai = float(valorpago) - valoracai
                                                        window['saidatroco'].update(round(trocoacai, 2))
                                                        print('VALOR PAGO: ' + ' ' * 85 + f'R$ {valorpago}\n'+'_' * 60)
                                                        print('VALOR TROCO: ' + ' ' * 83 + f'R$ {round(trocoacai, 2)}\n')

                                                    elif idproduto == '2' and gramas.isdigit() and float(valorpago) and not valorpago == None:
                                                        valorsorvete = (
                                                            int(gramas) * sorvete) / kg
                                                        trocosorvete = float(valorpago) - valorsorvete
                                                        window['saidatroco'].update(
                                                            round(trocosorvete, 2))
                                                        print('VALOR PAGO: ' + ' ' * 85 + f'R$ {valorpago}\n'+'_' * 65)
                                                        print('VALOR TROCO: ' + ' ' * 83 + f'R$ {round(trocosorvete, 2)}\n')

                                                    else:
                                                        sg.popup('[GRAMAS DO PEDIDO] EM BRANCO.',  # noqa: F405
                                                                 font='Arial 15 bold', title='ERRO!')

                                                else:
                                                    sg.popup('VERIFIQUE SE DIGITOU ID DO PRODUTO CORRETAMENTE!',  # noqa: F405
                                                        font='Arial 15 bold', title='ERRO!')

                                            else:
                                                sg.popup('PREENCHA O NOME DO CLIENTE.',  # noqa: F405
                                                    font='Arial 15 bold', title='ERRO!')

                                        except:  # noqa: E722
                                            sg.popup('VERIFIQUE O CAMPO DE PAGAMENTO.',  # noqa: F405
                                                font='Arial 15 bold', title='ERRO!')

                                    if events == 'DÉBITO':
                                        try:
                                            if not cliente.isalpha():
                                                sg.popup('PREENCHA O NOME do CLIENTE.',  # noqa: F405
                                                         font='Arial 15 bold', title='ERRO!')

                                            elif idproduto == '1' and not trocoacai == None and not valorpago == None and cliente.isalpha():  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                valoracai, 'DÉBITO', 'AÇAÍ', cliente, usuario)

                                            elif idproduto == '2' and not trocosorvete == None and not valorpago == None and cliente.isalpha():  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                valorsorvete, 'DÉBITO', 'SORVETE', cliente, usuario)

                                            elif idproduto != '1' and idproduto != '2':
                                                sg.popup('ID DO PRODUTO, SOMENTE [1] OU [2]',  # noqa: F405
                                                    font='Arial 15 bold', title='ERRO!')

                                        except:  # noqa: E722
                                            sg.popup('CONFIRME O PAGAMENTO PRIMEIRO!',   # noqa: F405
                                                     font='Arial 15 bold', title='ERRO!')

                                    if events == 'CRÉDITO':
                                        try:
                                            if not cliente.isalpha():
                                                sg.popup('PREENCHA O NOME do CLIENTE.',  # noqa: F405
                                                         font='Arial 15 bold', title='ERRO!')

                                            elif idproduto == '1' and not trocoacai == None and not valorpago == None and not cliente == None:  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                              valoracai, 'CRÉDITO', 'AÇAÍ', cliente, usuario)

                                            elif idproduto == '2' and not trocosorvete == None and not valorpago == None and not cliente == None:  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                              valorsorvete, 'CRÉDITO', 'SORVETE', cliente, usuario)

                                            elif idproduto != '1' and idproduto != '2':
                                                sg.popup('ID DO PRODUTO, SOMENTE [1] OU [2]',  # noqa: F405
                                                         font='Arial 15 bold', title='ERRO!')

                                        except:  # noqa: E722
                                            sg.popup('CONFIRME O PAGAMENTO PRIMEIRO!',  # noqa: F405
                                                     font='Arial 15 bold', title='ERRO!')

                                    if events == 'DINHEIRO':
                                        try:
                                            if not cliente.isalpha():
                                                sg.popup('PREENCHA O NOME do CLIENTE.',  # noqa: F405
                                                          font='Arial 15 bold', title='ERRO!')

                                            elif idproduto == '1' and not trocoacai == None and not valorpago == None and not cliente == None:  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                              valoracai, 'DINHEIRO', 'AÇAÍ', cliente, usuario)

                                            elif idproduto == '2' and not trocosorvete == None and not valorpago == None and not cliente == None:  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                              valorsorvete, 'DINHEIRO', 'SORVETE', cliente, usuario)

                                            elif idproduto != '1' and idproduto != '2':
                                                sg.popup('ID DO PRODUTO, SOMENTE [1] OU [2]',  # noqa: F405
                                                    font='Arial 15 bold', title='ERRO!')

                                        except:  # noqa: E722
                                            sg.popup('CONFIRME O PAGAMENTO PRIMEIRO!',  # noqa: F405
                                                     font='Arial 15 bold', title='ERRO!')

                                    if events == 'PIX':
                                        try:
                                            if not cliente.isalpha():
                                                sg.popup('PREENCHA O NOME do CLIENTE.',  # noqa: F405
                                                         font='Arial 15 bold', title='ERRO!')
                                            elif idproduto == '1' and not trocoacai == None and not valorpago == None and not cliente == None:  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                               valoracai, 'PIX', 'AÇAÍ', cliente, usuario)

                                            elif idproduto == '2' and not trocosorvete == None and not valorpago == None and not cliente == None:  # noqa: E711
                                                inserir_venda(idproduto, data, hora.strftime('%H:%M:%S'),  # noqa: F405
                                                              valorsorvete, 'PIX', 'SORVETE', cliente, usuario)

                                            elif idproduto != '1' and idproduto != '2':
                                                sg.popup('ID PRODUTO, SOMENTE [1] OU [2]',   # noqa: F405
                                                    font='Arial 15 bold', title='ERRO!')

                                        except:  # noqa: E722
                                            sg.popup('CONFIRME O PAGAMENTO PRIMEIRO!',   # noqa: F405
                                                     font='Arial 15 bold', title='ERRO!')

                                    # INICIA A JANELA DE CANCELAMENTO DE PEDIDOS
                                    if events == 'CANCELAR PEDIDO':
                                        window['idproduto'].update('')
                                        window['saida'].update('')
                                        window['gramas'].update('')
                                        window['saidapedido'].update('0.00')
                                        window['valorpago'].update('')
                                        window['saidatroco'].update('0.00')

                                        janela_cancelar()  # noqa: F405
                                        window.close()
                                        listacancelar = []
                                        while True:
                                            window, events, values = sg.read_all_windows()  # noqa: F405

                                            if events == sg.WINDOW_CLOSED:  # noqa: F405
                                                criar_janela_prin()  # noqa: F405
                                                window.close()
                                                break

                                            elif events == 'PROCURAR':
                                                try:
                                                    window['saidacancelar'].update('')
                                                    banco = sqlite3.connect('acai_database.db')  # noqa: F405
                                                    cursor = banco.cursor()
                                                    cursor.execute('SELECT _rowid_, DATA, HORA, FORMA, VALOR FROM VENDAS')
                                                    vendastotais = cursor.fetchall()
                                                    print('SEGUE RELATÓRIO COMPLETO DAS VENDAS\n')
                                                    for vendatt in vendastotais:
                                                        print(f'Linha: {vendatt[0]} | DATA: {vendatt[1]} - {vendatt[2]},\
                                                              FORMA DE PAGAMENTO: {vendatt[3]}, VALOR: R$ {vendatt[4]}\n')
                                                except:  # noqa: E722
                                                    sg.popup('Ocorreu algum erro durante a busca de vendas. Verifique se houve registro da venda',  # noqa: F405
                                                             font='Arial 13 bold', title='INFORMAÇÃO')

                                            elif events == 'CANCELAR':
                                                try:
                                                    window['idcancelar'].update('')
                                                    conexao_db()  # noqa: F405
                                                    window['saidacancelar'].update('')
                                                    if values['idcancelar'].isdigit():
                                                        idcancelar = values['idcancelar'].replace("'", "")
                                                        cursor.execute('DELETE FROM VENDAS WHERE ROWID = {}'.format(int(idcancelar)))
                                                        banco.commit()
                                                        sg.popup(f'A VENDA DA LINHA \
                                                                 {idcancelar}, FOI CANCELADA', font='Arial 14 bold', title='INFO')  # noqa: F405

                                                    else:
                                                        sg.popup('SOMENTE DÍGITOS SÃO ACEITOS!', font='Arial 14 bold',   # noqa: F405
                                                                 title='ERRO')
                                                except:  # noqa: E722
                                                    sg.popup('VERIFIQUE SE DIGITOU A LINHA CORRETAMENTE',   # noqa: F405
                                                        font='Arial 14 bold', title='ERRO')

                                            elif events == 'VOLTAR':
                                                criar_janela_prin()  # noqa: F405
                                                window.close()
                                                break

                                    # INICIAR NOVO PEDIDO
                                    if events == 'NOVO PEDIDO':
                                        window['saida'].update('')
                                        window['cliente'].update('')
                                        window['idproduto'].update('')
                                        window['gramas'].update('')
                                        window['saidapedido'].update('0.00')
                                        window['valorpago'].update('')
                                        window['saidatroco'].update('0.00')
                                        window['cliente'].set_focus()

                                    # MOSTRA OS RELATÓRIOS ESPECIFICOS E GERAL DE VENDAS
                                    if events == 'RELATÓRIO COMPLETO':
                                        window['saida'].update('')
                                        relatorio_completo()  # noqa: F405

                                    if events == 'RELATÓRIO AÇAÍ':
                                        window['saida'].update('')
                                        relatorio_acai()  # noqa: F405

                                    if events == 'RELATÓRIO SORVETE':
                                        window['saida'].update('')
                                        relatorio_sorvete()  # noqa: F405

                                    # MOSTRA INFORMAÇÕES RELEVANTES DO SISTEMA COM DICAS DE UTILIZAÇÃO
                                    if events == 'INFORMAÇÕES':
                                        window['saida'].update('')
                                        exibir_informacao()  # noqa: F405

                                    # INICIA O CONTROLE DE ESTOQUE
                                    if events == 'CONTROLE DE ESTOQUE':
                                        window.close()
                                        criar_janela_controle()  # noqa: F405

                                        while True:
                                            window, events, values = sg.read_all_windows()  # noqa: F405

                                            idgelato = values['idgelato']
                                            gelatos = values['gelatos']
                                            qntgelatos = values['qntgelatos']
                                            valorgelatos = values['valorgelatos']

                                            idutilidade = values['idutilidade']
                                            utilidades = values['utilidades']
                                            qntutilidades = values['qntutilidades']
                                            valorutilidades = values['valorutilidades']

                                            idfruta = values['idfruta']
                                            frutas = values['frutas']
                                            qntfrutas = values['qntfrutas']
                                            valorfrutas = values['valorfrutas']

                                            # UM PEQUENO AUXILIO PARA PREENCHER CORRETAMENTE.
                                            if events == 'AJUDA':
                                                window['mostrarproduto'].update(
                                                    '')
                                                print('*' * 51)
                                                print(
                                                    f'{' ' * 21}COMO FUNCIONA')
                                                print(
                                                    f'{' ' * 7}O PREENCHIMENTO DESTA JANELA')
                                                print('*' * 51)
                                                print(
                                                    'PRIMEIRO VOCÊ DEVERÁ SELECIONAR UM ITEM DAS CATEGORIAS: \n GELATO | UTILIDADE | FRUTA')
                                                print(
                                                    'EM SEGUIDA COLOCARÁ A QUANTIDADE E O VALOR UTILIZADO PARA ADQUIRÍ-LOS')
                                                print(
                                                    'LOGO APÓS PRESSIONE EM [ADD GELATO/UTILIDADE/FRUTA] PARA ADICIONAR NO BANCO DE DADOS OU PRESSIONE EM \n[VER GELATOS/UTILIDADES/FRUTAS]')
                                                print(
                                                    'O VALOR REGISTRADO SERÁ MOSTRADO EM UMA SOMA E AO LADO DO PRODUTO, SEU VALOR TAMBÉM.')
                                                print(
                                                    'SENDO ASSIM CASO DESEJE REGRESSAR A TELA ANTERIOR, PRESSIONE EM [VOLTAR] E RETORNARÁ PARA A TELA DE ATENDIMENTO.')

                                            if events == sg.WINDOW_CLOSED:  # noqa: F405
                                                criar_janela_prin()  # noqa: F405
                                                window.close()
                                                break

                                            if events == 'VOLTAR':
                                                window.close()
                                                criar_janela_prin()  # noqa: F405
                                                break

                                            # CADASTRAR OS PRODUTOS NO CONTROLE DE ESTOQUE
                                            if events == 'ADD GELATO':
                                                try:
                                                    if not gelatos == '' and not qntgelatos == '' and not valorgelatos == '':
                                                        inserir_item('GELATOS', 'GELATO', gelatos, qntgelatos, valorgelatos)  # noqa: F405
                                                        sg.popup(f'Inserido com sucesso: {gelatos}, QNT: {qntgelatos}, \
                                                                 Valor: {valorgelatos}', font='Arial 13 bold', title='INFORMAÇÃO')  # noqa: F405
                                                    else:
                                                        sg.popup('Verifique os campos GELATO, QUANTIDADE e VALOR.', font='Arial 13 bold', title='ERRO')  # noqa: F405
                                                except:  # noqa: E722
                                                    sg.popup('Algo deu errado. Tente novamente e verifique os campos de gelatos estão preenchidos.', font='Arial 13 bold', title='ERRO')  # noqa: F405

                                            if events == 'ADD UTILIDADE':
                                                try:
                                                    if not utilidades == '' and not qntutilidades == '' and not valorutilidades == '':
                                                        inserir_item('UTILIDADES', 'UTILIDADE', utilidades, qntutilidades, valorutilidades)  # noqa: F405
                                                        sg.popup(f'Inserido com sucesso: {qntutilidades} - {utilidades} \
                                                                 Valor: {valorutilidades}', font='Arial 13 bold', title='INFORMAÇÃO')  # noqa: F405
                                                    else:
                                                        sg.popup('Verifique os campos UTILIDADE, QUANTIDADE e VALOR.',  # noqa: F405
                                                                 font='Arial 13 bold', title='ERRO')
                                                except:  # noqa: E722
                                                    sg.popup('Algo deu errado. Tente novamente e verifique os campos de utilidades estão preenchidos.',  # noqa: F405
                                                             font='Arial 13 bold', title='ERRO')  # noqa: F405

                                            if events == 'ADD FRUTA':
                                                try:
                                                    if not frutas == '' and not qntfrutas == '' and not valorfrutas == '':
                                                        inserir_item(  # noqa: F405
                                                            'FRUTAS', 'FRUTA', frutas, qntfrutas, valorfrutas)
                                                        sg.popup(f'Inserido com sucesso: QNT: {qntfrutas} - {frutas}, \
                                                                 Valor: {valorfrutas}', font='Arial 13 bold',   # noqa: F405
                                                                 title='INFORMAÇÃO')
                                                    else:
                                                        sg.popup(  # noqa: F405
                                                            'Verifique os campos FRUTA, QUANTIDADE e VALOR.', font='Arial 13 bold', title='ERRO')
                                                except:  # noqa: E722
                                                    sg.popup(  # noqa: F405
                                                        'Algo deu errado. Tente novamente e verifique os campos de frutas estão preenchidos.', font='Arial 13 bold', title='ERRO')

                                            # VERIFICAR OS PRODUTOS CADASTRADOS NO CONTROLE DE ESTOQUE
                                            if events == 'VER GELATOS':
                                                try:
                                                    window['mostrarproduto'].update('')
                                                    window['idgelato'].update('')
                                                    window['gelatos'].update('')
                                                    window['qntgelatos'].update('')
                                                    window['valorgelatos'].update('')
                                                    window['gelatos'].set_focus()
                                                    print('RELATÓRIO DOS GELATOS EM ESTOQUE:\n')
                                                    ver_itens(  # noqa: F405
                                                        'GELATO', 'GELATOS')
                                                except:  # noqa: E722
                                                    sg.popup(  # noqa: F405
                                                        'Banco de dados está em branco, adicione algo para conseguir verificar.', font='Arial 13 bold', title='INFORMAÇÃO')

                                            if events == 'VER UTILIDADES':
                                                try:
                                                    window['idutilidade'].update('')
                                                    window['mostrarproduto'].update('')
                                                    window['utilidades'].update('')
                                                    window['qntutilidades'].update('')
                                                    window['valorutilidades'].update('')
                                                    window['utilidades'].set_focus()
                                                    print('RELATÓRIO DAS UTILIDADES EM ESTOQUE:\n')
                                                    ver_itens('UTILIDADE', 'UTILIDADES')  # noqa: F405
                                                except:  # noqa: E722
                                                    sg.popup('Banco de dados está em branco, adicione algo para conseguir verificar.',   # noqa: F405
                                                             font='Arial 13 bold', title='INFORMAÇÃO')

                                            if events == 'VER FRUTAS':
                                                try:
                                                    window['mostrarproduto'].update('')
                                                    window['idfruta'].update('')
                                                    window['frutas'].update('')
                                                    window['qntfrutas'].update('')
                                                    window['valorfrutas'].update('')
                                                    window['frutas'].set_focus()
                                                    print('RELATÓRIO DAS FRUTAS EM ESTOQUE:\n')
                                                    ver_itens('FRUTA', 'FRUTAS')  # noqa: F405
                                                except:  # noqa: E722
                                                    sg.popup(  # noqa: F405
                                                        'Banco de Dados está em Branco, adicione algo para conseguir verificar.', font='Arial 13 bold', title='INFORMAÇÃO')

                                            # REMOVER OS PRODUTOS CADASTRADOS NO CONTROLE DE ESTOQUE
                                            if events == 'REMOVER GELATO(S)':
                                                try:
                                                    window['mostrarproduto'].update('')
                                                    if idgelato.isdigit() and not gelatos == '':
                                                        remover_item(  # noqa: F405
                                                            'GELATO', 'GELATOS', idgelato, gelatos)
                                                    else:
                                                        sg.popup(  # noqa: F405
                                                            'SOMENTE DÍGITO NO CAMPO: ID | ex: 1,2,3...', font='Arial 13 bold', title='INFORMAÇÃO')
                                                except:  # noqa: E722
                                                    sg.popup(  # noqa: F405
                                                        'Preencha o GELATO e o ID para REMOVER', font='Arial 13 bold', title='INFORMAÇÃO')

                                            if events == 'REMOVER UTILIDADE(S)':
                                                try:
                                                    window['mostrarproduto'].update('')
                                                    if idutilidade.isdigit() and not utilidades == '':
                                                        remover_item('UTILIDADE', 'UTILIDADES', idutilidade, utilidades)  # noqa: F405
                                                    else:
                                                        sg.popup('SOMENTE DÍGITO NO CAMPO: ID | ex: 1,2,3...', font='Arial 13 bold',   # noqa: F405
                                                            title='INFORMAÇÃO')
                                                except:  # noqa: E722
                                                    sg.popup('Preencha a UTILIDADE e o ID para REMOVER', font='Arial 13 bold',   # noqa: F405
                                                        title='INFORMAÇÃO')

                                            if events == 'REMOVER FRUTA(S)':
                                                try:
                                                    window['mostrarproduto'].update('')
                                                    if idfruta.isdigit() and not frutas == '':
                                                        remover_item(  # noqa: F405
                                                            'FRUTA', 'FRUTAS', idfruta, frutas)
                                                    else:
                                                        sg.popup(  # noqa: F405
                                                            'SOMENTE DÍGITO NO CAMPO: ID | ex: 1,2,3...', font='Arial 13 bold', title='INFORMAÇÃO')
                                                except:  # noqa: E722
                                                    sg.popup(  # noqa: F405
                                                        'Preencha a FRUTA e o ID para REMOVER', font='Arial 13 bold', title='INFORMAÇÃO')
                            else:
                                sg.popup('A DATA NÃO PODE SER DIFERENTE DE HOJE E O SUPRIMENTO DEVE SER NO MÍNIMO R$100 (cem reais).',  # noqa: F405
                                         font='Arial 14 bold', title='ERRO INICIAL!')

                        else:
                            sg.popup('PREENCHA TODOS OS CAMPOS CORRETAMENTE',  # noqa: F405
                                     font='Arial 13 bold', title='ERRO DE PREENCHIMENTO!')

            else:
                sg.popup("SENHA INCORRETA!", font='Arial 13 bold',  # noqa: F405
                         title='ERRO DE SENHA!')

        except Exception as e:  # noqa: E722
            sg.popup(e)  # noqa: F405
            # sg.popup('O programa está sendo finalizado.',  # noqa: F405
            #          font='Arial 13 bold', title='Informação!')
