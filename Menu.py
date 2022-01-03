from time import sleep
import sys
from pick import pick
from RPGSmart import Main

def main_menu():

    # print(" ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░")
    # sleep(2)
    # print(" 1. Nouvelle partie \n 2. Charger une partie \n 3. Règles \n 4. Credits \n 5. Quitter")
    title = " ▄▄▄       ███▄ ▄███▓ ███▄    █ ▓█████   ██████  ██▓ ▄▄▄      \n▒████▄    ▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒████▄    \n▒██  ▀█▄  ▓██    ▓██░▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒▒██  ▀█▄  \n░██▄▄▄▄██ ▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░░██▄▄▄▄██ \n ▓█   ▓██▒▒██▒   ░██▒▒██░   ▓██░░▒████▒▒██████▒▒░██░ ▓█   ▓██▒\n ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░\n▒   ▒▒ ░░  ░      ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░\n ░   ▒   ░      ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░  ░   ▒   \n░  ░       ░            ░    ░  ░      ░   ░        ░  ░"
    sleep(2)
    options = ["Nouvelle partie", "Charger une partie", "Règles", "Credits", "quitter"]
    # choice = int(input())
    choice, index = pick(
        options, title, indicator='=>', default_index=0)
    if index == 0 :
        print("Le jeu va commencer ! \n")
        sleep(1)
        create_character()
        input("\nAppuyez sur Entrer pour continuer")
        game_start()
        input("\nAppuyez sur Entrer pour continuer")
        zone1()
        input("\nAppuyez sur Entrer pour continuer")
        rune()
        sleep(10)
        Main()


    elif index == 1 : 
        print("Quelle partie souhaitez-vous charger? (filename)")
        

    elif index == 2 : 
        print("\n Règles : \n \n Le jeu prendra place dans la première des trois zones de l'univers. \n Il s'agit d'un tour par tour classique dans lequel vous devrez vous confronter à différents monstres dans le but de vous frayer \n un chemin jusqu'à l'antagoniste. \n \n Avant d'y parvenir, vous trouverez sur votre route différents objets et personnages qui vous aideront à poursuivre votre quête. \n  \n Bon courage, aventurier!")
        sleep(15)
        main_menu()

    elif index == 3 :
        print("Credits : Jeu créé par Baptiste Verdier , Fabien Renoir , Julien Rion , Sandie Ouallet et Thierry Maignan.")
        sleep(10)
        main_menu()

    elif index == 4 :
        sys.exit()
        

    return index

def create_character():

    print("Bienvenue aventurier, comment vous appelez-vous?\n")
    player_name = input()
    print("\nFort bien",player_name,", que les cieux vous donnent la force de faire face à votre destin..." )
    return player_name


def script(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == ".":
            sleep(0.5)
        else:
            sleep(0.04)
    
def game_start():

    script("\nVous vous réveillez dans un paysage inconnu. Un visage étranger vous demande : \n \n - Vous allez bien ? Ca fait un moment que vous êtes là. \n \nConscient de la nature étrange de la situation, vous frottez vos paupières pour découvrir la lumière blafarde du paysage vous entourant, qui se trouve être une brume épaisse. \n \nVous cherchez autour de vous, mais impossible de retrouver la personne qui vous parlait. \n \nCe paysage inhabituel vous intrigue et quelque chose semble briller au loin... \n \nEt si vous alliez y jeter un coup d'oeil?\n")


def zone1():

    script("\nVous vous approchez de la lueur suspecte en vous enfonçant dans l'épaisse brume, et celle-ci se ternit au fur et à mesure que vous avancez. \nVous vous baissez pour voir de quoi il s'agit...\n \nVous voilà l'heureux propriétaire d'une potion!\n \nEn vous relevant, vous constatez que la brume est désormais presque palpable et vous empêche de voir même à moyenne distance. \n \nFrayez-vous un chemin pour en apprendre plus sur cet endroit.\n")
    #potion : +1

def zone2():

    script("\nAprès cette dure épreuve, vous voyez le paysage en face de vous se dégager. Toujours à la recherche de l'homme qui vous a parlé plus tôt, la brume laisse petit à petit place aux arbres. Poursuivez votre chemin, et vos questions trouveront éventuellement des réponses...\n")

def rune():

    title = script("Dans votre malheur, vous vous voyez offert une bénédiction qui affectera votre personnage jusqu'à la fin du jeu.\n Veuillez choisir une rune parmi les quatre ci-dessous\n")
    # script("\n Veuillez choisir une rune parmi les quatre ci-dessous\n")
    # script("\n1. - Triomphe : Vous regagnez des HP après chaque combat\n")
    # script("2. - Violence : Vous frappez en premier et votre première attaque est un coup critique")
    # script("3. - Assiduité : Vous gagnez plus d'XP après chaque combat")
    # script("4. - Prospection : Vous gagnez plus d'or après chaque combat")
    options = ["1. - Triomphe : Vous regagnez des HP après chaque combat", "2. - Violence : Vous frappez en premier et votre première attaque est un coup critique", "3. - Assiduité : Vous gagnez plus d'XP après chaque combat", "4. - Prospection : Vous gagnez plus d'or après chaque combat"]
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


main_menu()

    




