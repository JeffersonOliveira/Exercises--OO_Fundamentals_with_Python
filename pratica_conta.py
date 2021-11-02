from builtins import property


class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print('Construindo um objeto... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

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
    def limite(self, limite):
        self.__limite = limite

    def extrato(self):
        print('O valor do Saldo de {} é: {}'.format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel_na_conta = self.__saldo + self.__limite
        return valor <= valor_disponivel_na_conta

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print('Saque Realizado!')
        else:
            print('Saque não realizado. Saldo e Limite insuficientes!')

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}


    def testa_codigo():
        from pratica_conta import Conta
        conta1 = Conta(1, 'jefferson', 3000.0)
        conta1 = Conta(2, 'marco', 4000.0)