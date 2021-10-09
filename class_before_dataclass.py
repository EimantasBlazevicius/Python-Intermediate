class Investor:
    def __init__(self, name, age, investment):
        self.name = name
        self.age = age
        self.investment = investment

    def __repr__(self):
        return f"{self.name} yra {self.age} amžiaus ir turi {self.investment} eurų investuoti"

    def __eq__(self, other):
        if self.investment == other.investment:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.investment < other.investment:
            return True
        else:
            return False

i1 = Investor("Petras", 25, 3000)
i2 = Investor("Jonas", 45, 33000)
i3 = Investor("Eimantas", 28, 3)
i4 = Investor("Gintare", 21, 3000)
i5 = Investor("Petras", 25, 3000)

#print(i1 == i4)
print(i3 < i4)