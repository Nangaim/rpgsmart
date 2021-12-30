from Menu import main_menu
from shop import fonction_shop
from fight import encounter
from rogue_like import Monster_Encounter
from rogue_like import Player_Movement
from rogue_like import world_map
from rogue_like import Goblin_Movement


def Main():
    from Menu import main_menu
    from shop import fonction_shop
    from fight import encounter
    from rogue_like import Monster_Encounter, Player_Movement, world_map, Monster_Movement

    inventaire = []
    argent = 50
    liste_item = ["Potion", "Bombe", "item3"]
    liste_prix = [5, 10, 15]
    y = 19
    x = 14
    gobliny = 19
    goblinx = 7
    monstery = 9
    monsterx = 10
    Player_Life = 3

    print("Pour bouger le personnage:")
    print(" -Haut  -bas \n -gauche  -droite")
    world_map(y, x, monstery, monsterx, gobliny, goblinx)
    while Player_Life > 0:
        Move = input("Entrez une direction: ")
        y, x = Player_Movement(Move, y, x)
        monstery, monsterx = Monster_Movement(monstery, monsterx)
        gobliny, goblinx = Goblin_Movement(gobliny, goblinx)
        if y == monstery and x == monsterx:
            Monster_Encounter()
        if y == 16 and x == 13:
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item, liste_prix)

        else:
            Monster_Chance = Monster_Encounter()
            if Monster_Chance < 15:
                encounter()
        world_map(y, x, monstery, monsterx, gobliny, goblinx)


Main()
