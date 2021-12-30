from Menu import main_menu
from shop import fonction_shop
from fight import encounter
from rogue_like import Monster_Encounter
from rogue_like import Player_Movement
from rogue_like import world_map
from rogue_like import Goblin_Movement
from inventaire import inventaire
from rogue_like import Boss1


def Main():
    from Menu import main_menu
    from shop import fonction_shop
    from fight import encounter
    from rogue_like import Monster_Encounter, Player_Movement, world_map, Monster_Movement, Goblin_Movement, Monster, Goblin, foe, Boss1
    argent = 50
    liste_item = ["Potion", "Bombe", "item3"]
    liste_prix = [5, 10, 15]
    global y, x, inventaire
    y = 19
    x = 14
    gobliny = 19
    goblinx = 7
    monstery = 9
    monsterx = 10
    Player_Life = 1

    print("Pour bouger le personnage:")
    print(" -Haut  -bas \n -gauche  -droite")
    world_map(y, x, monstery, monsterx, gobliny, goblinx)
    while Player_Life > 0:
        Move = input("Entrez une direction: ")
        y, x = Player_Movement(Move, y, x)
        monstery, monsterx = Monster_Movement(monstery, monsterx)
        gobliny, goblinx = Goblin_Movement(gobliny, goblinx)
        if y == monstery and x == monsterx:
            encounter(y, x, Monster)
        if y == gobliny and x == goblinx:
            encounter(y, x, Goblin)
        if y == 16 and x == 13:
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item, liste_prix)
        if y == 13 and x == 3:
            encounter(y, x, Boss1)
        else:
            Monster_Chance = Monster_Encounter()
            if Monster_Chance < 15:
                encounter(y, x, foe)
        world_map(y, x, monstery, monsterx, gobliny, goblinx)


Main()
