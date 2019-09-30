import random


class Hero:
    def __init__(self, name, health=100):
            #remember you can can declear a property with out putting it in the constructor.
        self.name = name
        self.health = health
        self.starting_health = health
        self.current_health = health
        self.abilities = list() # list of abilities and weapons
        self.armors = list()
        self.deaths = 0
        self.kills = 0
#add weapon to weapons list
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

#add ability to abilities list
    def add_ability(self, ability):
        self.abilities.append(ability)
#add armor  to armors list for hero
    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        #ADD abality to abilities list
        totalDamage = 0
        for ability in self.abilities:
            totalDamage += ability.attack()
        return totalDamage

# health is equal damage minus defend.
    def take_damage(self, damage):
        self.health -= damage - self.defend()


    def defend(self):

        totalDefense = 0
        for armor in self.armors:
            totalDefense += armor.block()

        if self.health <= 0:
            self.deaths += 1
            totalDefense = 0

        return totalDefense


    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        self.kills += num_kills

    def fight(self, opponent):

        while self.is_alive() and opponent.is_alive():

            heroAttack = self.attack()
            opponent.take_damage(heroAttack)

            opponentAttack = opponent.attack()
            self.take_damage(opponentAttack)

            if self.is_alive() == False:
                print("{} died".format(self.name))
                opponent.add_kill(1)
                self.deaths += 1
            if opponent.is_alive() == False:
                print("{} died".format(opponent.name))
                self.add_kill(1)
                opponent.deaths += 1


class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        randomAttackValue = random.randint(0, int(self.attack_strength))
        return randomAttackValue

    def update_attack(self, new_attack_strength):
        newAttackStrengthValue = self.randrange(attack_strength, new_attack_strength)
        return newAttackStrengthValue


class Weapon(Ability):

    def attack(self):
        randomAttackValue = random.randrange(int(self.attack_strength) // 2, int(self.attack_strength))
        return randomAttackValue


class Team:

    def __init__(self, name):
        self.name = name
        self.heroes = list()


    def healthCheck(self):
        total = 0
        for hero in self.heroes:
            total += hero.current_health
        return total

    def add_hero(self, Hero):
        self.heroes.append(Hero)


    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                indexOfHero = self.heroes.index(hero)
                del self.heroes[indexOfHero]
                return
        ''' did not find hero so give an error value '''
        return 0


    def view_all_heroes(self):
        ''' Prints all heroes to the console '''
        for hero in self.heroes:
            print(hero.name)


    def attack(self, other_team):

        randomElement = random.SystemRandom()

        ''' randomly select a living hero from each '''
        selfRandomHero = randomElement.choice(self.heroes)
        other_team_random_hero = randomElement.choice(other_team.heroes)

        ''' Fight until one or both teams have no surviving heroes '''
        while other_team_random_hero.current_health > 0:
            selfRandomHero.fight(other_team_random_hero)
            other_team_random_hero.current_health -= 1


    def revive_heroes(self, health=100):
        ''' Resets all heroes health to their original starting value.'''
        for hero in self.heroes:
            hero.health = health

    def stats(self):
        ''' Prints Kills/Deaths ratio for each hero'''
        for hero in self.heroes:
            if(hero.deaths > 0):
                print("{}: {}".format(self.name, (hero.kills/hero.deaths)))
            else:
                print("{}: {}".format(self.name, hero.kills))

    def still_alive(self):
        for hero in self.heroes:
            if hero.current_health > 0:
                return True
        return False


class Armor:

    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        randomValue = random.randrange(0, int(self.max_block))
        return randomValue


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''
        This method will allow a user to create an ability.

        Prompt the user for the necessary information to create a new ability object.

        return the new ability object.
        '''
        abilityName = input("\nAbility name: ")
        abilityDamage = input("How much damage attack will the ability {} have? (e.g 30): ".format(abilityName))

        return Ability(abilityName, abilityDamage)


    def create_weapon(self):
        '''
        This method will allow a user to create a weapon.

        Prompt the user for the necessary information to create a new weapon object.

        return the new weapon object.
        '''
        newAbilityName = input("\nOk! Let's create a weapon. What weapon do you want? (e.g shotgun): ")
        newAbilityStrength = input("How much damage do you want your {} to cause? (e.g 25): ".format(newAbilityName))

        return Weapon(newAbilityName, newAbilityStrength)

    def create_armor(self):
        '''
        This method will allow a user to create a piece of armor.

        Prompt the user for the necessary information to create a new armor object.

        return the new armor object.
        '''
        armorName = input("\nArmor type for hero (say something like medium light armor): ")
        armorStrength = input("Armor strength (say something like 25): ")

        return Armor(armorName, armorStrength)

    def create_hero(self):
        '''
        This method should allow a user to create a hero.

        User should be able to specify if they want armors, weapons, and abilites. Call the methods you made above and use the return values to build your hero.

        return the new hero object
        '''
        heroName = input("\nHero name: ")
        return Hero(heroName)



    def build_team_one(self):
        '''
        This method should allow a user to create team one.
        Prompt the user for the number of Heroes on team one and
        call self.create_hero() for every hero that the user wants to add to team one.

        Add the created hero to team one.
        '''
        teamOneName = input("Let's create the 1st team. What do you want to call them?: ")
        numberOfHeroes = int(input("How many heroes do you want to have in Team {}? (Say an integer like 2): ".format(teamOneName)))



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
        '''
        This method should allow a user to create team two.
        Prompt the user for the number of Heroes on team two and
        call self.create_hero() for every hero that the user wants to add to team two.

        Add the created hero to team two.
        '''
        teamTwoName = input("\nNow, Let's create the 2nd team. What do you want to call them?: ")
        numberOfHeroes = int(input("How many heroes do you want to have in Team {}? (Say an integer like 2): ".format(teamTwoName)))

        self.team_two = Team(teamTwoName)

        while numberOfHeroes > 0:
            numberOfHeroes -= 1
            self.team_two.heroes.append(self.create_hero())
        for hero in self.team_two.heroes:
            hero.armors.append(self.create_armor())
            hero.abilities.append(self.create_ability())
            hero.abilities.append(self.create_weapon())


    def alive_heroes(self):
        '''
        Creates a list of heroes who have health > 0
        '''
        alive_list = []
        #find out if team one has heroes alive
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)
        return alive_list


    def team_battle(self):
        '''
        This method should battle the teams together.
        Call the attack method that exists in your team objects to do that battle functionality.
        '''
        self.team_one.attack(self.team_two)



    def show_stats(self):
        '''
        This method should print out battle statistics
        including each team's average kill/death ratio.

        Required Stats:
        Declare winning team
        Show both teams average kill/death ratio.
        Show surviving heroes.
        '''
        print("STATS:")

        # show surviving heroes
        if self.team_one.healthCheck() < 1:
            print(self.team_two.name + " Wins")
            print("Surviving Heroes:")
            for x in self.team_two.heroes:
                if x.current_health > 0:
                    print(x.name)
        elif self.team_two.healthCheck() < 1:
            print(self.team_one.name + " Wins")
            print("Surviving Heroes:")
            for x in self.team_one.heroes:
                if x.current_health > 0:
                    print(x.name)
        print("Team KDR:")
        self.team_one.stats()
        self.team_two.stats()



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
