from pick import pick
# inventory = ["item_soin_basique", "item_1",
#              "item_soin2", "item_armure1", "item_4", "item_arme1"]


# exemple de liste pour les stats :
# stats = ["Nom", 25, 50, 5, "item_armure_basique",
#          10, 5, "item_arme_basique", 15, 10, 1, 0]
# 0-Nom, 1-HP, 2-HP max,
# 3-Armure de base par lvl, 4-Armure utilisée, 5- Armure réelle,
# 6-dégâts de base par lvl, 7-arme utilisée, 8-dégat réels,
# 9-agilité, 10-level, 11-xp

inventaire = []


def objet_soin_verif(choice, L_objet_soin):
    j = 0
    while j < len(L_objet_soin):
        if choice == L_objet_soin[j]:
            return j
        else:
            j += 1
    return "non"


def objet_armure_verif(choice, L_objet_armure):
    k = 0
    while k < len(L_objet_armure):
        if choice == L_objet_armure[k]:
            return k
        else:
            k += 1
    return "non"


def objet_arme_verif(choice, L_objet_arme):
    l = 0
    while l < len(L_objet_arme):
        if choice == L_objet_arme[l]:
            return l
        else:
            l += 1
    return "non"


def objet_inventaire_verif(choice, inventory):
    i = 0
    while i < len(inventory):
        if choice == inventory[i]:
            return True
        else:
            i += 1
    return False


def fonction_inventory(inventory, hp, hp_max):
    L_objet_soin = ["Potion"]
    L_heal_value = [20]
    # L_objet_armure = ["plaque du mort", "warmog"]
    L_armor_value = [20, 30]
    L_objet_arme = ["master sword"]
    L_arme_value = [20]
    # print("Vous êtes dans votre inventaire, vous pouvez utiliser des soins, changer d'armure ou changer d'arme.\n")
    # print("Inventaire :", inventory, "\n")
    # print("Choisissez un objet ou quittez l'inventaire en choisissant 'quitter':")
    title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \n Vous avez {hp}hp/{hp_max}hp"
    options = []
    for i in range(len(inventory)):
        options.append(inventory[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    # choice = input("--> ")
    while choice != "quitter":
        i = objet_inventaire_verif(choice, inventory)
        if i == True:
            j = objet_soin_verif(choice, L_objet_soin)
            if j != "non":
                if hp == hp_max:
                    # print(
                    #     "Vous ne pouvez pas utiliser cet item, vos hp sont déjà au maximum.")
                    title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \n Vous avez {hp}hp/{hp_max}hp \n Vous ne pouvez pas utiliser cet item, vos hp sont déjà au maximum."
                    pass
                else:
                    print("Voulez-vous utiliser l'objet de soin '",
                          inventory[j], "' ?")
                    print("Vous avez", hp, "hp sur", hp_max, "hp max.")
                    print("cet objet heal",
                          L_heal_value[j], "hp, êtes-vous sure ?")
                    title2 = f"Voulez-vous utiliser l'objet de soin {inventory[j]} ?"
                    options2 = ["oui", "non"]
                    choice2, index = pick(
                        options2, title2, indicator='=>', default_index=0)
                    # choice2 = input("oui ou non ? ")
                    if choice2 == "oui":
                        hp_heal = L_heal_value[j]
                        hp += hp_heal
                        inventory.remove(choice)
                        options.remove(choice)
                        if hp_max < hp:
                            hp = hp_max
                        # print(f"-> {choice} utilisé")
                        title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \n Vous avez {hp}hp/{hp_max}hp \n  -> {choice} utilisé"
                    else:
                        pass
            # k = objet_armure_verif(choice, L_objet_armure)
            # if k != "non":
            #     print("Votre bouclier est de", stats[5], ".")
            #     print(
            #         "L'objet '", stats[4], "' est actuellement équipé et vous protège de", stats[5]-stats[3], ".")
            #     print("voulez vous le changer par l'objet '", choice,
            #           "' qui vous donnera un bouclier de", L_armor_value[k]+stats[3], "?")
            #     choice_armor = input("oui ou non ? ")
            #     while choice_armor != "oui" and choice_armor != "non":
            #         print("veuillez choisir oui ou non.")
            #         choice_armor = input()
            #     if choice_armor == "non":
            #         pass
            #     if choice_armor == "oui":
            #         stats[5] = stats[3]
            #         inventory.append(stats[4])
            #         stats[4] = choice
            #         stats[5] += L_armor_value[k]
            #         inventory.remove(choice)

            # l = objet_arme_verif(choice, L_objet_arme)
            # if l != "non":
            #     print("Vos dégâts sont de", stats[8], ".")
            #     print("L'arme actuellement utilisée est '",
            #           stats[7], "'qui fait", stats[8]-stats[6], "de dégâts.")
            #     print("voulez vous la changer par l'objet '", choice,
            #           "' qui rendra vos dégâts à", L_arme_value[l]+stats[6], "?")
            #     choice_arme = input("oui ou non ? ")
            #     while choice_arme != "oui" and choice_arme != "non":
            #         print("veuillez choisir oui ou non.")
            #         choice_arme = input()
            #     if choice_arme == "non":
            #         pass
            #     if choice_arme == "oui":
            #         stats[8] = stats[6]
            #         inventory.append(stats[7])
            #         stats[7] = choice
            #         stats[8] += L_arme_value[l]
            #         inventory.remove(choice)

            if j == "non":
                print("objet", choice, "non utilisable.")

        # if i == False:
        #     print("Cet objet n'est pas dans votre inventaire, vérifier l'ortographe.")

        # print(" ")
        # print("HP :", hp, "/", 200)
        # print("Inventaire :", inventory, "\n")
        # print("Choisissez un objet ou quittez l'inventaire en choisissant 'quitter':")
        choice, index = pick(
            options, title, indicator='=>', default_index=0)
        # choice = input("--> ")


# fonction_inventory(inventaire, hp)

# print("\nArmure équipée :", stats[4])
# print("Arme utilisée :", stats[7])
# print("HP :", "\033[32m", stats[1], "\033[0m")
# print("Inventaire :", inventory, "\n")
