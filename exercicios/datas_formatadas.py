
class Data:
    def __init__(self, day, month, year ):
        print('Construindo objeto Data... {}'.format(self))
        self.day = day
        self.month = month
        self.year = year

    def formatada(self):
        return f'{self.day:0>2}/{self.month:0>2}/{self.year}'
