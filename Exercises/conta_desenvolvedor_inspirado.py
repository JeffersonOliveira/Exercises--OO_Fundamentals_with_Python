class Conta:

    def __init__(self, numero, saldo, limite ):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0

    def __temSaldoDisponivelPara(self,valor):
        __valor_total_disponivel = self.__saldo + self.__limite
        return valor < __valor_total_disponivel

    def saca(self,valor):
        if self.__temSaldoDisponivelPara(valor):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")

    def deposita(self,valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        valorTotal = valor + self.__tarifaTransferencia

        if self.__temSaldoDisponivelPara(valorTotal):
            self.__saldo -= valorTotal
            destino.deposita(valor)
            print("Transferência efetuada.")
        else:
            print("Saldo insuficiente.")