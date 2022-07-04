from MatrizEsparsa import MatrizEsparsa
from Passageiro import Passageiro

if __name__ == "__main__":
    # OPÇÃO ESCOLHIDA PELO USUÁRIO NO MENU PRINCIPAL
    opcao = None
    # LINHAS DE ONIBUS CADASTRADAS SÃO ARMAZENADAS NESSA LISTA
    listaDeLinhas = []
    # NA OPÇÃO 2 DO MENU O USUARIO PODE ESCOLHER UMA LINHA E REALIZAR MODIFICAÇÕES
    # A LINHA ESCOLHIDA É GUARDADA AQUI
    linhaSelecionada: MatrizEsparsa = None

    while opcao != '11':
        if linhaSelecionada is not None:
            print('\n===========LINHA SELECIONADA: {}==========='.format(linhaSelecionada.getNome()))
        else:
            print('NENHUMA LINHA SELECIONADA. Use a opção 2 para selecioanr uma linha')
        print('1 - Cadastrar linha\n2 - Selecionar linha existente')
        
        # ALGUMAS OPÇÕES SÓ FAZEM SENTIDO SER MOSTRADAS APÓS SELECIONAR UMA LINHA
        if linhaSelecionada:
            print('3 - Adicionar passageiro em poltrona disponível')
            print('4 - Trocar Poltrona\n5 - Excluir passageiro\n6 - Consultar passageiro pela poltrona\n7 - Consultar poltrona do passageiro')
            print('8 - Exportar relação de passageiros\n9 - Consultar quantidade de assentos\n10 - Exibir status de todas as poltronas')
        print('11 - SAIR')
        opcao = input('DIGITE SUA OPÇÃO: ')


        # CADASTRA UMA LINHA E ADICIONA NA LISTA DE LINHAS CADASTRADAS
        if opcao == '1':
            try:
                nomeDaLinha = input('DIGITE O NOME DA LINHA: ')
                linhas = int(input('DIGITE A QUANTIDADE DE FILEIRAS: '))
                colunas = int(input('DIGITE A QUANTIDADDE DE POLTRONAS POR FILEIRAS: '))
                novaLinha = MatrizEsparsa(nomeDaLinha, linhas, colunas)
                listaDeLinhas.append(novaLinha)
                print('\nLINHA CRIADA COM SUCESSO: {} com {} ASSENTOS\n'.format(novaLinha.getNome(), novaLinha.tamanho()))
            except:
                print('\nOPÇÃO INVALIDA - Digite apenas números.\n')

        # PERMITE SELECIONAR UMA LINHA JA CADASTRADA E LIBERA AS OUTRAS OPÇÕES DO MENU
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

        # PERMITE ADICIONAR UM PASSAGEIRO NA LINHA SELECIONADA
        elif opcao == '3' and linhaSelecionada is not None:
            try:
                nome = input('Digite o nome do passageiro: ')
                rg = input('Digite o RG do passageiro: ')
                assento = linhaSelecionada.procurarAssentoDisponivel()
                passageiro = Passageiro(nome, rg)
                linhaSelecionada.adicionar(passageiro, assento)
                print('\nPASSAGEIRO {} ADICIONADO COM SUCESSO NA POLTRONA {}\n'.format(passageiro,assento))
            except:
                print('\nNENHUM ASSENTO DISPONIVEL\n')
            
        # PERMITE TROCAR UM PASSAGEIRO PARA UMA POLTRONA VAZIA
        elif opcao == '4' and linhaSelecionada is not None:
            try:
                poltrona1 = int(input('Digite A POLTRONA a ser trocada: '))
                poltrona2 = int(input('Digite A NOVA POLTRONA a ser trocada: '))
                linhaSelecionada.trocarPoltrona(poltrona1, poltrona2)
                print('\nPOLTRONA TROCADA COM SUCESSO!\n')
            except:
                print('\nPOLTRONA INVÁLIDA. POLTRONA ORIGEM DESOCUPADA. OU POLTRONA DESTINO OCUPADA. TENTE DE NOVO.\n')

        # PERMITE RETIRAR UM PASSAGEIRO DE UMA POLTRONA E DEIXA-LA VAGA
        elif opcao == '5' and linhaSelecionada is not None:
            try:
                poltrona = int(input('Digite o número da poltrona do passageiro que deseja excluir: '))
                dadosPassageiro = linhaSelecionada.pesquisar(poltrona)
                if dadosPassageiro is None:
                    raise Exception('NÃO É POSSÍVEL PROSSEGUIR, A POLTRONA NÃO ESTÁ OCUPADA POR NENHUM PASSAGEIRO.')
                check = input('Passageiro encontrado: {}. Deseja prosseguir com a exclusão? \nDigite sim ou não: '.format(dadosPassageiro))
                if check.lower() == "sim":
                    linhaSelecionada.remover(poltrona)
                    print('\nPASSAGEIRO {} REMOVIDO DO ASSENTO {}\n'.format(dadosPassageiro, poltrona))
            except:
                print('\nPASSAGEIRO NÃO ENCONTRADO\n')

        # PERMITE CONSULTAR OS DADOS DO PASSAGEIRO DE UMA CERTA POLTRONA
        elif opcao == '6' and linhaSelecionada is not None:
            try:
                poltrona = int(input('Digite a poltrona: '))
                passageiro = linhaSelecionada.pesquisar(poltrona)
                if passageiro is not None:
                    print('\nPASSAGEIRO {} ESTA NO ASSENTO {}\n'.format(passageiro, poltrona))
                else:
                    print('\nNENHUM PASSAGEIRO ESTA NO ASSENTO {}\n'.format(poltrona))

            except:
                print('\nPOLTRONA INVALIDA TENTE NOVAMENTE\n')

        # PERMITE CONSULTAR A POLTRONA EM QUE ESTÁ UM CERTO PASSAGEIRO
        elif opcao == '7' and linhaSelecionada is not None:
            try:
                nome = input('Digite o nome do passageiro: ')
                assento = linhaSelecionada.pesquisaPassageiro(nome)
                print('\nPASSAGEIRO {} ESTA NO ASSENTO {}\n'.format(nome, assento))
            except:
                print('\nPASSAGEIRO NÃO ENCONTRADO\n')

        # PERMITE CRIAR UM ARQUIVO DE TEXTO COM A RELAÇÃO DE PASSAGEIROS DA LINHA SELECIONADA
        elif opcao == '8' and linhaSelecionada is not None:
            with open('relacao_passageiros_{}.txt'.format(linhaSelecionada.getNome()), 'w') as relacaoDePassageiros:
                if linhaSelecionada.estaVazia():
                    relacaoDePassageiros.write('LINHA: {} ONIBUS VAZIO'.format(linhaSelecionada.getNome()))    
                else:
                    relacaoDePassageiros.write('LINHA: {}\n'.format(linhaSelecionada.getNome()))
                    relacaoDePassageiros.write('Poltrona;passageiro;rg\n')
                    # PERCORRE A LISTA DE PASSAGEIROS E ADICIONA OS DADOS DE CADA PASSAGEIRO NO ARQUIVO
                    for assento in range(1, linhaSelecionada.tamanho() + 1):
                        passageiro = linhaSelecionada.pesquisar(assento)
                        # SÓ ESCREVE NO ARQUIVO CASO A POLTRONA ESTEJA OCUPADA
                        if passageiro is not None:
                            relacaoDePassageiros.write('{};{};{}\n'.format(assento, passageiro.getNome(), passageiro.getRg()))
            print('\nARQUIVO {} GERADO COM SUCESSO'.format('relacao_passageiros_{}.txt\n'.format(linhaSelecionada.getNome())))
        
        # PERMITE MOSTRAR O TOTAL DE ASSENTOS DA LINHA SELECIONADA
        elif opcao == '9' and linhaSelecionada is not None:
            print("\nA LINHA SELECIONADA TEM {} ASSENTOS\n".format(linhaSelecionada.tamanho()))

        # PERMITE LISTAR O STATUS DE OCUPAÇÃO DE TODOS OS ASSENTOS DA LINHA SELECIONADA
        #  E MOSTRA TAMBÉM OS PASSGEIROS DE CADA ASSENTO
        elif opcao == '10' and linhaSelecionada is not None:
            linhaSelecionada.mostrarAssentos()

        # FINALIZA O PROGRAMA
        elif opcao == '11':
            pass

        # USUARIO ESCOLHEU UMA OPÇÃO INVALIDA. NÃO FAZ NADA E VOLTA PRO MENU
        else:
            print('\nOPÇÃO INVÁLIDA\n')
