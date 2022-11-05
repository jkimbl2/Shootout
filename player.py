from random import randint
class Player():
    #constructor, sets starting hp
    def __init__(self, health):
         self.health = health
         self.position = 'mid'
         self.supplies = 3
    #return important info as string
    def __str__(self):
        return f"You have {self.health} HP remaining. \nYou are in the {self.position} position. \nYou have {self.supplies} supplies remaining."
    #take a turn
    def turnActions(self):
        damage = 0
        isTurn = True
        while isTurn:
             #request attack
            attack = input('What would you like to do? (front, mid, back, shoot, heal, restock, status): ').lower()
            #do damage calculations
            #FRONT/MID/BACK: change position and do small damage. Position affects incoming and outgoing damage.
            if attack == 'front':
                self.position = 'front'
                damage = randint(5, 25)
                return damage
            if attack == 'mid':
                self.position = 'mid'
                damage = randint(2, 15)
                return damage
            if attack == 'back':
                self.position = 'back'
                damage = randint(1, 10)
                return damage
            #SHOOT: do larger damage, but without moving.
            if attack == 'shoot':
                if self.position == 'front':
                    damage = randint(10, 40)
                    return damage
                if self.position == 'mid':
                    damage = randint(5, 25)
                    return damage
                if self.position == 'back':
                    damage = randint(2, 15)
                    return damage
            #HEAL: Heal a random amount if you have the supplies.
            if attack == 'heal':
                if self.supplies > 1:
                    heal = randint(15,35)
                    self.health =  self.health + heal
                    print('Healed', heal , 'HP!')
                    print( self.health, 'HP total!')
                    print(self.supplies, 'supplies remain.\n')
                    self.supplies -= 1
                    isTurn = False
                else:
                    print('Not enough supplies!')
            #RESTOCK: replenishes healing options. has a chance to fail!
            if attack == 'restock':
                    if self.supplies < 3:
                            stockchance = randint(1,3)
                            if stockchance == 1:
                                    print('You failed to replenish supplies.')
                            elif stockchance == 2:
                                    print('You replenished one of your supplies.')
                                    self.supplies += 1
                            else:
                                    print('You replenished all supplies!')
                                    self.supplies = 3
                    else:
                            print('You tried to restock, but you couldn\'t carry any more supplies.')
                    isTurn = False
            #STATUS: print the return string
            if attack == 'status':
                print(self)
        return damage