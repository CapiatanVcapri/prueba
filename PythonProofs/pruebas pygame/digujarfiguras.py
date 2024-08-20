import pygame,sys
pygame.init()
#colores en rgb
negro =(0,0,0)
blanco =(255,255,255)
verde=(0,255,0)
rojo=(255,0,0)
azul=(0,0,255)


size=(800,500)

#abrir ventana
screen=pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(blanco)
    #----------------
    pygame.draw.line(screen,verde,[0,100],[100,500],5)
    #----------------
    pygame.display.flip()#actualizar pantalla