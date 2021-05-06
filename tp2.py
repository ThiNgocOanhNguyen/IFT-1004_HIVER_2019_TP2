import random

def lire_tous_mots():
    """
    Cette fonction va lire le document tous_mots.txt et en
    extraire la liste des mots potentiels pour le jeu de bonhomme
    pendu.

    Notez que les différents mots sont séparés par un caractère de
    retour de fin de ligne "\n". Vous devez seulement retourner les
    mots, sans ces caractères dans votre liste de tous les mots.

    Returns: 
        tous_mots, la liste de tous les mots sans les "\n". La
        longueur totale de la liste obtenue par len(tous_mots)
        devrait être 13879.

    Example:
        Si le fichier tous_mots.txt était seulement 

            kayak
            maison
            animal
        
        la liste retournée par cette fonction devrait être

            ["kayak", "maison", "animal"]
    """


    with open('tous_mots.txt') as fichier_tous_mots:
        liste_tous_mots = fichier_tous_mots.read().splitlines()

    return liste_tous_mots
    # liste = []
    #
    # with open("tous_mots.txt") as fichier:
    #
    #     for line in fichier:
    #         liste.append(line.strip())
    #     return liste
        # print(liste)

    # fichier.close()

def jouer_bonhomme_pendu(liste_tous_mots):
    """
    Cette fonction représente la boucle principale de jeu, qui va
    perpétuellement demander au joueur s'il désire jouer une
    manche et faire tous les appels nécessaires au début d'une
    manche. 

    La première étape de l'initialisation d'une manche, la pige
    aléatoire d'un mot, vous est founie. Vous devez toutefois
    implémenter vous-même le code des deux autres fonctions.
    Référez vous aux commentaires des fonctions respectives pour
    les détails.
    
    Cette fonction vous est fournie, vous NE DEVEZ PAS la
    modifier.
    """
    print("Bienvenue dans le jeu de Bonhomme Pendu.\n")

    while joueur_veut_jouer_manche():
        mot_choisi = piger_mot_dans_liste(liste_tous_mots)
        lettres_dans_mot = obtenir_lettres_mot(mot_choisi)
        dict_mot_choisi = creer_dict_mot(mot_choisi, lettres_dans_mot)

        jouer_manche(dict_mot_choisi, len(mot_choisi))

    print("Au revoir !")

def joueur_veut_jouer_manche():
    """
    Cette fonction demande au joueur s'il désire jouer une
    manche. La fonction retourne True si le joueur entre le
    caractère 'o' et False s'il entre n'importe quel autre
    caractère.
    
    Returns:
        True si le joueur entre 'o', False sinon.
    """

    reponse = input("Désirez-vous jouer une manche?\nEntrez 'o' pour jouer, " \
                    "ou n'importe quel autre caractère pour quitter: ")

    return reponse == 'o'

def piger_mot_dans_liste(liste_tous_mots):
    """
    Cette fonction va sélectionner au hasard un mot parmi la
    liste de mots passée en paramètre. 

    Cette fonction vous est fournie, vous NE DEVEZ PAS la
    modifier.
    
    Args: 
        liste_tous_mots: une liste de chaînes de caractères contenant 
            tous les mots pouvant potentiellement être retournés.

    Returns:
        Un mot aléatoire de liste_tous_mots
    """
    mot_choisi = random.choice(liste_tous_mots)

    # Cette ligne est là pour vous aider à déboguer votre
    # programme en sachant quel est le mot caché. Vous pouvez
    # l'enlever si vous voulez.
    print("Le mot choisi aléatoirement est {}".format(mot_choisi))

    return mot_choisi

def obtenir_lettres_mot(mot):
    """
    Cette fonction va extraire la liste de toutes les lettres
    présentes au moins une fois dans le mot en paramètre.

    Pour ce faire, il est possible de travailler avec une liste
    des lettres uniques du mot, initialement vide. On parcourt
    ensuite les caractères du mot passé en paramètre et, si la
    lettre actuelle n'est pas déjà présente dans notre liste de
    lettres uniques, on l'ajoute.

    Args: 
        mot: une chaîne de caractères du mot duquel on veut connaître
            la liste de lettres uniques

    Returns: 
        Une liste de caractères uniques représentant les
        lettres uniques du mot.

        Par exemple, si le mot est "arbre", la fonction doit 
        retourner la liste ["a", "r", "b", "e"].

        Si le mot est "maison", la liste est ["m", "a", "i", "s", "o", "n"].
    """

    # liste_un_mot = []
    # count = {}
    # for i in mot:
    #     if i in count:
    #         count[i] += 1
    #     else:
    #         count[i] = 1
    # for i in sorted(count, key=count.get, reverse=False):
    #     liste_un_mot.append(i)
    # return (liste_un_mot)

    lettres_mot = []

    for lettre in mot:
        if lettre not in lettres_mot:
            lettres_mot.append(lettre)

    return lettres_mot




def creer_dict_mot(mot, lettres):
    """
    Cette fonction va obtenir la représentation en dictionaire
    d'un mot à partir de sa liste de lettres uniques. Le
    dictionaire aura comme clés les différentes lettres uniques
    et les valeurs associées seront les index où la lettre se
    retrouve dans le mot ainsi qu'un booléen (initialisé à
    False), indiquant si la lettre clé a été trouvée par le
    joueur. Un exemple de dictionaire est présenté plus bas.

    Pour obtenir la représentation en dictionaire, une façon
    simple de procéder est de commencer par initialiser un
    dictionaire vide. On parcourt ensuite la liste des lettres
    uniques une lettre à la fois. Pour la lettre actuellement
    utilisée dans la boucle, on initialise l'entrée du
    dictionaire avec la lettre courante comme clé. On parcourt
    ensuite le mot une lettre à la fois et on ajoute les index où
    la lettre du mot est la même que la lettre courante à
    l'entrée correspondante dans le dictionaire du mot.

    Args: 
        mot : un string mot pour lequel on veut obtenir une
            représentation en dictionaire

        lettres : la liste des lettres uniques présentes dans le mot

    Returns: 
        Une représentation en dictionaire du mot en entrée.
        Pour le dictionaire, les clés sont des caractères
        représentant chacune des lettres uniques du mot. La
        valeur associée à une lettre est une liste de 2 éléments:
        une liste d'entiers représentant les index du mot où on
        retrouve la lettre clé et un booléen représentant si le
        joueur a deviné la lettre clé.

        Par exemple, pour le mot "arbre" et la liste ["a", "r", "b", "e"], 
        le dictionaire retourné serait

            {"a": [[0], False],
             "r": [[1, 3], False],
             "b": [[2], False],
             "e": [[4], False]}
        
        Remarquez particulièrement que les booléens sont initialisés à 
        False pour toutes les lettres. Aussi, même si une lettre n'est 
        présente qu'une seule fois dans le mot, on utilise quand même 
        une liste pour représenter tous les index où la lettre est 
        présente.
    """
    dictionnaire_mot = {}

    for lettre in lettres:
        dictionnaire_mot[lettre] = [[], False]

    for index_lettre, lettre in enumerate(mot):
        dictionnaire_mot[lettre][0].append(index_lettre)

    return dictionnaire_mot


def jouer_manche(dict_mot_choisi, taille_mot):
    """
    Cette fonction représente la boucle de jeu principale d'une
    manche.
    
    Cette fonction vous est fournie, vous NE DEVEZ PAS la
    modifier.
    
    Parmi toutes les fonctions appelées par cette fonction,
    seulement afficher_etat_manche() vous est fournie, vous devez
    implémenter les autres selon les détails présentés dans les
    commentaires de chacune d'entre elles.

    Args:
        dict_mot_choisi : la représentation en dictionaire du mot
            choisi

        taille_mot : la longueur du mot choisi
    """
    n_prises = 0
    lettres_tentees = []
    max_prises = 10

    while not manche_terminee(dict_mot_choisi, n_prises, max_prises, taille_mot):
        afficher_etat_manche(dict_mot_choisi, n_prises, max_prises, taille_mot)
        
        lettre_tentee = demander_lettre_joueur(lettres_tentees)
        lettres_tentees.append(lettre_tentee)

        n_prises = mise_a_jour_manche(lettre_tentee, dict_mot_choisi, n_prises)

def afficher_etat_manche(dict_mot, n_prises, max_prises, taille_mot):
    """
    Cette fonction vient afficher différentes données sur l'état
    de la manche courante; le nombre actuel de prises, le nombre
    de prises maximum et l'état du mot à deviner.

    Cette fonction vous est fournie, vous NE DEVEZ PAS la
    modifier. 

    Args:
        dict_mot : La représentation en dictionaire du mot à
            deviner
        
        n_prises : Le nombre actuel de prises

        max_prises : Le nombre maximum de prises

        taille_mot : La taille du mot à deviner
    """
    print("\nVoici l'état actuel de la manche.")
    print("Vous avez présentement {} prises sur une possibilité de {}.".format(n_prises, max_prises))
    print("L'état du mot à deviner est ")
    afficher_mot_formatte(dict_mot, taille_mot)

def manche_terminee(dict_mot, n_prises, max_prises, taille_mot):
    """
    Cette fonction va venir vérifier si la manche actuelle est
    terminée. Une manche peut être terminée pour deux raisons :

        1) Toutes les lettres ont été découvertes par le joueur. 
            Selon notre implémentation, cela revient à dire que,
            dans la représentation en dictionaire du mot, le booléen
            représentant la découverte de la lettre par l'usager est
            à True, pour toutes les lettres clé du dictionaire.

        2) Le joueur a excédé le nombre maximal de prises.

    Pour chacun des deux cas, un message approprié est affiché.
    Si la partie est terminée par victoire du joueur (cas 1),
    alors on félicite le joueur et on affiche le mot à deviner
    avec afficher_mot_formatte(). Si la partie est terminée par
    une défaite (cas 2), on indique le nombre maximal de prises
    qui a été atteint.

    Args:
        dict_mot : La représentation en dictionaire du mot
            recherché
        n_prises : Le nombre actuel de prises du joueur

        max_prises : Le nombre maximal de prises que le joueur 
            peut atteindre
        
        taille_mot : La taille du mot recherché

    Returns:
        True, si la manche est terminée pour une des deux raisons
            énoncées plus haut, False sinon
    """



    if all([v[1] for v in dict_mot.values()]):
        print("Félicitations vous avez trouvé le mot caché ! " + \
              "Il s'agissait de :")
        afficher_mot_formatte(dict_mot, taille_mot)
        return True
    if n_prises >= 10:
        print("Malheureusement vous avez atteint le nombre maximal de {} prises !".format(max_prises) + \
              " Meilleure chance la prochaine fois.\n")
        return True

    return False



def afficher_mot_formatte(dict_mot, taille_mot):
    """
    Cette fonction va afficher une représentation formattée du
    mot à deviner dans le terminal. Les lettres devinées seront
    affichées alors que celles qui restent inconnues seront
    représentées par un '-'.

    Cette fonction vous est fournie, vous NE DEVEZ PAS la
    modifier.
    
    Args:
        dict_mot : La représentation en dictionaire du mot à
            deviner
        
        taille_mot : La taille du mot à deviner
    """
    mot_formatte = ['-'] * taille_mot

    for lettre, valeur in dict_mot.items():
        if valeur[1]:
            for idx in valeur[0]:
                mot_formatte[idx] = lettre

    print()
    print(*mot_formatte, sep="")
    print()

def demander_lettre_joueur(lettres_tentees):
    """
    Cette fonction va demander au joueur quelle lettre il
    souhaite tenter pour son prochain coup. Cette fonction sera
    essentiellement une boucle, qui va commencer par afficher les
    lettres déjà tentées et ensuite demander à l'utilisateur
    quelle est la prochaine lettre qu'il souhaite tenter.

    Tant que la lettre tentée est déjà contenue dans la liste des
    lettres tentées, on affiche un message d'erreur au joueur et
    on retourne dans la boucle.

    ***Notez ici que vous n'avez pas à ajouter la lettre tentée
        par le joueur à la liste de lettres tentées mais
        seulement retourner la lettre tentée. C'est la fonction
        jouer_manche() qui s'occupe d'ajouter la lettre à liste.***

    Args:
        lettres_tentees : Une liste de toutes les lettres tentées
            jusqu'à présent.

    Returns :
        La lettre choisie par le joueur
    """
    while True:
        if len(lettres_tentees) > 0:
            print("Voici les lettres deja tentees: ")
            print(*lettres_tentees, sep=", ")

        lettre_tentee = input("Veillez entrer une lettre: ")

        if lettre_tentee in lettres_tentees:
            print("La lettre est deja tentee, entre une autre:")
        else:
            return lettre_tentee




def mise_a_jour_manche(lettre_tentee, dict_mot_choisi, n_prises):
    """
    Cette fonction va effectuer la mise à jour des différents
    composants de la manche en fonction de la lettre tentée par
    le joueur. La fonction retourne aussi le nombre de prises
    mis à jour.

    Deux cas peuvent survenir :

        1) Si la lettre tentée est une des clés du dictionaire du 
            mot choisi, alors on doit mettre à jour l'attribut 
            booléen correspondant à lettre pour True, indiquant
            que l'utilisateur a réussi à deviner la lettre.

        2) Sinon, on incrémente le nombre de prises de 1.

    Dans les deux cas, on souhaite aussi afficher un message
    approprié à l'utilisateur pour lui indiquer le résultat de
    son coup. Par exemple, "Bien joué !" pour un bon coup et
    "Dommage !" pour un mauvais.

    Args:
        lettre_tentee : la lettre tentée par le joueur

        dict_mot_choisi : la représentation en dictionaire du mot

        n_prises : le nombre de prises du joueur avant la mise à jour
        
    Returns:
        n_prises : le nombre de prises après la mise à jour
    """
    if lettre_tentee in dict_mot_choisi.keys():

        dict_mot_choisi[lettre_tentee][1] == True
        print("Bien joué !")
    else:
        n_prises+=1
        print("Domage!")
    return n_prises


def tests_fonctions():
    """
    Cette fonction vous permet de tester votre implémentation des
    fonctions obtenir_lettres_mot() et creer_dict_mot(). 

    Les tests utilisent un instruction spéciale nommée assert, dont
    vous avez seulement besoin de savoir qu'elle vérifie si une
    condition est vérifiée, et affiche un message d'erreur en cas
    d'échec. La syntaxe de cette fonction est 

    assert <condition>, <message_erreur>

    ***Notez que les tests faits ici ne garantissent pas que vos
    fonctions sont parfaites, mais ils sont un bon indicateur
    que vous êtes sur la bonne voie ! ***
    """
    test_obtenir_lettres_mot()
            
    test_creer_dict_mot()

def test_obtenir_lettres_mot():
    """
    Pour tester l'égalité entre deux listes sans vérifier
    l'ordre, nous validons d'abord qu'elles ont la même taille et
    que tous les éléments d'une liste sont présents dans l'autre.
    """
    mot_test = "arbre"

    lettres_uniques_test = obtenir_lettres_mot(mot_test)
    lettres_uniques_test_attendues = ["a", "r", "b", "e"]

    assert len(lettres_uniques_test_attendues) == len(lettres_uniques_test), \
            "La taille de la liste de lettres retournées ({}) n'est pas la même ".format(len(lettres_uniques_test)) \
            + "que celle de la liste attendue ({})".format(len(lettres_uniques_test_attendues))
            
    for lettre_attendue in lettres_uniques_test_attendues:
        assert lettre_attendue in lettres_uniques_test, \
            "La lettre attendue {} ne se trouve pas dans la liste retournée !".format(lettre_attendue)
            
def test_creer_dict_mot():
    """
    Pour tester l'égalité entre deux dictionaires, on valide que
    les dictionaires ont le même nombre de clés, et que les clés
    et les valeurs correspondent.
    """
    mot_test = "arbre"
    lettres = ["a", "r", "b", "e"]

    dict_mot_test = creer_dict_mot(mot_test, lettres)
    dict_mot_test_attendu = {"a": [[0], False],
                             "r": [[1, 3], False],
                             "b": [[2], False],
                             "e": [[4], False]}

    assert len(dict_mot_test_attendu.keys()) == len(dict_mot_test.keys()), \
            "Le dictionaire retourné et le dictionaire attendu n'ont pas le même nombre de clés !"
            
    for cle_attendue, valeur_attendue in dict_mot_test_attendu.items():
        assert cle_attendue in dict_mot_test, \
            "Une lettre clé attendue n'était pas présente dans le dictionaire retourné !"

        valeur_retournee = dict_mot_test[cle_attendue]
        assert valeur_attendue == valeur_retournee, \
            "La valeur retournée pour la clé"


if __name__ == "__main__":
    liste_tous_mots = lire_tous_mots()
    # ob = obtenir_lettres_mot("vernir")
    # print(ob)
    # creer = creer_dict_mot("vernir",['v', 'e', 'r', 'n', 'i'] )
    # print(creer)

    jouer_bonhomme_pendu(liste_tous_mots)


