import pygame
import sys
from init import *
from constants import *




while True:
    #    The update() should be here  
    pygame.display.update()
    game_display.fill(purple_background)
    pygame.draw.rect(game_display,red,(200,200,50,50))
    pygame.draw.rect(game_display,green,(200,150,50,50))
    pygame.draw.rect(game_display,blue,(150,150,50,50))
    pygame.draw.rect(game_display,white,(150,200,50,50))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
           
            

           