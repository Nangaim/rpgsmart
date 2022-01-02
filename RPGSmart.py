from rogue_like import Boss1, Boss2, Final_Boss
from Menu import main_menu
from shop import fonction_shop
from fight import encounter
from inventaire import inventaire
from rogue_like import Monster_Encounter, Player_Movement, world_map, Monster_Movement, Goblin_Movement, Monster, Goblin, foe, Boss1


def Main():
    argent = 50
    liste_item_etage1 = ["potion", "bombe", "corde"]
    liste_prix_etage1 = [5, 10, 15]

    liste_item_etage2 = ["potion +", "bombe", "Cote Ã©pineuse"]
    liste_prix_etage2 = [20, 25, 30]

    liste_item_etage3 = ["potion X", "explo-bombe", "gucci loafers"]
    liste_prix_etage3 = [35, 40, 45]
    global y, x, inventaire
    y = int(19)
    x = int(14)
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
                inventaire, argent, liste_item_etage1, liste_prix_etage1)
        if y == 13 and x == 3:
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage2, liste_prix_etage2)
        if y == 3 and x == 10:
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage3, liste_prix_etage3)
        if y == 15 and x == 0:
            y, x = encounter(y, x, Boss1)
        if y == 7 and x == 14:
            y, x = encounter(y, x, Boss2)
        if y == 0 and x == 0:
            y, x = encounter(y, x, Final_Boss)
        else:
            Monster_Chance = Monster_Encounter()
            if Monster_Chance < 15:
                encounter(y, x, foe)
        world_map(y, x, monstery, monsterx, gobliny, goblinx)


Main()
