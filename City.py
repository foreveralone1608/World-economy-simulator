import random
class world:
    def __init__(self):
        self.Cities = []
    def add_city(self, city):
        self.Cities.append(city)
    def migration(self):
        for i in range(len((self.Cities))):
            r = random.randint(0, 5)
            self.Cities[i].population[1][1] -= r
            for j in range(len(self.Cities)):
                r1 = r
                r2 = random.randint(0, r1)
                if j != i:
                    self.Cities[j].population[1][1] += r2
                    r1 -= r2
    def print(self):
        for i in range(len(self.Cities)):
            print(self.Cities[i].name+ ' ' + str(self.Cities[i].population))
class city:
    def __init__(self, name, owner, core, population = []):
        self.name = name
        self.owner = owner
        self.core = core
        self.population = population

    def print(self):
        print(self.name)
        for i in self.population:
            print(self.population[i])
