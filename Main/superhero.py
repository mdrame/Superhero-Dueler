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

    def take_damage(self, damage_amt):
        self.current_health -= damage_amt

    def is_alive(self):
        if self.current_health <= 0:
            return False # hero is dead dude
        else:
            return True

    def fight(self, opponent): #  give  opponent same capibility in function
        while self.is_alive() and opponent.is_alive():
            # setting super heros up
            #both heros attack method return 2 different random int
            first_hero_attack = self.attack()
            opponent_attack = opponent.attack()

            #assiging heros damages/current life  base on attacks
            opponent.take_damage(first_hero_attack)
            self.take_damage(opponent_attack)

        if self.is_alive() == False and opponent.is_alive() == False:
            print("👾 : Draw Game!")
        elif self.is_alive() == False:
            print(f'{opponent.name} won')
        elif opponent.is_alive() == False:
            print(f'{self.name} won')







# super hero   ability
class Ability:

    def __init__(self, name, attack_strength):
       self.name = name
       self.attack_strength = attack_strength



    def attack(self):
      return random.randint(0,self.attack_strength)




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
    the_flash = Hero("The flask", 310)
    zoom = Hero("Zoom 🔱", 100)

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
