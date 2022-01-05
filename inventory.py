from pick import pick

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


def fonction_inventory(inventory, hp, hp_max, atk, hpmonster):
    L_objet_soin = ["Potion", "Potion +", "Potion X"]
    L_heal_value = [50, 70, 150]
    L_objet_arme = ["Bombe", "Explo-bombe"]
    L_arme_value = [80, 150]
    used = False
    title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \n Vous avez {hp}hp/{hp_max}hp"
    options = []
    for i in range(len(inventory)):
        options.append(inventory[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice != "quitter":
        i = objet_inventaire_verif(choice, inventory)
        if i == True:
            j = objet_soin_verif(choice, L_objet_soin)
            if j != "non":
                if hp == hp_max:
                    title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \nVous avez {hp}hp/{hp_max}hp \nVous ne pouvez pas utiliser cet item, vos hp sont déjà au maximum."
                    pass
                else:
                    print("Voulez-vous utiliser l'objet de soin '",
                          inventory[j], "' ?")
                    print("Vous avez", hp, "/", hp_max, "hp.")
                    print("cet objet heal",
                          L_heal_value[j], "hp, voulez-vous l'utiliser ?")
                    title2 = f"Voulez-vous utiliser l'objet de soin {inventory[j]} ?"
                    options2 = ["oui", "non"]
                    choice2, index = pick(
                        options2, title2, indicator='=>', default_index=0)
                    if choice2 == "oui":
                        hp_heal = L_heal_value[j]
                        hp += hp_heal
                        inventory.remove(choice)
                        options.remove(choice)
                        if hp_max < hp:
                            hp = hp_max
                        title = f"Choisissez un objet ou quittez l'inventaire en choisissant 'quitter': \nVous avez {hp}/{hp_max}hp \n-> {choice} utilisée"
                        used = True
                        return used, hp, hpmonster
                    else:
                        pass

            l = objet_arme_verif(choice, L_objet_arme)
            if l != "non":
                print("Vos dégâts sont de", atk, ".")
                title2 = f"Voulez utiliser l'objet {choice} qui infligera {L_arme_value[l]} dégats?"
                options2 = ["oui", "non"]
                choice_arme, index = pick(
                    options2, title2, indicator='=>', default_index=0)
                if choice_arme == "non":
                    pass
                if choice_arme == "oui":
                    hpmonster -= L_arme_value[l]
                    inventory.remove(choice)
                    options.remove(choice)
                    used = True
                    return used, hp, hpmonster

            if j == "non" and l == "non":
                print("Objet", choice, "non utilisable.")

        if used == True:
            break
        choice, index = pick(
            options, title, indicator='=>', default_index=0)
    return used, hp, hpmonster
