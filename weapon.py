from ability import Ability
import random


class Weapon(Ability):
    def attack(self):
        min_damange = self.max_damage // 2
        random_value = random.randint(min_damange, self.max_damage)
        return random_value