from dataclasses import dataclass, field, InitVar


@dataclass(order=True)
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str = field(repr=False, default="Jon Doe")
    age: InitVar[int] = field(repr=False, default=18)
    investment: float = field(default=15)
    able: bool = field(init=False, default=True)

    def __post_init__(self, age):
        self.sort_index = self.investment
        if age < 18:
            self.able = False


i1 = Investor("Petras", 25, 3000)
i2 = Investor("Jonas", 45, 33000)
i3 = Investor("Eimantas", 28, 3)
i4 = Investor("Gintare", 2, 3000)
i5 = Investor("Petras", 25, 3000)

print(i4)
# print(i3 > i4)