class Unit:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Soldier(Unit):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health)
        self.attack_power = attack_power
    def attack(self, enemy):
        enemy -= self.attack_power
class Archer(Unit):
    def __init__(self, name, health, range_attack_power):
        super().__init__(name, health)
        self.range_attack_power = range_attack_power
    def attack(self, enemy):
        enemy -= self.range_attack_power


print("gdssdhhjsdsjghhfvshdsuyfygeyueryuyeyuvfuyrvu")