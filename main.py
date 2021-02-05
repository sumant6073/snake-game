import pygame

#Initializing the game
x = pygame.init()

#Display
gameWindow = pygame.display.set_mode((1200, 500))
#Caption set display
pygame.display.set_caption("Snake game ")

# Game specific variables
exit_game = False
game_over = False

#Creating a gameloop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")



pygame.quit()
quit()