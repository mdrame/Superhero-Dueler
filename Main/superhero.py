import random

# Shout out to all the TA & Fellow class Mates for the help am greatful.

def welcomeStatement():
    print("Hey Player, welcome to Super Hero")

class Hero:
    def __init__(self, name, health=100):
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
        self.name = name
        self.health = health
        self.starting_health = health
        self.current_health = health
        self.abilities = list() # list of abilities and weapons
        self.armors = list()
        # The code you have already written goes here.
        # ...
        self.deaths = 0
        self.kills = 0

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''

        self.armors.append(armor)



    def add_ability(self, ability):

         # TODO: Add ability object to abilities:List
         self.abilities.append(ability)




    def attack(self):
        #ADD abality to abilities list
        totalDamage = 0
        for ability in self.abilities:
            totalDamage += ability.attack()
        return totalDamage

# health is equal damage minus defend.
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
  # TODO: Create a method that updates self.current_health to the current
  # minus the the amount returned from calling self.defend(damage).
        self.health -= damage - self.defend()


    def defend(self):
        '''Runs `block` method on each armor.
        Returns sum of all blocks
        '''
  # TODO: This method should run the block method on each armor in self.armors

        totalDefense = 0
        for armor in self.armors:
            totalDefense += armor.block()

        if self.health <= 0:
            self.deaths += 1
            totalDefense = 0

        return totalDefense


    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
  # TODO: Check whether the hero is alive and return true or false
        if self.health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
    # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

#important
    def add_deaths(self, num_deaths):

    # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def fight(self, opponent):
        #... The code you already wrote should be here ...

        #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight

        while self.is_alive() and opponent.is_alive():

            heroAttack = self.attack()
            opponent.take_damage(heroAttack)

            opponentAttack = opponent.attack()
            self.take_damage(opponentAttack)

            if self.is_alive() == False:
                print(f"{self.name} died lol")
                opponent.add_kill(1)
                self.deaths += 1
            if opponent.is_alive() == False:
                print(f"{opponent.name} died 👏🏾")
                self.add_kill(1)
                opponent.deaths += 1


class Ability:
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
        randomAttackValue = random.randint(0, int(self.attack_strength))
        return randomAttackValue

    def update_attack(self, new_attack_strength):
        newAttackStrengthValue = self.randrange(attack_strength, new_attack_strength)
        return newAttackStrengthValue


class Weapon(Ability):
        # TODO: Use what you learned to complete this method.

    def attack(self):
        randomAttackValue = random.randrange(int(self.attack_strength) // 2, int(self.attack_strength))
        return randomAttackValue


class Team:

    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
    # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = list()


    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        randomElement = random.SystemRandom()

        #randomly select a living hero from each
        selfRandomHero = randomElement.choice(self.heroes)
        other_team_random_hero = randomElement.choice(other_team.heroes)

        #Fight until one or both teams have no surviving heroes
        while other_team_random_hero.current_health > 0:
            selfRandomHero.fight(other_team_random_hero)
            other_team_random_hero.current_health -= 1


    def remove_hero(self, name):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            if hero.name == name:
                indexOfHero = self.heroes.index(hero)
                del self.heroes[indexOfHero]
                return

        return 0

#call static in team arena class
    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:
            if(hero.deaths > 0):
                print("{}: {}".format(self.name, (hero.kills/hero.deaths)))
            else:
                print("{}: {}".format(self.name, hero.kills))

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, Hero):
        self.heroes.append(Hero)


    def healthCheck(self):
        total = 0
        for hero in self.heroes:
            total += hero.current_health
        return total


    def revive_heroes(self, health=100):
        ''' Resets all heroes health to their original starting value.'''
        for hero in self.heroes:
            hero.health = health



    def still_alive(self):
        for hero in self.heroes:
            if hero.current_health > 0:
                return True
        return False


class Armor:
        # TODO: Create instance variables for the values passed in.
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        randomValue = random.randrange(0, int(self.max_block))
        return randomValue


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

    def create_ability(self):
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.

        abilityName = input("Ability name: ")
        abilityDamage = input("How much damage attack will the ability {} have ? : ".format(abilityName))
        print('\n')
        return Ability(abilityName, abilityDamage)


    def create_weapon(self):
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        newAbilityName = input("Let's create a weapon. What weapon do you want? : ")
        newAbilityStrength = input("How much damage do you want your {} to cause? : ".format(newAbilityName))
        print("\n")
        return Weapon(newAbilityName, newAbilityStrength)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        armorName = input("\nArmor type for hero : ")
        armorStrength = input("Armor strength : ")
        print('\n')
        return Armor(armorName, armorStrength)

    def create_hero(self):
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        heroName = input("\nHero name: ")
        return Hero(heroName)



    def build_team_one(self):
        '''Prompt the user to build team_one '''
        teamOneName = input("Teame One Name? : ")
        #remindeer: creat error handing code for string
        numberOfHeroes = int(input("How many heroes do you want to have in Team {}?  ".format(teamOneName)))
        self.team_one = Team(teamOneName)
        while numberOfHeroes > 0:
            # subtract num of heroes so while loop can end
            numberOfHeroes -= 1
            self.team_one.heroes.append(self.create_hero())
        for hero in self.team_one.heroes:
            hero.armors.append(self.create_armor())
            hero.abilities.append(self.create_ability())
            hero.abilities.append(self.create_weapon())

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        teamTwoName = input("Team Two Name? : ")
        numberOfHeroes = int(input("How many heroes do you want to have in Team {}? : ".format(teamTwoName)))
        self.team_two = Team(teamTwoName)

        while numberOfHeroes > 0:
            numberOfHeroes -= 1
            self.team_two.heroes.append(self.create_hero())
        for hero in self.team_two.heroes:
            hero.armors.append(self.create_armor())
            hero.abilities.append(self.create_ability())
            hero.abilities.append(self.create_weapon())

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)


    def show_stats(self):
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        print('\n')
        print("Statistics:")
        print("-------------\n")

        # show surviving heroes
        if self.team_one.healthCheck() < 1:
            # TODO: This method should print out battle statistics
            print(self.team_two.name + " Wins")
            print("------------------")
            print("Surviving Heroes:")
            for x in self.team_two.heroes:
                if x.current_health > 0:
                    print(x.name)
        elif self.team_two.healthCheck() < 1:
            print(self.team_one.name + " Wins")
            print("------------------")
            print("Surviving Heroes:")
            for x in self.team_one.heroes:
                if x.current_health > 0:
                    print(x.name)

        print("Team Kill/Death - Ratio :")
        self.team_one.stats()
        self.team_two.stats()


    def alive_heroes(self):
        alive_list = []
        #find out if team one has heroes alive
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)
        return alive_list









if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


    # #armors
    # flash_suit = Armor("Red Suit", 100)
    # flash_ring = Armor("Flask Ring 💍", 80)
    #
    # #abilities
    # #super hero 1
    # flying = Ability(" Flying ", 100)
    # invensibility = Ability(" Invensibility ", 99)
    # #super hero 2
    # super_speed = Ability("Super Speed", 300)
    # super_eye = Ability("Super Eyes", 130)
    #
    #
    # #heros ( name )
    # the_flash = Hero("The flask ⚡️ ", 30000)
    # zoom = Hero("Zoom 🔱", 10)
    #
    # #add abilities
    # the_flash.add_ability(flying)
    # the_flash.add_ability(invensibility)
    #
    # zoom.add_ability(super_speed)
    # zoom.add_ability(super_eye)
    #
    # #add armors
    # the_flash.add_armor(flash_suit)
    # the_flash.add_armor(flash_ring)
    # #take punch
    # the_flash.take_damage(10)
    #
    # # print(f"Attack Power: {the_flash.attack()}")
    # # print(f"Depense Power : {the_flash.defend()}")
    # # print(f"current health : {the_flash.current_health}")
    #
    # # checking to see if hero is alive or dead
    # #print(the_flash.is_alive())
    #
    # the_flash.fight(zoom)
