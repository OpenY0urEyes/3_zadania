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


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        a = abs(self.a[1]) + abs(self.b[1])
        b = self.b[0] - self.a[0]

        return round((a + b) * 2, 2)

    def area(self):
        a = round(abs(self.a[1]) + abs(self.b[1]), 2)
        b = round(self.b[0] - self.a[0], 2)

        return round((a * b), 2)



rect = Rectangle((3.2, -4.3), (7.52, 3.14))



print(rect.perimeter())
# print(rect.area())
