from pick import pick
from time import sleep
from rogue_like import Boss1, Boss2, Final_Boss, LvlDesign, master_sword
from Menu import shopkeeper1, shopkeeper2, shopkeeper3, zone2, zone3, scriptroshi1, scriptroshi2, scriptroshi3, finalboss4, script
from os import spawnle, system
from shop import fonction_shop
from fight import encounter, hp, hp_max, niveau, exp, lvlgain, atk, dfs
from inventaire import inventaire
from rogue_like import Monster_Encounter, Player_Movement, world_map, Monster_Movement, Goblin_Movement, LvlDesign


def Main():
    from rogue_like import lvl, Monster, Goblin, foe, Boss1, Boss2, Final_Boss, Master_Roshi
    argent = 50
    global inventaire, hp, hp_max, exp, niveau, lvlgain, master_sword_here, atk, sword
    liste_item_etage1 = ["potion", "bombe", "corde"]
    liste_prix_etage1 = [5, 10, 15]

    liste_item_etage2 = ["potion +", "bombe", "Cote épineuse"]
    liste_prix_etage2 = [20, 25, 30]

    liste_item_etage3 = ["potion X", "explo-bombe", "gucci loafers"]
    liste_prix_etage3 = [35, 40, 45]
    # 19,14
    y = 4
    x = 14
    gobliny = 19
    goblinx = 7
    monstery = 9
    monsterx = 10
    Player_Life = 1
    monsterdead = False
    Boss1dead = False
    Boss2dead = False
    master_dead = False
    Final_Bossdead = False
    visited = 0
    master_sword_here = False
    print("Pour bouger le personnage:")
    print(" -Haut  -bas \n -gauche  -droite")
    world_map(y, x, monstery, monsterx, gobliny, goblinx)
    print(f"argent: {argent}€       {hp}hp / {hp_max}hp")
    print(f"Stats: {atk}Atk        {dfs}dfs")
    print(f"niveau: {niveau}        {exp}xp / {lvlgain}xp")
    print(f"Votre inventaire: {inventaire}")
    sword = master_sword(master_dead)
    print(
        f"Vous possédez une épée basique: {sword}")
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
            if visited == 0:
                shopkeeper1()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage1, liste_prix_etage1)
            visited += 1
        if y == 13 and x == 3:
            if visited == 0:
                shopkeeper2()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage2, liste_prix_etage2)
            visited += 1
        if y == 3 and x == 10:
            if visited == 0:
                shopkeeper3()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage3, liste_prix_etage3)
            visited += 1
        if y == 15 and x == 0:
            Boss1dead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                Boss1, lvl)
            argent += argent_mob
            if Boss1dead == True:
                y -= 2
                world_map(y, x, monstery, monsterx, gobliny, goblinx)
                zone2()
                sleep(1)
                pass
        if y == 7 and x == 14:
            Boss2dead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                Boss2, lvl)
            argent += argent_mob
            if Boss2dead == True:
                y -= 2
                world_map(y, x, monstery, monsterx, gobliny, goblinx)
                zone3()
                sleep(1)
                pass

        if y == 3 and x == 14:
            if niveau > 10:
                # scriptroshi2()
                sleep(1)
                master_dead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                    Master_Roshi, lvl)
                if master_dead == True:
                    atk += 20
                    sword, master_sword_here = master_sword(master_dead)
                    # scriptroshi3()
                    world_map(y, x, monstery, monsterx, gobliny, goblinx)

            else:
                scriptroshi1()
                sleep(1)
                pass
        if y == 0 and x == 0:
            script(
                "Voilà donc l'insecte qui brise le silence de ces lieux... Je me montrerai magnanime à ton égard. Je te laisse le choix de partir.")
            sleep(3)
            title = "voulez vous partir ?"
            options = ["oui", "non"]
            choice, index = pick(
                options, title, indicator='=>', default_index=0)
            sleep(1)
            if choice == "non" or index == 1:
                Final_Bossdead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                    Final_Boss, lvl)
                if Final_Bossdead == True:
                    system("clear")
                    finalboss4()
            else:
                pass

        # if y == 0 and x == 0:
        #     encounter(Final_Boss, lvl)
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
        print(f"Stats: {atk}Atk        {dfs}dfs")
        print(f"Votre inventaire: {inventaire}")
        if master_sword_here == True:
            print(
                f"Vous possédez la master sword ! Votre attaque s'en retrouve décupler !")


Main()
