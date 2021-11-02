class Circulo:

    def __init__(self,raio):
        self.__raio = raio
        self.__area = raio * Circulo.__obter_pi()
        self.__perimetro = 2 * Circulo.__obter_pi() * (raio ^ 2)

    @staticmethod
    def __obter_pi():
        return 3.14

    @property
    def area(self):
        return self.__area

    @property
    def perimetro(self):
        return self.__perimetro

