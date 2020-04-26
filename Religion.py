class Religion:
    def __init__(self, name):
        self.name = name


class Taoist(Religion):
    def __init__(self):
        super().__init__(name = 'Taoist')