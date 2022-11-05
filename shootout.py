#Shootout, a test game by Josh Kimble
import player
import enemy
from random import randint

def main():
    #set start variables
    p1 = player.Player(100)
    e1 = enemy.Enemy(150)
    damage = 0
    instructions = 'notread'
    #start battle loop
    while instructions != 'read':
        print('This is a quick battle tutorial.')
        print('Each turn you will get a chance to move and shoot.')
        print('Being closer means you do more damage but also take more damage.')
        print('Being further means you do less damage and take less damage as well.')
        print('Shoot lets you do more damage from less range.')
        print('Heal lets you heal up some HP from any distance, as long as you have supplies.')
        print('Restock lets you replenish your medical supplies, and makes your heal effective once more.')
        print('If you need to check your position,health,and supplies, you can use the status command.')
        instructions = input('type "read" to confirm you understand: ').lower()
    for n in range (3):
        print('')
    while e1.health > 1 and p1.health > 1:
        print('You have', p1.health, 'HP left!')
        print('Enemy has', e1.health , 'HP left!\n')
        damage = p1.turnActions()
        if damage > 0:
            print('Enemy took' , damage , 'damage!')
            print('Enemy has', e1.health , 'HP left!\n')
            e1.health = e1.health - damage
        if e1.health > 1:
            damage = e1.turnActions(p1.position)
        if damage > 0:
            e1.health = e1.health - damage               
            print(damage ,'damage received!')
            print(p1.health ,'HP remains!\n')
    if p1.health < 0:
         print('You fall to your knees.')
         print('GAME OVER')
    else:
        print('Enemy has been defeated! You win!')

    

main()
