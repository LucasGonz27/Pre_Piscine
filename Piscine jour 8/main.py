import pygame

# Initialiser
pygame.init()

# Position initiale du personnage
x, y = 300, 300

def perso(x, y):
    # la tete
    pygame.draw.circle(fenetre, 'black', (x, y), 25)

    # l'oeil gauche
    pygame.draw.circle(fenetre, 'pink', (x-8, y-5), 3)

    # l'oeil droit
    pygame.draw.circle(fenetre, 'pink', (x+9, y-5), 3)

    # la bouche
    pygame.draw.line(fenetre, 'red', (x, y+5), (x+10, y+5), 5)

    # le corps
    pygame.draw.line(fenetre, 'red', (x, y+24), (x, y+200), 40)

    # jambe gauche
    pygame.draw.line(fenetre, 'black', (x-10, y+200), (x-50, y+250), 20)

    # jambe droite
    pygame.draw.line(fenetre, 'black', (x+15, y+200), (x+50, y+250), 20)

    # bras gauche
    pygame.draw.line(fenetre, 'black', (x-25, y+60), (x-30, y+130), 10)

    # bras droit
    pygame.draw.line(fenetre, 'black', (x+25, y+60), (x+35, y+130), 10)

# Créer la fenêtre
fenetre = pygame.display.set_mode((600, 600))
background = pygame.image.load("caste.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
            if event.key == pygame.K_ESCAPE:
                running = False

    # Afficher l'image de fond
    fenetre.blit(background, (0, 0))
    perso(x, y)
    pygame.display.flip()

pygame.quit()
