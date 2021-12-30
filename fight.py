import random
from time import sleep
from os import system
from pick import pick

Monster_list = ["Thierry Le Maignan", "Fabien le ténébreux",
                "Julien l'audacieux", "Sandie la malice", "Baptiste l'imprimeur"]
global hp, hpmonster, playerdead, monsterdead
hp = 200
atk = 15
dfs = 5
agi = 5
strike = 1
playerdead = False

# ici fabien j'ai du corriger son code car il arrive pas a me faire un menu de combat en 4 jours
# Trigger : définir l'ennemi
# Choice : faire face ou fuir
# attack et attackmonster: define le coup du joueur (ou du monstre) quand il attaque (+ coups critiques)
# hpcount : calcul des hp restant + qui frappe en premier
# attaquer : séquence entière des 3 fonctions nommées au dessus
# fight : tout l'ensemble du fight et ses choix (inventory etc)
# encounter : trigger fight si le joueur choisit de se battre


def enter():
    print("\n")


def trigger():
    enemy = Monster_list[random.randint(0, 4)]
    print("Vous rencontrez un", enemy, "sauvage 🙀!")
    sleep(0.5)
    Clear = input("Press Enter to continue")
    if Clear == "":
        system("cls")
    return enemy


def attack(atk, agi, agimonster, strike):
    chancecrit = random.randint(0, 10)
    if chancecrit <= agi:
        crit = 1
    else:
        crit = 0
    randhit = 1
    if crit == 1:
        strike = (atk*2)*randhit
    else:
        strike = atk*randhit
    dodgechance = random.randint(1, 20)
    if dodgechance <= agimonster:
        strike = 0
        print("Vous n'êtes pas assez rapide et manquez votre attaque ! ")
        sleep(2)
    else:
        strike = strike
    return strike


def attackmonster(atkmonster, agi, agimonster, strikemonster):
    chancecrit = random.randint(0, 10)
    if chancecrit <= agimonster:
        crit = 1
    else:
        crit = 0
    randhit = 1
    if crit == 1:
        strikemonster = (atkmonster*2)*randhit
    else:
        strikemonster = atkmonster*randhit
    dodgechance = random.randint(1, 20)
    if dodgechance <= agi:
        strikemonster = 0
        print("Vous êtes assez rapide et esquivez l'attaque de peu")
        sleep(0.5)
        system("clear")
    else:
        strikemonster = strikemonster
    return strikemonster


def hpcount(strike, strikemonster, enemy):
    global hp, hpmonster, playerdead, monsterdead
    if hp > 0 and hpmonster > 0:
        if agi >= agimonster:
            armormonster = dfsmonster
            strike = strike - armormonster
            if strike < 0:
                strike = 0
            hpmonster = hpmonster - strike
            print("Vous avez infligé", strike,
                  "Pts de dégâts au", enemy, " ! ")
            sleep(0.5)
            armor = dfs
            strikemonster = strikemonster - armor
            if strikemonster < 0:
                strikemonster = 0
            hp = hp - strikemonster
            print("Le", enemy, "Vous a infligé",
                  strikemonster, "Pts de dégats ! ")
            sleep(0.5)
        else:
            armor = dfs
            strikemonster = strikemonster - armor
            if strikemonster < 0:
                strikemonster = 0
            hp = hp - strikemonster
            print("Le", enemy, "Vous a infligé",
                  strikemonster, "Pts de dégats ! ")
            sleep(0.5)
            armormonster = dfsmonster
            strike = strike - armormonster
            if strike < 0:
                strike = 0
            hpmonster = hpmonster - strike
            print("Vous avez infligé", strike,
                  "Pts de dégâts au", enemy, " ! ")
            sleep(0.5)
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
    print("Vous faîtes face au", enemy, "sauvage !")
    while hp > 0 and hpmonster > 0:
        print("PV du ", enemy, "sauvage : ", hpmonster, "PV")
        enter()
        print("Il vous reste actuellement", hp, "Points de vie.")
        enter()
        title = "Que voulez-vous faire ?"
        options = ["attaquer", "inventaire", "fuir"]
        fight1, index = pick(options, title, indicator='=>', default_index=0)
        if fight1 == "attaquer" or index == 0:
            system("clear")
            attaquer(strike, strikemonster, atk, agi, agimonster, enemy)
        elif fight1 == "inventaire" or index == 1:
            # MANAGE INVENTORY

            pass
        elif fight1 == "fuir" or index == 2:
            break


def encounter():
    enemy = trigger()
    title = "Que voulez-vous faire ?"
    options = ["Fuir", "Attaquer"]
    choix, index = pick(options, title, indicator='=>', default_index=0)

    global hp, hpmonster, playerdead, monsterdead, atkmonster, dfsmonster, agimonster
    hpmonster = 50
    atkmonster = 10
    dfsmonster = 2
    agimonster = 5
    strikemonster = 1
    monsterdead = False

    # choix = (input("Que faire? "))
    system("clear")
    choix = choix.strip()
    while playerdead != True or monsterdead != True:
        if choix == "attaquer" or index == 1:
            fight(enemy, strike, strikemonster, atk, agi, agimonster)
            if monsterdead == True:
                print("Vous avez vaincu le", enemy, "sauvage !")
                enter()
                print("Il vous reste", hp, "Points de vie")
                enter()
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
            elif playerdead == True:
                print("Vous avez été vaincu par le ", enemy, "sauvage !")
                enter()
                print("Miskine")
                waiting = input("Press Enter to continue")
                if waiting == "":
                    system("clear")
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
