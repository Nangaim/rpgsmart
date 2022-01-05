from pick import pick
import msvcrt
from time import sleep
from map import Boss1, Boss2, Final_Boss, LvlDesign
# from menu import shopkeeper1, shopkeeper2, shopkeeper3, zone2, zone3, scriptroshi1, scriptroshi2, scriptroshi3, finalboss4, script, boss1, boss2, postgame, finalboss2, main_menu
from menu import *
from shop import fonction_shop
from fight import encounter, hp, hp_max, niveau, exp, lvlgain, atk, dfs
from inventory import inventaire
from map import Monster_Encounter, Player_Movement, world_map, Monster_Movement, Goblin_Movement, LvlDesign
from save import save, load
from os import system
# from menu import filename, want_load


def Main():

    global inventaire, hp, hp_max, exp, niveau, lvlgain, master_sword_here, atk, sword, dfs, filename, want_load, lvl, foe
    want_load = False
    filename, want_load = main_menu()

    if want_load == True:
        x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe = load(
            filename)
        pass
    else:
        from map import lvl, Monster, Goblin, foe, Boss1, Boss2, Final_Boss, Master_Roshi
        argent = 50

        liste_item_etage1 = ["Potion", "Bombe"]
        liste_prix_etage1 = [20, 30]

        liste_item_etage2 = ["Potion +", "Bombe"]
        liste_prix_etage2 = [30, 30]

        liste_item_etage3 = ["Potion X", "Explo-bombe"]
        liste_prix_etage3 = [40, 60]
        # 19,14
        y = 19
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
        visited2 = 0
        visited3 = 0
    Player_Life = 1

    world_map(y, x, monstery, monsterx, gobliny, goblinx)
    print(f"Argent: {argent}€       {hp}hp / {hp_max}hp")
    print(f"Stats: {atk}Atk        {dfs}dfs")
    print(f"Niveau: {niveau}        {exp}xp / {lvlgain}xp")
    print(f"Votre inventaire: {inventaire}")
    while Player_Life > 0:
        lvl = LvlDesign(y, lvl)
        char = msvcrt.getche().decode()
        # Move = input("Entrez une direction: ")
        Move = char
        y, x = Player_Movement(Move, y, x)
        monstery, monsterx = Monster_Movement(monstery, monsterx)
        gobliny, goblinx = Goblin_Movement(gobliny, goblinx)
        if y == 15 and x == 5:
            title3 = "Vous arrivez dans une zone de sauvegarde. Voulez vous y entrer ?"
            options3 = ["oui", "non"]
            choice, index = pick(
                options3, title3, indicator='=>', default_index=0)
            if choice == "oui" and index == 0:
                save(x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead,
                     Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe)
                # save
            else:
                pass
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
            y += 1
        if y == 13 and x == 3:
            if visited2 == 0:
                shopkeeper2()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage2, liste_prix_etage2)
            visited2 += 1
            y -= 1
        if y == 3 and x == 10:
            if visited3 == 0:
                shopkeeper3()
                sleep(1)
            inventaire, argent = fonction_shop(
                inventaire, argent, liste_item_etage3, liste_prix_etage3)
            visited3 += 1
            y += 1
        if y == 15 and x == 0:
            boss1()
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
            boss2()
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
                scriptroshi2()
                sleep(1)
                master_dead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                    Master_Roshi, lvl)
                if master_dead == True:
                    sleep(1)
                    scriptroshi3()
                    atk += 50
                    y += 1
                    world_map(y, x, monstery, monsterx, gobliny, goblinx)

            else:
                sleep(1)
                scriptroshi1()
                sleep(1)
                pass
        if y == 0 and x == 0:
            script(
                "Voilà donc l'insecte qui brise le silence de ces lieux... Je me montrerai magnanime à ton égard. Je te laisse le choix de partir.")
            sleep(3)
            title = "Voulez vous partir ?"
            options = ["oui", "non"]
            choice, index = pick(
                options, title, indicator='=>', default_index=0)
            sleep(1)
            finalboss2()
            sleep(1)
            if choice == "non" or index == 1:
                Final_Bossdead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                    Final_Boss, lvl)
                if Final_Bossdead == True:
                    sleep(1)
                    system("cls")
                    finalboss4()
                    sleep(1)
                    system("cls")
                    postgame()
                    sleep(2)
                    system("cls")
                    script(" ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░")
                    sleep(10)
                    break
            else:
                pass
        else:
            Monster_Chance = Monster_Encounter()
            if Monster_Chance < 15:
                monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain = encounter(
                    foe, lvl)
                if monsterdead == True:
                    argent += argent_mob
        if hp == 0:
            filename, want_load = main_menu()
            # break
        system('cls')
        world_map(y, x, monstery, monsterx, gobliny, goblinx)
        print(f"Argent: {argent}€       {hp}hp / {hp_max}hp")
        print(f"Niveau: {niveau}        {exp}xp / {lvlgain}xp")
        print(f"Stats: {atk}Atk        {dfs}dfs")
        print(f"Votre inventaire: {inventaire}")


Main()
