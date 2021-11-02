class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print('Construindo um objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def obtem_extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor



    def saca(self, valor):
        if self.__saldo >= valor:
            print('Saque realizado.')
            self.__saldo -= valor
        elif (self.__saldo + self.__limite) >= valor:
            print('Você está utilizando o seu limite para realizar esse saque: ')
            self.__saldo -= valor
        else:
            print('Você não possui limite suficiente para realizar essa operação.')
            print(f'O valor {valor} passou o limite')
            self.obtem_extrato()
            print(f'O Seu limite é: {self.__limite}')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

if __name__ == '__main__':
    conta1 = Conta(1, 'Jefferson', 2500.0)
    print(conta1.__dict__)
