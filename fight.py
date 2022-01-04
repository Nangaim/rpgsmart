# from _typeshed import Self
from os import system
from pick import pick
from random import randint
from inventaire import fonction_inventory, inventaire
from Menu import finalboss3

# IMPORT DES BOSS A FAIRE DANS /ROGUE_LIKE.PY
# Boss1dead, Boss2dead, Final_Bossdead
from rogue_like import Goblin, Monster, foe, Boss1, Boss2, Final_Boss, Master_Roshi
global hp, hpmonster, playerdead, monsterdead, monster_name
hp_max = 1000
hp = 1000
exp = 0
niveau = 11
lvlgain = 100
atk = 100
dfs = 5
agi = 5
strike = 1
playerdead = False
monster_name = None

# ici fabien j'ai du corriger son code car il arrive pas a me faire un menu de combat en 4 jours
# Trigger : définir l'ennemi
# Choice : faire face ou fuir
# attack et attackmonster: define le coup du joueur (ou du monstre) quand il attaque (+ coups critiques)
# hpcount : calcul des hp restant + qui frappe en premier
# attaquer : séquence entière des 3 fonctions nommées au dessus
# fight : tout l'ensemble du fight et ses choix (inventory etc)
# encounter : trigger fight si le joueur choisit de se battre


def attack(atk, agi, agimonster, strike):
    chancecrit = randint(0, 10)
    if chancecrit <= agi:
        crit = 1
    else:
        crit = 0
    randhit = 1
    if crit == 1:
        strike = (atk*2)*randhit
    else:
        strike = atk*randhit
    dodgechance = randint(1, 20)
    if dodgechance <= agimonster:
        strike = 0
        print("Vous n'êtes pas assez rapide et manquez votre attaque ! ")
        input("Appuyez sur Entrée pour continuer...")
    else:
        strike = strike
    return strike


def attackmonster(atkmonster, agi, agimonster, strikemonster):
    chancecrit = randint(0, 10)
    if chancecrit <= agimonster:
        crit = 1
    else:
        crit = 0
    randhit = 1
    if crit == 1:
        strikemonster = (atkmonster*2)*randhit
    else:
        strikemonster = atkmonster*randhit
    dodgechance = randint(1, 20)
    if dodgechance <= agi:
        strikemonster = 0
        print("Vous êtes assez rapide et esquivez l'attaque de peu")
        input("Appuyez sur Entrée pour continuer...")
        system("clear")
    else:
        strikemonster = strikemonster
    return strikemonster


def hpcount(strike, strikemonster, enemy):
    global hp, hpmonster, playerdead, monsterdead, adversary, Boss1dead, Boss2dead, Final_Bossdead, atkmonster, dfsmonster, if_low

    if hp > 0 and hpmonster > 0:
        if agi >= agimonster:
            armormonster = dfsmonster
            strike = strike - armormonster
            if strike < 0:
                strike = 0
            hpmonster = hpmonster - strike
            print("Vous avez infligé", strike,
                  "Pts de dégâts au", monster_name, " ! ")
            armor = dfs
            strikemonster = strikemonster - armor
            if strikemonster < 0:
                strikemonster = 0
            hp = hp - strikemonster
            print("Le", monster_name, "Vous a infligé",
                  strikemonster, "Pts de dégats ! ")
            input("Appuyez sur Entrée pour continuer...")
        else:
            armor = dfs
            strikemonster = strikemonster - armor
            if strikemonster < 0:
                strikemonster = 0
            hp = hp - strikemonster
            print("Le", monster_name, "Vous a infligé",
                  strikemonster, "Pts de dégats ! ")
            input("Appuyez sur Entrée pour continuer...")
            armormonster = dfsmonster
            strike = strike - armormonster
            if strike < 0:
                strike = 0
            hpmonster = hpmonster - strike
            print("Vous avez infligé", strike,
                  "Pts de dégâts au", monster_name, " ! ")
    if hp <= 0:
        hp = 0
        playerdead = True
        return (hp, hpmonster, playerdead, monsterdead)
    elif hpmonster < 400 and if_low == 0:
        if monster_name == "Boss Final":
            finalboss3()
            atkmonster += 15
            dfsmonster += 15
        if_low += 1

    elif hpmonster < 0:
        if monster_name == "Boss 1":
            hpmonster = 0
            Boss1dead = True
            return (hp, hpmonster, playerdead, Boss1dead)
        if monster_name == "Boss 2":
            hpmonster = 0
            Boss2dead = True
            return (hp, hpmonster, playerdead, Boss2dead)

        if monster_name == "Master Roshi":
            hpmonster = 0
            master_dead = True
            return (hp, hpmonster, playerdead, master_dead)

        if monster_name == "Boss Final":
            hpmonster = 0
            Final_Bossdead = True
            return (hp, hpmonster, playerdead, Final_Bossdead)
        else:
            hpmonster = 0
            monsterdead = True
            return (hp, hpmonster, playerdead, monsterdead)

    return (hp, hpmonster, playerdead, monsterdead)


def attaquer(strike, strikemonster, atk, agi, agimonster, enemy):
    strike = attack(atk, agi, agimonster, strike)
    strikemonster = attackmonster(atkmonster, agi, agimonster, strikemonster)
    hp, hpmonster, playerdead, monsterdead = hpcount(
        strike, strikemonster, enemy)


def fight(enemy, strike, strikemonster, atk, agi, agimonster):
    global hp
    global hpmonster, if_low
    if_low = 0
    print("Vous faîtes face au", monster_name, "sauvage !")
    while hp > 0 and hpmonster > 0:
        print("PV du ", monster_name, "sauvage : ", hpmonster, "PV")
        print("Il vous reste actuellement", hp, "Points de vie.")
        title = f"Vous affrontez {monster_name} \n Il vous reste {hp} HP \n Que voulez-vous faire ?"
        options = ["attaquer", "inventaire", "fuir"]
        fight1, index = pick(options, title, indicator='=>', default_index=0)
        if fight1 == "attaquer" or index == 0:
            attaquer(strike, strikemonster, atk, agi, agimonster, enemy)
        elif fight1 == "inventaire" or index == 1:
            # MANAGE INVENTORY
            used = fonction_inventory(inventaire, hp, hp_max, atk)
            if used == True:
                strikemonster = attackmonster(
                    atkmonster, agi, agimonster, strikemonster)
                hp, hpmonster, playerdead, monsterdead = hpcount(
                    strike, strikemonster, enemy)

            pass
        elif fight1 == "fuir" or index == 2:
            break


def exp_gain(hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain):
    global gain
    if adversary == foe:
        if lvl == 1:
            gain = randint(40, 50)
        if lvl == 2:
            gain = randint(50, 65)
        if lvl == 3:
            gain = randint(65, 80)
    elif adversary == Goblin:
        gain = randint(25, 45)
    elif adversary == Monster:
        gain = randint(500, 800)
    elif adversary == Boss1:
        gain = randint(250, 300)
    elif adversary == Boss2:
        gain = randint(500, 800)
    elif adversary == Master_Roshi:
        gain = randint(1000, 1001)
    elif adversary == Final_Boss:
        gain = randint(1, 2)

    exp += gain

    while exp >= lvlgain:
        niveau += 1
        exp -= lvlgain
        lvlgain = round(lvlgain * 1.5)
        title = f"Vous avez gagner un niveau, vous etes niveau {niveau} quel stat voulez vous augmenter"
        options = ["Vie", "Attaque", "Défense"]
        choix_up, index = pick(options, title, indicator='=>', default_index=0)
        if index == 0:
            hp_max += 10
        elif index == 1:
            atk += 4
        elif index == 2:
            dfs += 4
    return hp_max, exp, niveau, atk, dfs, lvlgain


def encounter(adversary, lvl):
    global hp, hpmonster, playerdead, monsterdead, atkmonster, dfsmonster, agimonster, monster_name, atk, agi, dfs, exp, niveau, hp_max, Boss1dead, Boss2dead, Final_Bossdead, lvlgain, master_dead
    Boss1dead = False
    Boss2dead = False
    master_dead = False
    Final_Bossdead = False
    if adversary == foe:
        if lvl == 1:
            foes_name = ['Thierry Le Maignan', 'Sandie La Malice',
                         'Julien le rusé', 'Fabien le ténébreux', 'Baptiste le moine']
            monster_name = foes_name[randint(0, 4)]
            hpmonster = 50
            atkmonster = 10
            dfsmonster = 2
            agimonster = 5
            strikemonster = 1
            monsterdead = False
            argent_mob = randint(5, 10)
        if lvl == 2:
            foes_name2 = ['Springtrap', 'Maitre soupier',
                          'Carlos', 'Théo Duval', 'Floppa']
            monster_name = foes_name2[randint(0, 4)]
            hpmonster = 150
            atkmonster = 15
            dfsmonster = 3
            agimonster = 5
            strikemonster = 1
            monsterdead = False
            argent_mob = randint(10, 20)
        if lvl == 3:
            foes_name3 = ['Big Floppa', 'Big Chungus',
                          'Biggy Burger', 'дpyr', 'Baptiste le moine']
            monster_name = foes_name3[randint(0, 4)]
            hpmonster = 250
            atkmonster = 20
            dfsmonster = 5
            agimonster = 5
            strikemonster = 1
            monsterdead = False
            argent_mob = randint(20, 30)

    if adversary == Goblin:
        monster_name = "Goblin"
        hpmonster = 100
        atkmonster = 10
        dfsmonster = 2
        agimonster = 10
        strikemonster = 1
        monsterdead = False

    if adversary == Monster:
        monster_name = "Monster"
        hpmonster = 400
        atkmonster = 25
        dfsmonster = 10
        agimonster = 5
        strikemonster = 1
        monsterdead = False
        argent_mob = randint(40, 50)

    if adversary == Boss1:
        monster_name = "Boss 1"
        hpmonster = 250
        atkmonster = 20
        dfsmonster = 10
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = randint(20, 30)

    if adversary == Boss2:
        monster_name = "Boss 2"
        hpmonster = 500
        atkmonster = 30
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = randint(50, 60)

    if adversary == Master_Roshi:
        monster_name = "Master Roshi"
        hpmonster = 650
        atkmonster = 30
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = 0

    if adversary == Final_Boss:
        monster_name = "Boss Final"
        hpmonster = 800
        atkmonster = 35
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        argent_mob = 0

    # print(f"Vous rencontrez un {monster_name} 🙀")
    title = f"Vous rencontrez un {monster_name} 🙀 \n Que voulez-vous faire ?"
    options = ["Fuir", "Attaquer"]
    choix, index = pick(options, title, indicator='=>', default_index=0)


# choix = (input("Que faire? "))
    system("clear")
    # choix = choix.strip()
    while playerdead != True or monsterdead != True:
        if choix == "attaquer" or index == 1:
            fight(adversary, strike, strikemonster, atk, agi, agimonster)
            if monsterdead == True:
                system("clear")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)

                print(f"Vous avez gagner {exp}xp/{lvlgain}")
                print(f"Vous êtes niveau {niveau}")
                print(f"Le monstre vous a donné {argent_mob}€")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain
            if Boss1dead == True:
                system("clear")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagner {exp}xp/{lvlgain}")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return Boss1dead, hp, argent_mob, hp_max, exp, niveau, lvlgain
            if Boss2dead == True:
                system("clear")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagner {exp}xp/{lvlgain}")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return Boss2dead, hp, argent_mob, hp_max, exp, niveau, lvlgain

            if master_dead == True:
                system("clear")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagner {exp}xp/{lvlgain}")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return master_dead, hp, argent_mob, hp_max, exp, niveau, lvlgain

            if Final_Bossdead == True:
                system("clear")
                print("Vous avez vaincu le", monster_name, "sauvage !")
                print("Il vous reste", hp, "Points de vie")
                hp_max, exp, niveau, atk, dfs, lvlgain = exp_gain(
                    hp_max, exp, niveau, atk, dfs, adversary, lvl, lvlgain)
                print(f"Vous avez gagner {exp}xp/{lvlgain}")
                print(f"Vous êtes niveau {niveau}")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return Final_Bossdead, hp, argent_mob, hp_max, exp, niveau, lvlgain
            if playerdead == True:
                system("clear")
                print(""" 
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
    """)
                print("Vous avez été vaincu par le ",
                      monster_name, "sauvage !")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return playerdead, hp, argent_mob, hp_max, exp, niveau, lvlgain
        if choix == "fuir" or index == 0:
            monsterdead == False
            argent_mob == 0
            return monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain
        else:
            system("clear")
            title = "Vous allez quitter la combat !"
            options = ["Quitter"]
            choix, index = pick(
                options, title, indicator='=>', default_index=0)
            if choix == "Quitter":
                monsterdead == False
                argent_mob == 0
                return monsterdead, hp, argent_mob, hp_max, exp, niveau, lvlgain
