import random


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'up'
        self.shot_directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
        self.targets_hit = 0

    def move(self, direction_to_move):
        self.direction = direction_to_move
        if direction_to_move == 'up':
            self.y += 1
        elif direction_to_move == 'down':
            self.y -= 1
        elif direction_to_move == 'left':
            self.x -= 1
        elif direction_to_move == 'right':
            self.x += 1

    def shoot(self, targetx, targety):
        print('Shot done!')
        self.shot_directions[self.direction] += 1
        if self.x == targetx:
            if self.y < targety:
                if self.direction == 'up':
                    self.targets_hit += 1
                    return True
            else:
                if self.direction == 'down':
                    self.targets_hit += 1
                    return True
        if self.y == targety:
            if self.x < targetx:
                if self.direction == 'right':
                    self.targets_hit += 1
                    return True
            else:
                if self.direction == 'left':
                    self.targets_hit += 1
                    return True
        return False

    def info(self):
        print(f"Kryptis: {self.direction}")
        print(f"Koordinatės: {self.x}:{self.y}")
        print(f"Šūvių iš viso: {sum(self.shot_directions.values())}")
        print(f"{self.shot_directions}")
        print((f"Targets Hit: {self.targets_hit}"))


class Target:
    def __init__(self):
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)

    def reset(self):
        self.x = random.randint(-5, 5)
        self.y = random.randint(-5, 5)


tankutis = Tank()
takinys = Target()
POINTS = 100

print("Sveiki, Taisyklės kaip žaisti")

while POINTS != 0:
    print("Judesiai:")
    print("w: aukštyn, s: žemyn, a: kairėn, d: dešinėn")
    print("b: Boom, i: informacija, q: išeiti")
    print(f"x: {tankutis.x}, y: {tankutis.y}")
    x = str(input("Tavo pasirinkimas: "))
    POINTS -= 10
    if x == 'w':
        tankutis.move('up')
    elif x == 's':
        tankutis.move('down')
    elif x == 'a':
        tankutis.move('left')
    elif x == 'd':
        tankutis.move('right')
    elif x == 'b':
        if tankutis.shoot(takinys.x, takinys.y):
            print('Pataikei')
            POINTS += 50
            takinys.reset()
    elif x == 'i':
        tankutis.info()
    elif x == "q":
        print("GG")
        print(f"Targets Hit: {tankutis.targets_hit}")
        break
    elif x == "c":
        print(f"{takinys.x}: {takinys.y}")

print("Taškai baigėsi, ko dar nori?")



