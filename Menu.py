from time import sleep
import sys
from pick import pick
# from RPGSmart import Main


def main_menu():

    # print(" ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░")
    # sleep(2)
    # print(" 1. Nouvelle partie \n 2. Charger une partie \n 3. Règles \n 4. Credits \n 5. Quitter")
    title = " ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░"
    sleep(2)
    options = ["Nouvelle partie", "Charger une partie",
               "Règles", "Credits", "quitter"]
    # choice = int(input())
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    if index == 0:
        print("Le jeu va commencer ! \n")
        sleep(1)
        create_character()
        input("\nAppuyez sur Entrer pour continuer")
        game_start()
        input("\nAppuyez sur Entrer pour continuer")
        zone1()
        input("\nAppuyez sur Entrer pour continuer")
        # rune()
        Main()

    elif index == 1:
        print("Quelle partie souhaitez-vous charger? (filename)")

    elif index == 2:
        print("\n Règles : \n \n Le jeu prendra place dans la première des trois zones de l'univers. \n Il s'agit d'un tour par tour classique dans lequel vous devrez vous confronter à différents monstres dans le but de vous frayer \n un chemin jusqu'à l'antagoniste. \n \n Avant d'y parvenir, vous trouverez sur votre route différents objets et personnages qui vous aideront à poursuivre votre quête. \n  \n Bon courage, aventurier!")
        sleep(15)
        main_menu()

    elif index == 3:
        print("Credits : Jeu créé par Baptiste Verdier , Fabien Renoir , Julien Rion , Sandie Ouallet et Thierry Maignan.")
        sleep(10)
        main_menu()

    elif index == 4:
        sys.exit()

    return index


def create_character():
    global player_name
    print("Bienvenue aventurier, comment vous appelez-vous?\n")
    player_name = input()
    print("\nFort bien", player_name,
          ", que les cieux vous donnent la force de faire face à votre destin...")
    return player_name


def script(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == ".":
            sleep(0.5)
        else:
            sleep(0.04)


def shopkeeper1():

    script("\nBonjour, je suis un modeste marchand égaré. Si vous veniez à m'acheter quoi que ce soit, cela pourrait probablement m'aider à repartir... Ce coin est trop étrange pour moi.\n \n Bienvenue.\n")


def shopkeeper2():

    script("\nAh, vous revoilà... J'ai bien peur que s'enfoncer dans cet endroit ne soit pas le meilleur moyen pour tenter de m'extraire de mes problèmes. Malheureusement, je n'ai pas vu une quelconque autre sortie dans les parages...\n \nQue puis-je faire pour vous?\n")


def shopkeeper3():

    script("\nBonjour, jeune aventurier. Je me rends compte que vous êtes probablement ma meilleure chance de partir d'ici. Je compte sur vous.\n \nDites-moi comment je peux vous aider.\n")


def game_start():

    script("\nVous vous réveillez dans un paysage inconnu. Un visage étranger vous demande : \n \n - Vous allez bien ? Ca fait un moment que vous êtes là. \n \nConscient de la nature étrange de la situation, vous frottez vos paupières pour découvrir la lumière blafarde du paysage vous entourant, qui se trouve être une brume épaisse. \n \nVous cherchez autour de vous, mais impossible de retrouver la personne qui vous parlait. \n \nCe paysage inhabituel vous intrigue et quelque chose semble briller au loin... \n \nEt si vous alliez y jeter un coup d'oeil?\n")


def zone1():

    script("\nVous vous approchez de la lueur suspecte en vous enfonçant dans l'épaisse brume, et celle-ci se ternit au fur et à mesure que vous avancez. \nVous vous baissez pour voir de quoi il s'agit...\n \nVous voilà l'heureux propriétaire d'une potion!\n \nEn vous relevant, vous constatez que la brume est désormais presque palpable et vous empêche de voir même à moyenne distance. \n \nFrayez-vous un chemin pour en apprendre plus sur cet endroit.\n")
    #potion : +1


def zone2():

    script("\nAprès cette dure épreuve, vous voyez le paysage en face de vous se dégager. Toujours à la recherche de l'homme qui vous a parlé plus tôt, la brume laisse petit à petit place aux arbres. Poursuivez votre chemin, et vos questions trouveront éventuellement des réponses...\n")


def zone3():

    script("\nVous vous frayez un chemin en laissant derrière vous la dépouille de l’atroce bête.\n \nEn avançant, vous avez l'impression d'apercevoir au loin une silhouette humaine voire amicale...\n \nSerait-ce enfin là la personne que vous recherchiez?\n")


def scriptroshi1():

    script("\nVous êtes donc parvenu jusqu'ici, félicitations. Vous méritez des explications sur ce qui vous arrive et je m'excuse de ne pas vous en avoir offert plus tôt. Cependant, il en va de ma responsabilité de ne pas vous laisser aller plus loin...\n \nCe qui se cache là-bas n'est en rien comparable avec ce que vous avez connu auparavant.\n \nRevenez me voir lorsque vous serez plus fort.\n")


def scriptroshi2():

    script(
        f"\nVous revoilà...\n \nJe préfèrerais directement vous sommer de mettre un terme à votre entreprise.\n \nMalheureusement, je connais la soif inextinguible de l'esprit et la faiblesse de l'Homme. Si je ne vous arrêterai pas, je souhaiterais au moins m'assurer que vous avez les épaules assez larges pour faire face à ce qui vous attend..\n \nEn garde,nangaim, prouvez-moi votre valeur!")


def scriptroshi3():

    script(
        f"\nAlors c'est ainsi...\n \nVous dépassez de loin tout ce que j'ai pu imaginer. J'ai été victime de mon ignorance alors même que je souhaitais vous protéger du haut de mon illusoire sagesse, quelle arrogance, quelle ironie!\n \nnangaim,vous avez toutes mes excuses et ma sympathie. Je vous en prie, prenez ceci...\n \n - Vous avez obtenu l'Epée légendaire.\n \nCela devrait vous permettre de voir le bout de cet affreux rêve. Allez la ou je n'ai jamais pu, brisez le sort... Bon courage.\n")


def finalboss3():
    # drop a 50% HP, phase 2?
    script("\nTu te débrouilles bien pour un cafard, mais personne ne sortira jamais d'ici. Nous avons assez joué. Ta stupide épée ne te mènera nulle part. Tu vas retrouver le sommeil pour l'éternité.\n")


def finalboss4():

    script("\nTout ça à cause d'une misérable épée... Tu peux brûler en enfer misérable insecte... J'irai même jusque là-bas pour te retrouver.\n \n Le jour ou je te mettrai à nouveau la main dessus, tu auras l'impression que ce que tu as vécu aujourd'hui n’était qu’un doux rêve à côté...\n")


def rune():

    title = script("Dans votre malheur, vous vous voyez offert une bénédiction qui affectera votre personnage jusqu'à la fin du jeu.\n Veuillez choisir une rune parmi les quatre ci-dessous\n")
    # script("\n Veuillez choisir une rune parmi les quatre ci-dessous\n")
    # script("\n1. - Triomphe : Vous regagnez des HP après chaque combat\n")
    # script("2. - Violence : Vous frappez en premier et votre première attaque est un coup critique")
    # script("3. - Assiduité : Vous gagnez plus d'XP après chaque combat")
    # script("4. - Prospection : Vous gagnez plus d'or après chaque combat")
    options = ["1. - Triomphe : Vous regagnez des HP après chaque combat", "2. - Violence : Vous frappez en premier et votre première attaque est un coup critique",
               "3. - Assiduité : Vous gagnez plus d'XP après chaque combat", "4. - Prospection : Vous gagnez plus d'or après chaque combat"]
    choice, index = pick(
        options, title, indicator='=>', default_index=0)

    # Collecter le code de verdier
    if index == 0:
        rune_choice = "triomphe"
    elif index == 1:
        rune_choice = "violence"
    elif index == 2:
        rune_choice = "assiduite"
    elif index == 3:
        rune_choice = "prospection"
    return rune_choice
