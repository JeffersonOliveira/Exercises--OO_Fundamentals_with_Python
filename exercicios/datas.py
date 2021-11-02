
class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print('{}/{}/{}'.format(self.dia,self.mes, self.ano))

'''
    def formatada(self):
        print(f'{self.dia:02d}/{self.mes:02d}/{self.ano}')
                                
    def formatada(self):
        print(f'{self.dia:0>2}/{self.mes:0>2}/{self.ano}')
'''