import random


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0



    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        for ability in self.abilities: #iterating over self.abilities list of object
            return ability.attack() # if attack() is in return it as an intiger ‼️.

    def defend(self):
        for armor in self.armors:
            return armor.block()

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.

        self.abilities.append(weapon)

    def take_damage(self, damage_amt):
        self.current_health -= damage_amt

    def is_alive(self):
        if self.current_health <= 0:
            return False # hero is dead dude
        else:
            return True

    def fight(self, opponent): #  give  opponent same capibility in function

        #... The code you already wrote should be here ...

        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        index = 0
        while self.is_alive() and opponent.is_alive():
            if len(opponent.abilities) == 0 and len(self.abilities) == 0:
                print("Hero's Draw !")
                break
            else:
                if index < len(opponent.abilities):
                    self.take_damage(opponent.abilities[index].attack_strength)
                if index < len(self.abilities):
                    opponent.take_damage(self.abilities[index].attack_strength)
                index += 1

        # update the number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight
        if self.is_alive():
            self.add_kill(1)
            opponent.add_deaths(1)
            print(self.name + " won!")
        else:
            opponent.add_kill(1)
            self.add_deaths(1)
            print(opponent.name + " won!")

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # This method should add the number of kills to self.kills
        self.kills += num_kills # incrementing kills variable
        return self.kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        return self.deaths






class Team:
    def __init__(self,name):
        ''' Initialize your team with its team name
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = list()


    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes

        self.heroes.append(hero)


    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return self.heroes
        # else return 0
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for superHeroes in self.heroes:
            print(superHeroes.name)


    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        # while loop as long as both hero object is present, and add to heroOne & heroTwo vatriable.
        while len(other_team.hero) > 0 and len(self.heroes) > 0:
            heroOne = self.heroes[randint(0, len(self.heroes))]
            heroTwo = other_team.heroes[randint(0, len(other_team.heroes))]
            if heroOne.is_alive() == False:
                self.heroes.remove_hero(hero.name)
            elif heroTwo.is_alive() == False:
                other_team.heroes.remove_hero(hero.name)
            else:
                heroOne.fight(heroTwo)


    def revive_heroes(self, health=100):
        # reset hero health to 100 which is == starting_health
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
             print(f"{hero.name} is one hell of a baddass current ratio of kills/deaths of {hero.kills//hero.deaths}.")






# super hero ability blueprint
class Ability:
    def __init__(self, name, attack_strength):
       self.name = name
       self.attack_strength = attack_strength



    def attack(self):
      return random.randint(0,self.attack_strength)

# inheratance of Ability class
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        return random.randint(self.attack_strength // 2, self.attack_strength)




# super hero weapons blueprint class
class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
        # TODO: Create instance variables for the values passed in.
    def block(self):
        return random.randint(0, self.max_block)


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = None
        self.team_two = None
        self.winning_team = None





#testing

if __name__ == "__main__":

    #armors
    flash_suit = Armor("Red Suit", 100)
    flash_ring = Armor("Flask Ring 💍", 80)

    #abilities
    #super hero 1
    flying = Ability(" Flying ", 100)
    invensibility = Ability(" Invensibility ", 99)
    #super hero 2
    super_speed = Ability("Super Speed", 300)
    super_eye = Ability("Super Eyes", 130)


    #heros ( name )
    the_flash = Hero("The flask ⚡️ ", 30000)
    zoom = Hero("Zoom 🔱", 10)

    #add abilities
    the_flash.add_ability(flying)
    the_flash.add_ability(invensibility)

    zoom.add_ability(super_speed)
    zoom.add_ability(super_eye)

    #add armors
    the_flash.add_armor(flash_suit)
    the_flash.add_armor(flash_ring)
    #take punch
    the_flash.take_damage(10)

    # print(f"Attack Power: {the_flash.attack()}")
    # print(f"Depense Power : {the_flash.defend()}")
    # print(f"current health : {the_flash.current_health}")

    # checking to see if hero is alive or dead
    #print(the_flash.is_alive())

    the_flash.fight(zoom)
