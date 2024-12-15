import random

class Human:
    def __init__(self, name, efficiency):
        self.name = name
        self.efficiency = efficiency
        self.resources = 0

    def mine(self, available):
        mined = min(random.randint(1, self.efficiency), available)
        self.resources += mined
        return mined

class Work:
    def __init__(self, resources):
        self.resources = resources
        self.humans = []

    def add_human(self, human):
        self.humans.append(human)

    def work_day(self):
        for human in self.humans:
            if self.resources > 0:
                self.resources -= human.mine(self.resources)

work = Work(100)

humans = [Human("Михайло", 10), Human("Микола", 15), Human("Человек Паук ", 7)]
for human in humans:
    work.add_human(human)

for day in range(1, 6):
    print(f"Дкнь {day}")
    work.work_day()
    print(f"Фарма в шахте залишилось: {work.resources}")
    for human in work.humans:
        print(f"{human.name} видобув: {human.resources}")
    if work.resources <= 0:
        print("Увесь фарм видобуто.")
        break
