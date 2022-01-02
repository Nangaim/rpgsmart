from pick import pick


def fonction_shop(inventaire, argent, liste_item, liste_prix):
    liste_item_etage1 = ["item1", "item2", "item3"]
    liste_prix_etage1 = [5, 10, 15]

    liste_item_etage2 = ["item4", "item5", "item6"]
    liste_prix_etage2 = [20, 25, 30]

    liste_item_etage3 = ["item7", "item8", "item9"]
    liste_prix_etage3 = [35, 40, 45]
    global result

    title = f"\n Bienvenue dans le shop, que souhaitez vous faire ? \n Vous avez {argent}€"
    print("inventaire:", inventaire)
    print("argent:", argent, "\n")
    options = ["Achetter", "Vendre", "Quitter"]

    choice_action, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice_action != "quitter" or index == 2:
        if choice_action == "acheter" or index == 0:
            result = fonction_achat(inventaire, argent, liste_item, liste_prix)
            # print("argent:", result[1], "€")
            title = f"\n Bienvenue dans le shop, que souhaitez vous faire ? \n Vous avez {result[1]}€"
            argent = result[1]
        elif choice_action == "vendre" or index == 1:
            result = fonction_vente(inventaire, argent, result[2])
            # print("argent:", result[1], "€")
            title = f"\n Bienvenue dans le shop, que souhaitez vous faire ? \n Vous avez {result[1]}€"
            argent = result[1]
        # else:
        #     print("Erreur, il faut choisir 'acheter', 'vendre' ou 'quitter'.")

        if choice_action == "quitter" or index == 2:
            break
        # inventaire = result[0]
        # argent = result[1]
        choice_action, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent


def verif_item(choice, liste):
    i = 0
    while i < len(liste):
        if choice == liste[i]:
            return i
        else:
            i += 1
    return "non"


def fonction_achat(inventaire, argent, liste_item, liste_prix):

    # print("\n Objets en vente:", liste_item)
    credit = []
    # print("Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :")
    title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' : \n Vous avez {argent}€"
    options = []
    for i in range(len(liste_item)):
        options.append(liste_item[i])
    options.append("quitter")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    # choice = input("--> ")
    while choice != "quitter":
        i = verif_item(choice, liste_item)
        if i != "non":
            if argent >= liste_prix[i]:
                # print(f"vous avez {argent} €.")
                # print(f"L'objet {liste_item[i]} coûte {liste_prix[i]} €")
                # print("voulez-vous l'acheter ?")
                title2 = f" vous avez {argent} €. \n L'objet {liste_item[i]} coûte {liste_prix[i]} € \n voulez-vous l'acheter ?"
                options2 = ["oui", "non"]
                choice2, index = pick(
                    options2, title2, indicator='=>', default_index=0)
                # while choice2 != "oui" and choice2 != "non":
                #     choice2 = input(
                #         "Erreur, il faut choisir 'oui' ou 'non': --> ")
                if choice2 == "oui":
                    # print("--> paiement effectué, merci de votre achat !")
                    inventaire.append(liste_item[i])
                    argent -= liste_prix[i]
                    credit.append(liste_prix[i])
                    title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :\n --> paiement effectué, merci de votre achat ! \n Vous avez {argent}€"
                if choice2 == "non":
                    pass
            else:
                # print("Vous avez", argent, "€.")
                # print("L'objet", liste_item[i], "coûte", liste_prix[i], "€.")
                # print("Vous n'avez pas assez d'argent pour acheter cet objet.")
                title = f"Choisissez l'objet que vous souhaitez acheter ou quittez le mode achat en choisissant 'quitter' :\n Vous avez {argent}€ \n L'objet {liste_item[i]} coûte {liste_prix[i]} € \n Vous n'avez pas assez d'argent pour acheter cet objet."
        # else:
        #     print("Erreur, l'item '", choice, "' n'est pas en vente ici.")

        # print("\n Choisissez un autre objet a acheter ou quitter le mode achat :")
        # print("inventaire :", inventaire)
        # print("argent :", argent, "€")
        # print("objets en vente:", liste_item)
        # choice = input("--> ")
        choice, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent, credit


def fonction_vente(inventaire, argent, credit):
    # print("\n Vous avez", argent, "€.")
    # print("Voici votre inventaire :")
    # print(inventaire)
    # print("quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente:")
    title = f"quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente: \n Vous avez {argent}€"
    options = []
    for i in range(len(inventaire)):
        options.append(inventaire[i])
    options.append("quitter")
    # choice = input("--> ")
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    while choice != "quitter":
        i = verif_item(choice, inventaire)
        if i != "non":
            title2 = "êtes-vous sûre de vouloir vendre cet objet, oui ou non ?"
            options2 = ["oui", "non"]
            choice_answer, index = pick(
                options2, title2, indicator='=>', default_index=0)
            # while choice_answer != "Oui" and choice_answer != "Non":
            #     choice_answer = input(
            #         "Erreur, il faut choisir 'oui' ou 'non': --> ")
            if choice_answer == "oui":
                argent += credit[i]
                credit.remove(credit[i])
                inventaire.remove(inventaire[i])
                options.remove(options[i])
                # print("Votre inventaire:", inventaire)
                # print("Vous avez", argent, "€.")
                title = f"quel objet souhaitez-vous vendre ? Choisissez 'quitter' pour quitter le mode vente: \n Vous avez {argent}€"
            if choice_answer == "non":
                pass
        # else:
        #     print("L'item '", choice, "' ne fait pas partie de votre inventaire.")

        # print("\n Souhaitez-vous vendre un autre objet ou quitter le mode vente:")
        # print("inventaire :", inventaire)
        # print("argent :", argent, "€")
        # choice = input("--> ")
        choice, index = pick(
            options, title, indicator='=>', default_index=0)

    return inventaire, argent
