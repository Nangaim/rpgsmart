import sys
from time import sleep
from pick import pick
import pickle


def save(x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe):
    title = "Voulez vous: "
    options = ["Sauvegarder et quitter", "Quitter sans sauvegarder"]
    choice, index = pick(options, title, indicator='=>', default_index=0)
    sleep(1)
    variables = 0

    if index == 0:
        saveName = input("Donnez un nom a votre sauvegarde : ")
        with open(f'{saveName}.dat', 'wb') as f:
            pickle.dump([x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead,
                        Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe], f, protocol=2)
        sys.exit()

    elif index == 1:
        sys.exit()


def load(partie):
    with open(f'{partie}.dat', 'rb') as f:
        x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe = pickle.load(
            f)
    return x, y, gobliny, goblinx, monstery, monsterx, monsterdead, Boss1dead, Boss2dead, master_dead, Final_Bossdead, visited, inventaire, hp, hp_max, exp, niveau, lvlgain, dfs, argent, lvl, foe
