
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property  # serve para fazer o get;
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        print('Chamando @nome.setter nome()')
        self.__nome = nome
