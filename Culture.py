class Culture:
    def __init__(self, name):
        self.name = name


class Chinese(Culture):
    def __init__(self):
        super().__init__(name = 'Chinese')