import pygame
import math

pygame.init()

WITDH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WITDH, HEIGHT))
pygame.display.set_caption("Solar System")


def main():
    run = True
    
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()
    
    
main()
