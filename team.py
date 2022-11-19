import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    #removes hero from team
    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
            if not found_hero:
                return 0
    
    #Displaying all heroes
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths: {kd}")
    
    # current_health = starting_health
    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    # Attacking each team
    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # Selects random hero for each team
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            # Heros on both sides fight each other
            hero.fight(opponent) 
            
            # Updates list of living_heroes and living_opponents
            # Then reflects its data
            if hero.is_alive() == True:
                living_opponents.remove(opponent)
            else:
                living_heroes.remove(hero)