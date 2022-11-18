import random
from ability import Ability
from armor import Armor
from weapon import Weapon


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
    self.abilities = list()
    # Need to add Armors to our hero.
    self.armors = list()
    # Need to display deaths
    self.deaths = 0
    self.kills = 0

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

  def take_damage(self, damage):
    protection = self.defend()
    damage_impact = damage - protection
    if damage_impact > 0:
      self.current_health -= damage_impact

  def is_alive(self):
    if self.current_health <= 0:
      return False
    else:
      return True

  def fight(self, opponent):
    if not self.abilities and not opponent.abilities:
      print("Draw")
      return

    while self.is_alive() and opponent.is_alive():
      opponent.take_damage(self.attack())
      self.take_damage(opponent.attack())

      # Possible results during battle
      if self.is_alive() and not opponent.is_alive():
        print(f'{self.name} defeated {opponent.name}!')
        self.add_kill()
        opponent.add_death()
      elif not self.is_alive() and opponent.is_alive():
        print(f'{opponent.name} defeated {self.name}!')
        opponent.add_kill()
        self.add_death()
      elif not self.is_alive() and not opponent.is_alive():
        print(f'Both parties are dead!')
        self.add_kill()
        self.add_death()
        opponent.add_death()
        opponent.add_kill()


  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def add_kill(self, num_kills):
    self.kills += num_kills

  def add_death(self, num_deaths):
    self.deaths += num_deaths

if __name__ == "__main__":
  # hero1 = Hero("Wonder Woman")
  # hero2 = Hero("Dumbledore")
  # ability1 = Ability("Super Strength", 250)
  # ability2 = Ability("Lasso of Truth", 320)
  # ability3 = Ability("Avada Kedavra", 550)
  # ability4 = Ability("Expelliarmus", 500)
  # hero1.add_ability(ability1)
  # hero1.add_ability(ability2)
  # hero2.add_ability(ability3)
  # hero2.add_abilit(ability4)
  # hero1.fight(hero2)

  eye_rays = Ability('Eye Rays', 50)
  laser_blast = Weapon('Laser Blast', 50)
  powers = [eye_rays, laser_blast]
  for power in powers:
    print(power.max_damage)
  for power in powers:
    print(power.attack())