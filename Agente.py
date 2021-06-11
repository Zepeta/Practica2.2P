import pygame
class Agente():
    def __init__(self):
        self.agente = pygame.Surface((20,20))
        self.mov_agente = self.agente.get_rect()
        self.mov_agente.x =-30
        self.mov_agente.y =-30
        self.tipo_agente = []
        self.posicion_actual = ()
        self.costos = {
            "Monkey":[
                (0,None),
                (1,2),
                (2,4),
                (3,3),
                (4,1)
            ],
            "Octopus":[
                (0,None),
                (1,2),
                (2,1),
                (3,None),
                (4,3)
            ]
        }
    def definir_agente(self,agente):
        self.tipo_agente = self.costos[agente]
        return self.tipo_agente
        
        #self.agente.fill((255,255,255))
    def definir_posicion_final(self,x,y):
        if (x//30)!=0 and (y//30)!=0:
            letra = pygame.font.SysFont(None, 30)
            imgF = letra.render("F", True, (255,255,255))
            rect = imgF.get_rect()
            rect.x = (x//30)*30+13
            rect.y = (y//30)*30+5
            return imgF,rect

    # def mover_agente(self,tecla_presionada,WIDTH,HEIGHT):
    #     if tecla_presionada[K_UP]:
    #         self.mov_agente.move_ip(0,-30)
    #     if tecla_presionada[K_DOWN]:
    #         self.mov_agente.move_ip(0, 30)
    #     if tecla_presionada[K_LEFT]:
    #         self.mov_agente.move_ip(-30, 0)
    #     if tecla_presionada[K_RIGHT]:
    #         self.mov_agente.move_ip(30, 0)    
        
    #     if self.mov_agente.left < 30:
    #         self.mov_agente.left = 30
    #     if self.mov_agente.right > WIDTH:
    #         self.mov_agente.right = WIDTH
    #     if self.mov_agente.top <= 30:
    #         self.mov_agente.top = 30
    #     if self.mov_agente.bottom >= HEIGHT:
    #         self.mov_agente.bottom = HEIGHT
            
        
        