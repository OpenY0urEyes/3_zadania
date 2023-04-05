class Planet:
    def __init__(self, name):
        self.name = name

    def get_s(self, frome, to):
        s = frome*to
        return s

    def gravity(self, mass1, mass2, R):
        G = 6.67384 * 10.5
        F = G * ((mass1*mass2) / R**2)
        return F

planet = Planet("earth")
print(planet.name)
print(planet.get_s(10, 60))
print(planet.gravity(10, 30, 100))