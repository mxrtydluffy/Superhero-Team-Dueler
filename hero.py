import random
from ability import Ability
from armor import Armor


class Hero:
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    # Need to assign our hero
    self.name = name
    # Similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # When a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
    # Need to add Abilities to our hero.
    self.abilities = list ()
    # Need to add Armors to our hero.
    self.armors = list()

def fight(self, opponent):
  winner = random.randint(0,1)
  if winner == 1:
    print(f'{self.name} defeated {opponent.name}!')
  else:
      print(f'{opponent.name} defeated {self.name}!')

def add_ability(self, ability):
  self.abilities.append(ability)

def attack(self):
  total_damage = 0
  for ability in self.abilites:
    total_damage += ability.attack()
  return total_damage

def add_armor(self, armor):
  self.armors.append(armor)

def defend(self):
  total_block = 0
  for armor in self.armors:
    total_block += armor.block()
    return total_block

if __name__ == "__main__":
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")
  hero1.fight(hero2)
  ability = Ability("Great Debugging", 50)
  ability2 = Ability("Invisibility", 150)
  hero = Hero("Dr. Strange", 200)
  hero.add_ability(ability)
  hero.add_ability(ability2)
  print(hero.attack())