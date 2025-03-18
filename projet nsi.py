
#Jeux de morpion (tic tac toe)
#par Pablo Faivre et Flavio Spedicato


#introduire le jeux
def introduction():
    """introduire le jeux"""
    print('bienvenue dans notre jeu de morpion. Il y a deux joueurs X et O')
    print('la premiere personne qui aligne 3 symboles gagne, soit en colonne, en ligne ou en diagonale')
    print('quand vous decidez de valider votre tour ou votre symbole, appuyez sur entrée')
    input('appuyez entrée après avoir lu les règles dans la console')

#on va creer l'interface
def interface():
    """renvoie le plateaux de jeux"""
    plateaux= [[" "," "," "],
               [" "," "," "],
               [" "," "," "]]
    return plateaux

def beaux_plateaux(plateaux):
    """la fonction change linterface du plateaux"""
    ligne = len(plateaux)
    colonne = len(plateaux)
    print("+---+---+---+")
    for i in range(ligne):
        print("|",plateaux[i][0], "|", plateaux[i][1], "|", plateaux[i][2],"|")
        print("+---+---+---+")
    input('voici votre plateau, appuyez entrée')
    return plateaux

# quel joueur joue quel signe
def joueur():
    """sert a deffinir le joueur 1 et 2 et quel signe ils ont"""
    symbole_1 = input('joueur 1, veux tu ètre X ou O ?' )
    if symbole_1 == 'X' or 'x':
        symbole_2 = 'O'
        print('joueur 1 vous etes X; joueur 2 vous ètes O')
    else:
        symbole_1 = 'O'
        symbole_2 = 'X'
        print('joueur 1 vous etes O; joueur 2 vous ètes X')
    return(symbole_1, symbole_2)

#La fonction qui commence le jeux
def commencer_jeux(plateaux, symbole_1, symbole_2, compteur):
    """commence le jeux et les tours regarde aussi si c'est possible de mettre le pion a cet endroit"""
    #demare le jeux
    if compteur % 2 == 0:
         joueur = symbole_2
    elif compteur % 2 == 1:
        joueur = symbole_1
    print("c'est aux tour du joueur",joueur)
    ligne = int(input("choisis une ligne (horizontal): premiere case = 0 || la deuxieme = 1 || la troisieme = 2 "))
    colonne = int(input("choisis une colonne (vertical): premiere case = 0 || la deuxieme = 1 || la troisieme = 2"))

    #regarde si la case existe
    while (ligne > 2 or ligne < 0) or (colonne > 2 or colonne < 0):
        input("Cette case n'existe pas, rejouez apres avoir appuyé sur entrée")
        ligne = int(input("choisis une ligne (horizontal): premiere case = 0 || la deuxieme = 1 || la troisieme = 2 "))
        colonne = int(input("choisis une colonne (vertical): premiere case = 0 || la deuxieme = 1 || la troisieme = 2"))

    # regarder si la case est prise
    while (plateaux[ligne][colonne] == symbole_1)or (plateaux[ligne][colonne] == symbole_2):
        input("La Case a été prise par l'autre joueur, appuyez sur entrée pour rejouer")
        ligne = int(input("choisis une ligne (horizontal): premiere case = 0 || la deuxieme = 1 || la troisieme = 2 "))
        colonne = int(input("choisis une colonne (vertical): premiere case = 0 || la deuxieme = 1 || la troisieme = 2"))

    # met le x ou le o sur le plateaux
    if joueur == symbole_1:
        plateaux[ligne][colonne] = symbole_1

    else:
        plateaux[ligne][colonne] = symbole_2

    return (plateaux)

def est_plein(plateaux, symbole_1, symbole_2,joueur):
    """regarde si il y a une une égalité, et donc si le plateaux est plein"""
    compteur = 1
    gagnant = True
# regarde si le plateux est plein et si il n'y a pas encore de gagnant
    while compteur < 10 and gagnant == True:
        jeux = commencer_jeux(plateaux, symbole_1, symbole_2, compteur)
        beaux = beaux_plateaux(plateaux)
        gagnant = est_gagnant(plateaux, symbole_1, symbole_2, compteur)

        # regarde si il y a une egalite ou un gagnant et termine la partie
        if compteur == 9 and gagnant == True:
            print ('Fin de Jeu')
            print("Dommage il y a une égalité")
        if gagnant == False:
            print("Fin de Jeu")
        compteur += 1

def est_gagnant(plateaux, symbole_1, symbole_2, compteur):
    """déffinit et regarde si il y a un gagnant"""
    gagnant = True
    #regarde les lignes si il y a un gagnant
    for ligne in range(0,3):
        if (plateaux[ligne][0]==plateaux[ligne][1]==plateaux[ligne][2]==symbole_1):
            gagnant = False
            print('Le Gagnant est le', symbole_1,'Bien Joué')
        elif (plateaux[ligne][0]==plateaux[ligne][1]==plateaux[ligne][2]==symbole_2):
            gagnant = False
            print('Le Gagnant est le',symbole_2,'Bien Joué')
    #regarde les colonnes si il y a un gagnant
    for colonne in range(0,3):
        if (plateaux[0][colonne]==plateaux[1][colonne]==plateaux[2][colonne]==symbole_1):
            gagnant = False
            print('Le Gagnant est le', symbole_1,'Bien Joué')
        elif (plateaux[0][colonne]==plateaux[1][colonne]==plateaux[2][colonne]==symbole_2):
            gagnant = False
            print('Le Gagnant est le',symbole_2,'Bien Joué')
    #regarde les diagonales si il y a un gagnant
    if (plateaux[0][0]==plateaux[1][1]==plateaux[2][2]==symbole_1):
            gagnant = False
            print('Le Gagnant est le', symbole_1,'Bien Joué')
    elif (plateaux[0][0]==plateaux[1][1]==plateaux[2][2]==symbole_2):
            gagnant = False
            print('Le Gagnant est le' ,symbole_2,'Bien Joué')
    if (plateaux[0][2]==plateaux[1][1]==plateaux[2][0]==symbole_1):
            gagnant = False
            print('Le Gagnant est le' ,symbole_1,'Bien Joué')
    elif (plateaux[0][2]==plateaux[1][1]==plateaux[2][0]==symbole_2):
            gagnant = False
            print('Le Gagnant est le',symbole_2,'Bien Joué')
    return gagnant

def main():
    #fonction main
    intro = introduction()
    plateaux = interface()
    beaux = beaux_plateaux(plateaux)
    symbole_1, symbole_2 = joueur()
    plein = est_plein(plateaux, symbole_1, symbole_2, joueur)
main()