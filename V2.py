import pygame
import sys

# Définit la taille du plateau et la taille d'une case
hauteur, largeur = 10, 10
taille_case = 40

# Couleurs
couleur_fond = (255, 255, 255)
couleur_bloc = (255, 0, 0)
couleur_cible = (0, 0, 0)
couleur_grille = (200, 200, 200)
couleur_parcours = (195, 165, 140)

parcours = [(0,0),(1,0),(2,0),(3,0),(2,1),(2,2),(2,3),(3,3),(4,3),(3,2),(3,4),(3,5),(3,6),(3,7),(4,6),(2,6),(1,6),(0,6),(0,7),(0,8),(1,8),(0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9)]

# Position initiale du bloc et de la cible
bloc_x1, bloc_x2, bloc_y1, bloc_y2 = 0, 1, 0, 0
cible_x1, cible_x2, cible_y1, cible_y2 = 8, 9, 9, 9


pygame.init()


fenetre = pygame.display.set_mode((largeur * taille_case, hauteur * taille_case))
pygame.display.set_caption("Jeu Bloxorz")

orientation_horizontale = True

compteur_mouvements = 0

def dessiner_plateau():
    fenetre.fill(couleur_fond)
    for y in range(hauteur):
        for x in range(largeur):
            pygame.draw.rect(fenetre, couleur_bloc, (x * taille_case, y * taille_case, taille_case, taille_case), 1)
    pygame.draw.rect(fenetre, couleur_cible, (cible_x1 * taille_case, cible_y1 * taille_case, taille_case, taille_case))
    pygame.draw.rect(fenetre, couleur_cible, (cible_x2 * taille_case, cible_y2 * taille_case, taille_case, taille_case))
    
    for case_x, case_y in parcours:
        pygame.draw.rect(fenetre, couleur_parcours, (case_x * taille_case, case_y * taille_case, taille_case, taille_case))
    
    if orientation_horizontale:
        pygame.draw.rect(fenetre, couleur_bloc, (bloc_x1 * taille_case, bloc_y1 * taille_case, taille_case, taille_case))
        pygame.draw.rect(fenetre, couleur_bloc, (bloc_x2 * taille_case, bloc_y2 * taille_case, taille_case, taille_case))
    else:
        pygame.draw.rect(fenetre, couleur_bloc, (bloc_x1 * taille_case, bloc_y1 * taille_case, taille_case, taille_case * 2))
    
    # Dessine la grille
    for y in range(1, hauteur):
        pygame.draw.line(fenetre, couleur_grille, (0, y * taille_case), (largeur * taille_case, y * taille_case), 1)
    for x in range(1, largeur):
        pygame.draw.line(fenetre, couleur_grille, (x * taille_case, 0), (x * taille_case, hauteur * taille_case), 1)

def verifier_victoire():
    if (bloc_x1 == cible_x1 and bloc_x2 == cible_x2 and bloc_y1 == cible_y1 and bloc_y2 == cible_y2) or \
       (bloc_x1 == cible_x2 and bloc_x2 == cible_x1 and bloc_y1 == cible_y2 and bloc_y2 == cible_y1):
        print("Gagné en", compteur_mouvements, "mouvements.")
        return True
    return False

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # raccourcis clavier
            if event.key == pygame.K_LEFT:
                if bloc_x1 > 0 and bloc_x2 > 0:
                    bloc_x1 -= 1
                    bloc_x2 -= 1
                    compteur_mouvements += 1
            elif event.key == pygame.K_RIGHT:
                if bloc_x1 < largeur - 1 and bloc_x2 < largeur - 1:
                    bloc_x1 += 1
                    bloc_x2 += 1
                    compteur_mouvements += 1
            elif event.key == pygame.K_UP:
                if bloc_y1 > 0 and bloc_y2 > 0:
                    bloc_y1 -= 1
                    bloc_y2 -= 1
                    compteur_mouvements += 1
            elif event.key == pygame.K_DOWN:
                if bloc_y1 < hauteur - 1 and bloc_y2 < hauteur - 1:
                    bloc_y1 += 1
                    bloc_y2 += 1
                    compteur_mouvements += 1
            elif event.key == pygame.K_SPACE:
                orientation_horizontale = not orientation_horizontale

    dessiner_plateau()
    if not verifier_victoire():
        print(compteur_mouvements)
    elif verifier_victoire():
        sys.stdout.flush()  # Force l'affichage immédiat du message

    pygame.display.update()
