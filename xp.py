#truc de flemmard pour pas avoir à type "\"
def enter():
    print("\n")

#player stats
global lvl,xp,xpneeded,hpmax,atk,dfs,agi,monsterlvl
lvl = 5
xp = 0
xpneeded = 10
hpmax = 200
hp = 200
atk = 15
dfs = 5
agi = 5
monsterlvl = 5

def xpfight():
    global xp,lvl,monsterlvl
    ratio = monsterlvl//lvl
    gain = 10*ratio
    print("Vous avez gagné ", gain, "Points d'expérience.")
    xp = xp + gain
    return xp

def lvlup():
    global lvl,xpneeded,hpmax,atk,dfs,agi
    lvl = lvl + 1
    xpneeded = xpneeded + 5
    print("Vous êtes maintenant niveau", lvl, " ! ")
    hpmax = hpmax + 20
    atk = atk + 5
    dfs = dfs + 2
    agi = agi + 2
    print("Vous sentez votre corps se renforcer et vos capacités s'améliorent")
    enter()
    print("Points d'expérience supplémentaires nécessaire pour atteindre le prochain niveau : ")
    print(xpneeded - xp)

def islvlup():
    global xp,xpneeded
    if xp >= xpneeded:
        xp = xp - xpneeded
        print("Vous avez gagné un niveau d'expérience ! ")
        lvlup()
    else:
        print("Vous avez actuellement ", xp, "Points d'expérience")
        enter()
        print("Points d'expérience supplémentaires requis pour passer au niveau suivant : ")
        print(xpneeded - xp)
        enter()

def statslvl():
    xpfight()
    islvlup()