#Shootout, a test game by Josh Kimble
import os
from random import randint
def main():
    #set start variables
    playerhp = int(100)
    enemyhp = int(150)
    phase = "player"
    attackturn = 1
    enemyturn = 0
    enemyatk = 0
    damage = 0
    restock = 1
    battlepos = 'mid'
    instructions = 'notread'
    #start battle loop
    while instructions != 'read':
        print('This is a quick battle tutorial.')
        print('Each turn you will get a chance to move and shoot.')
        print('Being closer means you do more damage but also take more damage.')
        print('Being further means you do less damage and take less damage as well.')
        print('Shoot lets you do more damage from less range.')
        print('Heal lets you heal up some HP from any distance. This gets weaker over time.')
        print('Restock lets you replenish your medical supplies, and makes your heal effective once more.')
        print('If you need to check your position and health, you can use the status command.')
        instructions = input('type "read" to confirm you understand: ').lower()
    for n in range (3):
        print('')
    
    while enemyhp > 1 and playerhp > 1:
        if attackturn == 1:
             #request attack
            attack = input('What would you like to do? (front, mid, back, shoot, heal, restock, status): ').lower()
            #do damage calculations
            if attack == 'front':
                battlepos = 'front'
                damage = randint(5, 25)
                enemyhp = enemyhp - damage
                print('Enemy took' , damage , 'damage!')
                print('Enemy has', enemyhp , 'HP left!')
                attackturn = 0
                enemyturn = 1
            if attack == 'mid':
                battlepos = 'mid'
                damage = randint(2, 15)
                enemyhp = enemyhp - damage
                print('Enemy took' , damage , 'damage!')
                print('Enemy has', enemyhp , 'HP left!')
                attackturn = 0
                enemyturn = 1
            if attack == 'back':
                battlepos = 'back'
                damage = randint(1, 10)
                enemyhp = enemyhp - damage
                print('Enemy took' , damage , 'damage!')
                print('Enemy has', enemyhp , 'HP left!')
                attackturn = 0
                enemyturn = 1
            if attack == 'shoot':
                if battlepos == 'front':
                    damage = randint(10, 40)
                    enemyhp = enemyhp - damage
                    print('Enemy took' , damage , 'damage!')
                    print('Enemy has', enemyhp , 'HP left!')
                if battlepos == 'mid':
                    damage = randint(5, 25)
                    enemyhp = enemyhp - damage
                    print('Enemy took' , damage , 'damage!')
                    print('Enemy has', enemyhp , 'HP left!')
                if battlepos == 'back':
                    damage = randint(2, 15)
                    enemyhp = enemyhp - damage
                    print('Enemy took' , damage , 'damage!')
                    print('Enemy has', enemyhp , 'HP left!')
                attackturn = 0
                enemyturn = 1
            if attack == 'heal':
                heal = 30//restock
                playerhp = playerhp + heal
                print('Healed', heal , 'HP!')
                print(playerhp, 'HP total!')
                restock += 1
                attackturn = 0
                enemyturn = 1
            if attack == 'restock':
                    if restock > 1:
                            stockchance = randint(1,3)
                            if stockchance == 1:
                                    print('You failed to replenish supplies.')
                                    attackturn = 0
                                    enemyturn = 1
                            elif stockchance == 2:
                                    print('You replenished some supplies. healing x2!')
                                    restock-=1
                                    attackturn = 0
                                    enemyturn = 1
                            else:
                                    print('You replenished all supplies! Heals are back to 30!')
                                    restock = 1
                                    attackturn = 0
                                    enemyturn = 1
                    else:
                            print('You tried to restock, but you couldn\'t carry any more supplies.')
                            attackturn = 0
                            enemyturn = 1
            if attack == 'status':
                print('You have', playerhp, 'HP left!')
                print('Enemy has', enemyhp , 'HP left!')
                print('You are in the', battlepos, 'position!')

        if enemyhp > 0:
            if enemyturn == 1:
                #roll enemy's attack
                enemyai = randint(1,10)
                #check for special conditions
                if enemyai == 1 or enemyai == 2:
                    print('The enemy seems distracted...')
                    enemyturn = 0
                    attackturn = 1
                elif enemyai == 5:
                    print('The enemy fires rapidly!')
                    hittimes = randint(1,5)
                    if battlepos == 'front':
                        hitdamage = randint(2, 15)
                    if battlepos == 'mid':
                        hitdamage = randint(1,10)
                    if battlepos == 'back':
                        hitdamage = randint(1, 5)
                    enemyatk = hittimes * hitdamage
                    print('Hit', hittimes , 'for' , hitdamage , 'each!')
                    playerhp = playerhp - enemyatk
                    print(enemyatk ,'damage received!')
                    print(playerhp ,'HP remains!')
                    enemyturn = 0
                    attackturn = 1
                elif enemyai == 10:
                    print('The enemy rushes forward!')
                    battlepos = 'front'
                    print('Position changed to front!')
                    enemyatk = randint(2, 20)
                    playerhp = playerhp - enemyatk
                    print(enemyatk ,'damage received!')
                    print(playerhp ,'HP remains!')
                    enemyturn = 0
                    attackturn = 1
                #run normal attack.    
                else:
                    print('The enemy fires!')
                    if battlepos == 'front':
                        enemyatk = randint(5, 30)
                    if battlepos == 'mid':
                        enemyatk = randint(2, 20)
                    if battlepos == 'back':
                        enemyatk = randint(1,15)
                    playerhp = playerhp - enemyatk
                    print(enemyatk ,'damage received!')
                    print(playerhp ,'HP remains!')
                    enemyturn = 0
                    attackturn = 1
    if playerhp < 0:
         print('You fall to your knees.')
         print('GAME OVER')
    else:
        print('Enemy has been defeated! You win!')

    

main()
