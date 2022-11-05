from random import randint
class Enemy():
    #constructor
    def __init__(self, health):
     self.health = health
    #return string
    def __str__(self):
        return f"Enemy has {self.health} HP remaining."

    def turnActions(self,pos):
        damage = 0
        #roll enemy's attack
        enemyai = randint(1,10)
        #check for special conditions
        if enemyai == 1 or enemyai == 2:
            print('The enemy seems distracted...')
            return damage
        elif enemyai == 5:
            print('The enemy fires rapidly!')
            hittimes = randint(1,5)
            if pos == 'front':
                hitdamage = randint(2, 15)
            if pos == 'mid':
                hitdamage = randint(1,10)
            if pos == 'back':
                hitdamage = randint(1, 5)
            damage = hittimes * hitdamage
            print('Hit', hittimes , 'for' , hitdamage , 'each!')
            return damage
        elif enemyai == 10:
            print('The enemy rushes forward!')
            pos = 'front'
            print('Position changed to front!')
            damage = randint(2, 20)
            return damage
        #run normal attack.    
        else:
            print('The enemy fires!')
            if pos == 'front':
                damage = randint(5, 30)
            if pos == 'mid':
                damage = randint(2, 20)
            if pos == 'back':
                damage = randint(1,15)
            return damage