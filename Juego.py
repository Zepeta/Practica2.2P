import pygame,sys
from Agente import Agente
from Mapa import Mapa
from Aestrella import Aestrella
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class Juego:
    def __init__(self):
        self.Mapa = Mapa()
        self.Agente = Agente()
        self.running = True
        self.WIDTH = 480
        self.HEIGHT = 505
        self.screen  = pygame.display.set_mode([self.WIDTH,self.HEIGHT])
        self.menu = True
        self.tipo_costos = []
        self.posicion_inicial = ()
        self.posicion_final = ()
        self.nodos_abiertos = []
        self.nodos_cerrados = []
        self.ruta_optima = []
    def mostrarInterfaz(self):
        pygame.init()
        pygame.display.set_caption("Práctica 3")        
        cont = 0
        imgI = None
        imgF = None
        self.screen.fill((255,255,255)) 
        lista_textos = []
        lista_rp = []
        while self.running:
            self.elegir_agente()
            self.screen.fill((169,169,169))
            self.Mapa.definirMapa(self.screen)
            letra = pygame.font.SysFont(None, 30)
            texto = letra.render("Comenzar", True, (0,0,0))
            self.screen.blit(texto,(10,485))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.posicion = pygame.mouse.get_pos()    
                    if self.posicion[1]//30==16:
                        if self.posicion[0]>=10 and self.posicion[0]<=109 and self.posicion[1]>=485 and self.posicion[1]<=505:
                            if self.posicion_inicial!=() and self.posicion_final!=():
                                a_estrella = Aestrella()
                                self.nodos_abiertos, self.nodos_cerrados, self.ruta_optima = a_estrella.a_estrella(self.posicion_inicial,self.posicion_final,self.tipo_costos)
                                # print("nodos_cerrados",self.nodos_cerrados)
                                # print("nodos_abiertos",self.nodos_abiertos)
                                self.ruta_optima.reverse()
                                print(self.ruta_optima)
                    else:
                        cont+=1 
                        if (self.posicion[0]//30)!=0 and (self.posicion[1]//30)!=0:           
                            if cont ==1:  
                                self.posicion = self.posicion[0]//30,self.posicion[1]//30
                                imgI,rectI = self.dibujar_posicion(self.posicion[0],self.posicion[1],"I")
                                self.posicion_inicial = self.posicion
                                self.mapear(self.posicion,cont) 
                            if cont==2:
                                self.posicion = self.posicion[0]//30,self.posicion[1]//30
                                imgF,rectF = self.dibujar_posicion(self.posicion[0],self.posicion[1],"F") #self.screen
                                self.posicion_final = self.posicion                                
                                self.mapear(self.posicion,cont)  
            if imgI != None:
                self.screen.blit(imgI,rectI)
            if imgF != None:
                self.screen.blit(imgF,rectF)
            if self.nodos_abiertos:
                nodo_abierto = self.nodos_abiertos.pop()
                img, rect = self.dibujar_posicion(nodo_abierto[0][0],nodo_abierto[0][1],"O("+str(nodo_abierto[1])+")")
                lista_textos.append((img,rect))
                if len(nodo_abierto)==2:
                    self.mapear(nodo_abierto[0],1)
                else:
                    self.mapear(nodo_abierto[2],1)
                pygame.time.delay(200)
            else:
                while self.ruta_optima:
                    nodo = self.ruta_optima.pop()
                    letra = pygame.font.SysFont(None, 19)
                    img = letra.render("X", True, (255,0,0))
                    rect = imgI.get_rect()
                    rect.x = nodo[0]*30+3
                    rect.y = nodo[1]*30+9
                    lista_rp.append((img,rect))
                for i in range(0,len(lista_rp)):
                    self.screen.blit(lista_rp[i][0],lista_rp[i][1])
            for i in range(0,len(lista_textos)):
                    self.screen.blit(lista_textos[i][0],lista_textos[i][1])
                
            pygame.display.flip()
           
    def dibujar_posicion(self,x,y,texto):
        letra = pygame.font.SysFont(None, 19)
        imgI = letra.render(texto, True, (0,0,0))
        rect = imgI.get_rect()
        rect.x = x*30+2
        rect.y = y*30+8
        return imgI, rect
        
    def mapear(self,posicion,cont):
        x = posicion[0]-1
        y = posicion[1]-1
        if cont==1:
            if x>-1 and y>-1:
                posicion_actual = self.Mapa.mapeo[y,x]
                self.Mapa.mapa[y,x] = posicion_actual
                if y>0:
                    arriba = self.Mapa.mapeo[y-1,x]
                    self.Mapa.mapa[y-1,x] = arriba
                if y<14:
                    abajo = self.Mapa.mapeo[y+1,x]
                    self.Mapa.mapa[y+1,x] = abajo
                if x>0:
                    izquierda = self.Mapa.mapeo[y,x-1]
                    self.Mapa.mapa[y,x-1] = izquierda
                if x<14:
                    derecha = self.Mapa.mapeo[y,x+1]
                    self.Mapa.mapa[y,x+1] = derecha
        if cont == 2:
            posicion_actual = self.Mapa.mapeo[y,x]
            self.Mapa.mapa[y,x] = posicion_actual
    
    def elegir_agente(self):
        while self.menu:
                letra = pygame.font.SysFont(None, 30)
                
                texto = letra.render("Elegir al agente", True, (0,0,0))
                self.screen.blit(texto,(160,40))

                texto_octopus = letra.render("Octopus", True, (0,0,0))
                self.screen.blit(texto_octopus,(160,100))
                
                texto_monkey = letra.render("Monkey", True, (0,0,0))
                self.screen.blit(texto_monkey,(160,160))
            
                for event in pygame.event.get(): 
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if pos[0]>=160 and pos[0]<=245 and pos[1]>=100 and pos[1]<=115:
                            self.tipo_costos = self.Agente.definir_agente("Octopus")
                            self.menu = False
                        if pos[0]>=160 and pos[0]<=235 and pos[1]>=159 and pos[1]<=175:
                            self.tipo_costos = self.Agente.definir_agente("Monkey")
                            self.menu = False
                    if event.type == QUIT:
                        self.running = False
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.running = False
                            sys.exit()
                pygame.display.update()
        
juego = Juego()
juego.mostrarInterfaz()


# pkg load signal
# b= [0.729441, -2.18832, 2.18832, -0.729441  ]
# a=[1, -2.37409, 1.92936, -0.532075]
# freqz(b, a)