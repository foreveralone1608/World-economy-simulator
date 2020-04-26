class LowerClass:
    def __init__(self, rank = 'Lower Class'):
        self.rank = rank

class Craftmen(LowerClass):
    def __init__(self):
        LowerClass.__init__(self)
        self.name = 'Craftmean'
        self.need = ['Grain']
    def print(self):
        print(self.rank)

class Farmer(LowerClass):
    def __init__(self):
        LowerClass.__init__(self)
        self.name = 'Farmer'
        self.need = ['Grain']
    def print(self):
        print(self.rank)
c = Craftmen()
c.print()

