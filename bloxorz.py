# Définitit la taille du plateau
hauteur, largeur = 10, 10
plateau = [[' ']*largeur for _ in range(hauteur)]

# position du bloc et de la cible
bloc_x1, bloc_x2, bloc_y1, bloc_y2 = 0, 1, 0, 0
cible_x1, cible_x2, cible_y1, cible_y2 = 9, 9, 9, 8
plateau[bloc_y1][bloc_x1] = plateau[bloc_y2][bloc_x2] = 'B'
plateau[cible_y1][cible_x1] = plateau[cible_y2][cible_x2] = 'C'

def afficher_plateau():
    for ligne in plateau:
        print(' '.join(ligne))
        
def verifier_victoire():
    if (bloc_x1 == cible_x1 and bloc_x2 == cible_x2 and bloc_y1 == cible_y1 and bloc_y2 == cible_y2) or \
       (bloc_x1 == cible_x2 and bloc_x2 == cible_x1 and bloc_y1 == cible_y2 and bloc_y2 == cible_y1):
        print("gagné")
        return True
    return False

while True:
    afficher_plateau()
    mouvement = input("Déplace le bloc (g pour gauche, d pour droite, h pour haut, b pour bas, t pour tourner): ").lower()
    
    if mouvement == 'g':
        if bloc_x1 > 0 and bloc_x2 > 0:
            plateau[bloc_y1][bloc_x1] = plateau[bloc_y2][bloc_x2] = ' '
            bloc_x1 -= 1
            bloc_x2 -= 1
    elif mouvement == 'd':
        if bloc_x1 < largeur - 1 and bloc_x2 < largeur - 1:
            plateau[bloc_y1][bloc_x1] = plateau[bloc_y2][bloc_x2] = ' '
            bloc_x1 += 1
            bloc_x2 += 1
    elif mouvement == 'h':
        if bloc_y1 > 0 and bloc_y2 > 0:
            plateau[bloc_y1][bloc_x1] = plateau[bloc_y2][bloc_x2] = ' '
            bloc_y1 -= 1
            bloc_y2 -= 1
    elif mouvement == 'b':
        if bloc_y1 < hauteur - 1 and bloc_y2 < hauteur - 1 and plateau[bloc_y1+1][bloc_x1] == ' ' and plateau[bloc_y1+1][bloc_x2] == ' ':
            plateau[bloc_y1][bloc_x1] = plateau[bloc_y2][bloc_x2] = ' '
            bloc_y1 += 1
        bloc_y2 += 1
    elif mouvement == 't':
        if bloc_x1 == bloc_x2:
            if plateau[bloc_y1+1][bloc_x1] == ' ':
                plateau[bloc_y1][bloc_x1] = ' '
                plateau[bloc_y2][bloc_x2] = ' '
                bloc_x2 += 1
                bloc_y2 -= 1
            else:
                plateau[bloc_y1][bloc_x1] = ' '
                plateau[bloc_y2][bloc_x2] = ' '
                bloc_x2 -= 1
                bloc_y2 += 1
        plateau[bloc_y1][bloc_x1] = 'B'
        plateau[bloc_y2][bloc_x2] = 'B'
        
    assert 0 <= bloc_x1 < largeur and 0 <= bloc_x2 < largeur and 0 <= bloc_y1 < hauteur and 0 <= bloc_y2 < hauteur, "Le bloc est hors du plateau."
    
    if verifier_victoire():
        break
