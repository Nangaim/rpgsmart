from rogue_like import Boss1, Boss2, Final_Boss, LvlDesign
# from Menu import main_menu
from os import system
from shop import fonction_shop
from fight import encounter, hp, hp_max, niveau, exp, lvlgain
from inventaire import inventaire
from rogue_like import Monster_Encounter, Player_Movement, world_map, Monster_Movement, Goblin_Movement, LvlDesign


def Main():
    from rogue_like import lvl, Monster, Goblin, foe, Boss1, Boss2, Final_Boss
    argent = 50
    global inventaire, hp, hp_max, exp, niveau, lvlgain
    liste_item_etage1 = ["potion", "bombe", "corde"]
    liste_prix_etage1 = [5, 10, 15]

    liste_item_etage2 = ["potion +", "bombe", "Cote épineuse"]
    liste_prix_etage2 = [20, 25, 30]

    liste_item_etage3 = ["potion X", "explo-bombe", "gucci loafers"]
    liste_prix_etage3 = [35, 40, 45]
    y = 16
    x = 0
    gobliny = 19
    goblinx = 7
    monstery = 9
    monsterx = 10
    Player_Life = 1
    monsterdead = False
    Boss1dead = False
    Boss2dead = False
    Final_Bossdead = False

    print("Pour bouger le personnage:")
    print(" -Haut  -bas \n -gauche  -droite")
    world_map(y, x, monstery, monsterx, gobliny, goblinx)
    print(f"argent: {argent}€       {hp}hp / {hp_max}hp")
    print(f"niveau: {niveau}        {exp}xp / {lvlgain}xp")
    while Player_Life > 0:
        lvl = LvlDesign(y, lvl)
        Move = input("Entrez une direction: ")
        y, x = Player_Movement(Move, y, x)
        monstery, monsterx = Monster_Movement(monstery, monsterx)
        gobliny, goblinx = Goblin_Movement(gobliny, goblinx)
        if y == monstery and x == monsterx:
            monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                Monster, lvl)
            argent += argent_mob
        if y == gobliny and x == goblinx:
            encounter(Goblin, lvl)
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
            Boss1dead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                Boss1, lvl)
            argent += argent_mob
            if Boss1dead == True:
                y -= 2
                world_map(y, x, monstery, monsterx, gobliny, goblinx)
                pass
        if y == 7 and x == 14:
            Boss2dead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                Boss2, lvl)
            argent += argent_mob
            if Boss2dead == True:
                y -= 2
                world_map(y, x, monstery, monsterx, gobliny, goblinx)
                pass
        if y == 0 and x == 0:
            Final_Bossdead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                Final_Boss, lvl)
            if Final_Bossdead == True:
                system("clear")
                print("OMG POGGERS VOUS AVEZ VAINCU LE SOCIER MALEFIQUE")
        if y == 0 and x == 0:
            encounter(Final_Boss, lvl)
        else:
            Monster_Chance = Monster_Encounter()
            if Monster_Chance < 15:
                monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                    foe, lvl)
                if monsterdead == True:
                    argent += argent_mob

        world_map(y, x, monstery, monsterx, gobliny, goblinx)
        print(f"argent: {argent}€       {hp}hp / {hp_max}hp")
        print(f"niveau: {niveau}        {exp}xp / {lvlgain}xp")


Main()
