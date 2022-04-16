from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # self.sort_index = self.age
        object.__setattr__(self, 'sort_index', self.age)

    def __str__(self):
        return f'{self.name}, {self.job}, {self.age}, {self.strength}'

p1 = Person('Lol', 'ass', 20)
p2 = Person('lmao', 'bitch', 21)
p3 = Person('Lol', 'ass', 20)

print(p1)

print(p1 == p3)

print(p1 < p2)

p3.age = 30