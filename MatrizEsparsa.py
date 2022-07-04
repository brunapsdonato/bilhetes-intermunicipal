import Passageiro

class MatrizEsparsa:
    def __init__(self, id:str, linhas:int, colunas:int):
        '''A numeracao das poltronas é definida da seguinte forma:
                      Poltronas
           Fileira 1: 01 02    03 04
           Fileira 2: 05 06    07 08
           Fileira 3: 09 10    11 12
           Fileira 4: 13 14    15 16
           ....
        '''
        self.__id = id
        self.__linhas = linhas
        self.__colunas = colunas
        self.__matriz = [ [ None for y in range( linhas ) ] 
             for x in range( colunas ) ]

    def getMatriz(self):
        return self.__matriz

    def getNome(self):
        return self.__id
    
    def tamanho(self)->int:
        '''Retorna a quantidade de células da matriz'''
        return self.__linhas * self.__colunas

    def estaVazia(self)->bool:
        taVazio = True
        for linha in self.__matriz:
            for passageiro in linha:
                if passageiro is not None:
                    taVazio = False
        return taVazio

    def estaCheio(self)->bool:
        taCheio = True
        for linha in self.__matriz:
            if None in linha:
                taCheio = False
        return taCheio


    def procurarAssentoDisponivel(self)->int:
        '''Retorna um assento vazio disponível, se houver.
           Se não houver assento disponível, lançar uma exceção'''
        quantidadeDeAssentos = self.tamanho()
        for assento in range(1, quantidadeDeAssentos + 1):
            if self.pesquisar(assento) is None:
                return assento
        raise Exception('Nenhum assento disponível')
            

    def pesquisar(self, numero_poltrona:int)->Passageiro:
        '''Retorna os dados do passageiro alocado em um
           determinado assento'''
        linha, coluna = self.acharLinhaColunaPeloNumerDaPoltrona(numero_poltrona)
        return self.__matriz[linha][coluna]

    def pesquisaPassageiro(self, nome:str )->int:
        '''Retorna o número da poltrona em que um determinado
           passageiro está ocupando'''
        quantidadeDeAssentos = self.tamanho()
        for assento in range(1, quantidadeDeAssentos + 1):
            if self.pesquisar(assento) is not None:
                linha, coluna = self.acharLinhaColunaPeloNumerDaPoltrona(assento)
                passageiro = self.__matriz[linha][coluna]
                if nome.lower() in passageiro.getNome().lower():
                    return assento
        raise Exception('Passageiro {} não encontrado'.format(nome))

    def trocarPoltrona(self, poltrona_atual:int, nova_poltrona:int)->bool:
        '''Permite mover um passageiro pra outra poltrona caso ela esteja vazia
           e exista um passageiro na poltrona original. Caso contrário lança exceção (erro)'''
        linhaAtual, colunaAtual = self.acharLinhaColunaPeloNumerDaPoltrona(poltrona_atual)
        linhaNova, colunaNova = self.acharLinhaColunaPeloNumerDaPoltrona(nova_poltrona)

        passageiroNaPoltronaAtual = self.__matriz[linhaAtual][colunaAtual]
        poltronaDestino = self.__matriz[linhaNova][colunaNova]

        if passageiroNaPoltronaAtual is None or poltronaDestino is not None:
            raise Exception('Poltrona atual deve estar ocupada e a poltrona destino deve estar vazia')

        atual = self.__matriz[linhaAtual][colunaAtual]
        self.__matriz[linhaAtual][colunaAtual]= self.__matriz[linhaNova][colunaNova]
        self.__matriz[linhaNova][colunaNova] = atual

    def adicionar(self, passageiro: Passageiro, numero_poltrona:int)->bool:
        linha, coluna = self.acharLinhaColunaPeloNumerDaPoltrona(numero_poltrona)
        if self.__matriz[linha][coluna] is not None:
            # ASSENTO JA ESTA OCUPADO. EXCEÇÃO
            raise Exception('O assento {} já esta ocupado.'.format(numero_poltrona))
        self.__matriz[linha][coluna] = passageiro

    def acharLinhaColunaPeloNumerDaPoltrona(self, numero_poltrona: int):
        cadeira = 0
        for linha in range(len(self.__matriz)):
            for coluna in range(len(self.__matriz[linha])):
                cadeira = cadeira + 1
                if cadeira == numero_poltrona:
                    return (linha, coluna)

    def remover(self, numero_poltrona:int)->Passageiro:
        linha, coluna = self.acharLinhaColunaPeloNumerDaPoltrona(numero_poltrona)
        self.__matriz[linha][coluna] = None

    def esvaziar(self):
        '''Esvazia a matriz esparsa'''
        self.__matriz = MatrizEsparsa(self.__id, self.__linhas, self.__colunas)

    def mostrarAssentos(self):
        '''Mostra o status de ocupacao de todos os assentos'''
        totalDePoltronas = self.tamanho()
        for numeroPoltrona in range(1, totalDePoltronas + 1):
            statusDeOcupacao = "Desocupada"
            passageiroDaPoltrona = self.pesquisar(numeroPoltrona)
            if passageiroDaPoltrona is not None:
                statusDeOcupacao = "OCUPADA pelo passageiro {}".format(passageiroDaPoltrona)
            print("Poltrona {} {}".format(numeroPoltrona, statusDeOcupacao))

    def __str__(self):
        s = ''
        i = 0
        for m in self.__matriz:
            i+=1
            s+= f'{i}-{m}\n'
        s += f'{self.__id}, {self.tamanho()} assentos.'
        return s
