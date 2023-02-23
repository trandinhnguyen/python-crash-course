from random import randint


class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


if __name__ == '__main__':
    n_sides = [6, 10, 20]

    for sides in n_sides:
        dice = Die(sides)
        for _ in range(10):
            dice.roll_die()
        print()
