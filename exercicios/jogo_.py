class Jogo:
    def __init__(self, nome, vezes_que_joguei):
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_joguei

    def get_nome(self):
        return self.__nome

    def get_vezes_que_joguei(self):
        return self.__vezes_que_joguei

    def joga(self):
        self.__vezes_que_joguei += 1

