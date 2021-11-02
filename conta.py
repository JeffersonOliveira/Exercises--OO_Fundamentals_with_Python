class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print('Construindo um objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = '001'

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

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def obtem_extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor <= valor_disponivel_para_saque

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} passou da soma do saldo e limite. Saque não realizado'.format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}

if __name__ == '__main__':
    conta1 = Conta(1, 'Jefferson', 2500.0)
    print(conta1.__dict__)
