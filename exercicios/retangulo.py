
class Retangulo:
    def __init__(self, lado1, lado2):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__area = self.__lado1 * self.__lado2

    def obter_area(self):
        return self.__area
