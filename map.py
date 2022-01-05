from os import system
from random import randint
Player = "😎"
Final_Boss = "💀"
Boss1 = "🐲"
Boss2 = "🗡 "
Shop = "💰"
Shop1 = "💰"
Shop2 = "💰"
Master_Roshi = "👴"
Monster = "😡"
Goblin = "😈"
checkpoint = "⭐️"
trees = "🌲"
chain = "  "
cloud = " 🌥"
foe = 1
lvl = 1
# ---------------------------------------------------------------------


def Goblin_Movement(gobliny, goblinx):
    Index1 = randint(1, 3)
    Index2 = randint(1, 3)
    if Index1 == 1:
        if gobliny < 19:
            gobliny += 1
        else:
            pass
    if Index1 == 2:
        if gobliny > 16:
            gobliny -= 1
        else:
            pass
    if Index2 == 1:
        if goblinx < 12:
            goblinx += 1
        else:
            pass
    if Index2 == 2:
        if goblinx > 0:
            goblinx -= 1
        else:
            pass
    return gobliny, goblinx

# ---------------------------------------------------------------------


def Monster_Movement(monstery, monsterx):
    Index1 = randint(1, 3)
    Index2 = randint(1, 3)
    if Index1 == 1:
        if monstery < 12:
            monstery += 1
        else:
            pass
    if Index1 == 2:
        if monstery > 7:
            monstery -= 1
        else:
            pass
    if Index2 == 1:
        if monsterx < 13:
            monsterx += 1
        else:
            pass
    if Index2 == 2:
        if monsterx > 0:
            monsterx -= 1
        else:
            pass
    return monstery, monsterx

# ---------------------------------------------------------------------


def Monster_Encounter():
    Monster_Chance = randint(0, 50)
    return Monster_Chance

# ---------------------------------------------------------------------


def Player_Movement(Move, y, x):
    Move = Move.strip()
    system("clear")
    if Move == "z":
        if y != 0 or y != 15 or y != 7:
            y -= 1
        else:
            print("Vous ne pouvez pas aller en haut")
            pass

    if Move == "s":
        if y < 19 or y != 13 or y != 5:
            y += 1
        else:
            print("Vous ne pouvez pas aller en bas")
            pass

    if Move == "q":
        if x != 0:
            x -= 1
        else:
            print("Vous ne pouvez pas aller a gauche")
            pass

    if Move == "d":
        if x < 14:
            x += 1
        else:
            print("Vous ne pouvez pas aller a droite")
            pass
    return y, x

# ---------------------------------------------------------------------


def world_map(y, x, monstery, monsterx, gobliny, goblinx):
    i = 0
    p = 0
    World_Map = []
    Map = []
    for i in range(18):
        L = []
        L1 = []
        for p in range(15):
            L.append("|__|")
            p += 1
        i += 1
        Map.append(L)
        if i == 13 or i == 6:
            Map.append(L1)
    Map[y][x] = f"|{Player}|"

    Map[17][0] = f"|{cloud}|"
    Map[18][1] = f"|{cloud}|"
    Map[16][14] = f"|{cloud}|"
    Map[17][14] = f"|{cloud}|"
    Map[15][11] = f"|{cloud}|"
    Map[16][4] = f"|{cloud}|"
    Map[18][11] = f"|{cloud}|"
    Map[19][13] = f"|{cloud}|"
    Map[16][10] = f"|{cloud}|"
    Map[16][8] = f"|{cloud}|"
    Map[17][7] = f"|{cloud}|"
    Map[16][6] = f"|{cloud}|"
    Map[17][6] = f"|{cloud}|"

    Map[18][9] = f"|{trees}|"
    Map[19][6] = f"|{trees}|"
    Map[19][8] = f"|{trees}|"
    Map[13][0] = f"|{trees}|"
    Map[13][1] = f"|{trees}|"
    Map[13][4] = f"|{trees}|"
    Map[13][5] = f"|{trees}|"

    Map[11][8] = f"|{trees}|"
    Map[11][8] = f"|{trees}|"
    Map[12][7] = f"|{trees}|"
    Map[12][10] = f"|{trees}|"
    Map[12][14] = f"|{trees}|"
    Map[9][8] = f"|{trees}|"
    Map[9][6] = f"|{trees}|"
    Map[9][1] = f"|{trees}|"
    Map[7][0] = f"|{trees}|"
    Map[7][4] = f"|{trees}|"
    Map[7][9] = f"|{trees}|"
    Map[9][13] = f"|{trees}|"
    Map[10][12] = f"|{trees}|"
    Map[12][9] = f"|{trees}|"
    Map[10][3] = f"|{trees}|"

    Map[4][4] = f"|{chain}|"
    Map[5][5] = f"|{chain}|"
    Map[3][6] = f"|{chain}|"
    Map[4][13] = f"|{chain}|"
    Map[4][12] = f"|{chain}|"
    Map[5][9] = f"|{chain}|"
    Map[5][2] = f"|{chain}|"
    Map[4][4] = f"|{chain}|"
    Map[0][4] = f"|{chain}|"
    Map[0][5] = f"|{chain}|"
    Map[0][8] = f"|{chain}|"
    Map[4][4] = f"|{chain}|"
    Map[1][14] = f"|{chain}|"
    Map[3][1] = f"|{chain}|"
    Map[0][1] = f"|{chain}|"
    Map[2][11] = f"|{chain}|"
    Map[3][9] = f"|{chain}|"
    Map[3][8] = f"|{chain}|"
    Map[0][12] = f"|{chain}|"

    Map[16][13] = f"|{Shop}|"
    Map[13][3] = f"|{Shop1}|"
    Map[3][10] = f"|{Shop2}|"
    Map[15][0] = f"|{Boss1}|"
    Map[7][14] = f"|{Boss2}|"
    Map[0][0] = f"|{Final_Boss}|"
    Map[3][14] = f"|{Master_Roshi}|"
    Map[15][5] = f"|{checkpoint}|"
    Map[monstery][monsterx] = f"|{Monster}|"
    Map[gobliny][goblinx] = f"|{Goblin}|"

    a = 0
    for a in range(len(Map)):
        World_Map.append(Map[a])
        print(*World_Map[a])
        a += 1
    return Map


def LvlDesign(y, lvl):
    if y < 15:
        lvl = 2
        return lvl
    if y < 7:
        lvl = 3
        return lvl
    else:
        lvl = 1
        return lvl
