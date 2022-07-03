from MatrizEsparsa import MatrizEsparsa
from Passageiro import Passageiro

if __name__ == "__main__":
    opcao = None
    listaDeLinhas = []
    linhaSelecionada = None
    while opcao != '11':
        if linhaSelecionada is not None:
            print('\nLINHA SELECIONADA: {}'.format(linhaSelecionada.getNome()))
        else:
            print('NENHUMA LINHA SELECIONADA. Use a opção 2 para selecioanr uma linha')
        print('1 - Cadastrar linha\n2 - Selecionar linha existente')
        if linhaSelecionada:
            print('3 - Adicionar passageiro em poltrona disponível')
            print('4 - Trocar Poltrona\n5 - Excluir passageiro\n6 - Consultar passageiro da poltrona\n7 - Consultar poltrona do passageiro')
            print('8 - Exportar relação de passageiros\n9 - Consultar quantidade de assentos\n10 - Exibir status de todas as poltronas')
        print('11 - SAIR')
        opcao = input('DIGITE SUA OPÇÃO: ')


        if opcao == '1':
            nomeDaLinha = input('DIGITE O NOME DA LINHA: ')
            linhas = int(input('DIGITE O NUMERO DE LINHAS: '))
            colunas = int(input('DIGITE O NUMERO DE COLUNAS: '))
            novaLinha = MatrizEsparsa(nomeDaLinha, linhas, colunas)
            listaDeLinhas.append(novaLinha)
            print('\nLINHA CRIADA COM SUCESSO: {} com {} ASSENTOS\n'.format(novaLinha.getNome(), novaLinha.tamanho()))


        elif opcao == '2':
            if len(listaDeLinhas) == 0:
                print('\nNENHUMA LINHA CADASTRADA\n')
            else:
                print('\nLINHAS CADASTRADAS: ')
                for indiceLinha in range(len(listaDeLinhas)):
                    print('{} - {}'.format(indiceLinha + 1, listaDeLinhas[indiceLinha].getNome()))
                numeroDaLinhaSelecionada = int(input('\nSELECIONE UMA LINHA: '))
                try:
                    linhaSelecionada = listaDeLinhas[numeroDaLinhaSelecionada - 1]
                except:
                    print('\nOPÇÃO INVALIDA - TENTE NOVAMENTE\n')
        elif opcao == '3' and linhaSelecionada is not None:
            pass
        elif opcao == '4' and linhaSelecionada is not None:
            pass
        elif opcao == '5' and linhaSelecionada is not None:
            pass
        elif opcao == '6' and linhaSelecionada is not None:
            pass
        elif opcao == '7' and linhaSelecionada is not None:
            pass
        elif opcao == '8' and linhaSelecionada is not None:
            pass
        elif opcao == '9' and linhaSelecionada is not None:
            pass
        elif opcao == '10' and linhaSelecionada is not None:
            pass
        elif opcao == '11':
            pass
        else:
            print('\nOPÇÃO INVÁLIDA\n')

    # me = MatrizEsparsa('JPA-CG',4,12)
    # print("esta cheio: {}".format(me.estaCheio()))
    # print("esta vazio: {}".format(me.estaVazia()))
    # me.adicionar(Passageiro('LUCAS DINIZ', '123456'), 30)
    # me.adicionar(Passageiro('BRUNA DINIZ', '789011'), 11)
    # me.adicionar(Passageiro('PRISCILA DINIZ', '777777'), 32)
    # me.adicionar(Passageiro('OUTRA PESSOA', '0000000'), 4)
    # me.trocarPoltrona(30,1)
    # me.trocarPoltrona(11,2)
    # me.trocarPoltrona(32,3)
    # me.remover(4)
    # me.mostrarAssentos()
    # print("pesquisa passageiro BRUNA. Esta no assento numero: {}".format(me.pesquisaPassageiro('')))
    # print(me.pesquisar(3))
    # print("esta cheio: {}".format(me.estaCheio()))
    # print("esta vazio: {}".format(me.estaVazia()))