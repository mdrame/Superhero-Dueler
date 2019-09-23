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
            if ability.attack() in ability: # checking to see is the method attack() is in ability.
                return ability.attack() # if attack() is in return it as an intiger ‼️.
            else:
                return = " Sorry there is no attack method in the abilities list ""



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

    flying = Ability(" Flying ", 100)
    invensibility = Ability(" Invensibility ", 99)
    the_flask = Hero("The flask", 100)
    the_flask.add_ability(flying)
    the_flask.add_ability(invensibility)
    print(the_flask.attack())
