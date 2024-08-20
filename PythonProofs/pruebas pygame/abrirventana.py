import pygame,sys

pygame.init()

size=(800,500)

#abrir ventana
screen=pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pass

