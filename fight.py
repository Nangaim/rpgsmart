# from _typeshed import Self
from os import system
from pick import pick
from rogue_like import Goblin
from rogue_like import Monster
from rogue_like import foe
from random import randint
from inventaire import fonction_inventory, inventaire

# IMPORT DES BOSS A FAIRE DANS /ROGUE_LIKE.PY
# Boss1dead, Boss2dead, Final_Bossdead
from rogue_like import Boss1, Boss2, Final_Boss


global hp, hpmonster, playerdead, monsterdead, monster_name
hp_max = 200
hp = 200
exp = 0
niveau = 1
atk = 15
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
    global hp, hpmonster, playerdead, monsterdead, adversary
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

    elif hpmonster < 0:
        hpmonster = 0
        monsterdead = True

    return(hp, hpmonster, playerdead, monsterdead)


def attaquer(strike, strikemonster, atk, agi, agimonster, enemy):
    strike = attack(atk, agi, agimonster, strike)
    strikemonster = attackmonster(atkmonster, agi, agimonster, strikemonster)
    hp, hpmonster, playerdead, monsterdead = hpcount(
        strike, strikemonster, enemy)


def fight(enemy, strike, strikemonster, atk, agi, agimonster):
    global hp
    global hpmonster
    print("Vous faîtes face au", monster_name, "sauvage !")
    while hp > 0 and hpmonster > 0:
        print("PV du ", monster_name, "sauvage : ", hpmonster, "PV")
        print("Il vous reste actuellement", hp, "Points de vie.")
        title = f"Vous affrontez {monster_name} \n Que voulez-vous faire ?"
        options = ["attaquer", "inventaire", "fuir"]
        fight1, index = pick(options, title, indicator='=>', default_index=0)
        if fight1 == "attaquer" or index == 0:
            system("clear")
            attaquer(strike, strikemonster, atk, agi, agimonster, enemy)
        elif fight1 == "inventaire" or index == 1:
            # MANAGE INVENTORY
            fonction_inventory(inventaire, hp, hp_max)

            strikemonster = attackmonster(
                atkmonster, agi, agimonster, strikemonster)
            hp, hpmonster, playerdead, monsterdead = hpcount(
                strike, strikemonster, enemy)

            pass
        elif fight1 == "fuir" or index == 2:
            break


def exp_gain(hp_max, exp, niveau, atk, dfs, adversary):
    lvlgain = 100

    if adversary == foe:
        gain = randint(90, 100)
    elif adversary == Goblin:
        gain = randint(25, 45)
    elif adversary == Monster:
        gain = randint(100, 150)
    elif adversary == Boss1:
        gain = randint(55, 85)
    elif adversary == Boss2:
        gain = randint(150, 200)
    elif adversary == Final_Boss:
        gain = randint(200, 300)

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
    return hp_max, exp, niveau, atk, dfs


def encounter(y, x, adversary):
    global hp, hpmonster, playerdead, monsterdead, atkmonster, dfsmonster, agimonster, monster_name, atk, agi, dfs, exp, niveau, hp_max
    if adversary == foe:
        foes_name = ['Thierry Le Maignan', 'Sandie La Malice',
                     'Julien le rusé', 'Fabien le ténébreux', 'Baptiste le moine']
        monster_name = foes_name[randint(0, 4)]
        hpmonster = 50
        atkmonster = 10
        dfsmonster = 2
        agimonster = 5
        strikemonster = 1
        monsterdead = False

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
        atkmonster = 20
        dfsmonster = 10
        agimonster = 5
        strikemonster = 1
        monsterdead = False

    if adversary == Boss1:
        hpmonster = 250
        atkmonster = 15
        dfsmonster = 10
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        Boss1dead = False

        if Boss1dead == True:
            y == 13
            x == 0
            return y, x
    if adversary == Boss2:
        hpmonster = 500
        atkmonster = 20
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        Boss2dead = False

        if Boss2dead == True:
            y == 5
            x == 14
            return y, x
    if adversary == Final_Boss:
        hpmonster = 800
        atkmonster = 30
        dfsmonster = 15
        agimonster = 2
        strikemonster = 1
        monsterdead = False
        Boss3dead = False

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
                hp_max, exp, niveau, atk, dfs = exp_gain(
                    hp_max, exp, niveau, atk, dfs, adversary)

                print(f"Vous avez gagner {exp}xp")
                print(f"Vous êtes niveau {niveau}")

                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
            elif playerdead == True:
                system("clear")
                print("Vous avez été vaincu par le ",
                      monster_name, "sauvage !")
                print("Miskine")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
                return playerdead
        if choix == "fuir" or index == 0:
            break
        else:
            system("clear")
            title = "Vous allez quitter la combat !"
            options = ["Quitter"]
            choix, index = pick(
                options, title, indicator='=>', default_index=0)
            if choix == "Quitter":
                break
