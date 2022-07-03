class Passageiro:
    def __init__(self, nome, rg):
        self.__nome = nome
        self.__rg = rg

    def getNome(self):
        return self.__nome
        
    def getRg(self):
        return self.__rg
    
    def __str__(self):
        return f'{self.__nome} RG {self.__rg}'
