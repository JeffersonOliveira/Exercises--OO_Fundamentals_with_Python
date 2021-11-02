class Sistema:
    def __init__(self):
        self.texto = ''

    def ler_entrada(self):
        self.texto = input('Digite um texto: ')

    def exibe_saida(self):
        print('O texto digitado foi: \n{}'.format(self.texto))