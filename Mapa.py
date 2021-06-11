import numpy as np
import pygame


doc = open("doc2.txt","r").read()
filas = doc.split("\n")
row = len(filas)
col = len(filas[0].split(","))
lista = []
for fila in filas:
    aux = fila.split(",")
    for car in aux:
        lista.append(int(car))
mapeo = np.array(lista).reshape(row,col)

mapa = np.full((row,col),5)

class Mapa:
    def __init__(self):
        self.mapa = mapa
        self.mapeo = mapeo
        self.filas = row
        self.columnas = col
        self.montania = pygame.Surface((30,30))
        self.tierra = pygame.Surface((30,30))
        self.agua = pygame.Surface((30,30))
        self.arena = pygame.Surface((30,30))
        self.bosque = pygame.Surface((30,30))
        self.negro = pygame.Surface((30,30))
        self.colores = {
            "montania" : (105,105,105),
            "tierra" : (255, 188, 145),
            "agua" : ( 0, 84, 255),
            "arena" : ( 255, 197, 0),
            "bosque" : (29, 220, 32),
            "negro" : (0,0,0)
        }
    def definirMapa(self, screen):
        self.montania.fill(self.colores.get("montania"))
        self.tierra.fill(self.colores.get("tierra"))
        self.agua.fill(self.colores.get("agua"))
        self.arena.fill(self.colores.get("arena"))
        self.bosque.fill(self.colores.get("bosque"))
        self.negro.fill(self.colores.get("negro"))
        for i in range(self.filas):
            letra = pygame.font.SysFont(None, 30)
            img = letra.render(str(i+1), True, (0,0,0))
            screen.blit(img, (5, i*30+38))
            screen.blit(img, (i*30+38, 5))
            for j in range(self.columnas):
                if self.mapa[i,j] == 0:
                    screen.blit(self.montania,(j*30+30,i*30+30))             
                elif self.mapa[i,j] == 1:
                    screen.blit(self.tierra,(j*30+30,i*30+30))
                elif self.mapa[i,j] == 2:
                    screen.blit(self.agua,(j*30+30,i*30+30))             
                elif self.mapa[i,j] == 3:
                    screen.blit(self.arena,(j*30+30,i*30+30))             
                elif self.mapa[i,j] == 4:
                    screen.blit(self.bosque,(j*30+30,i*30+30))             
                elif self.mapa[i,j] == 5:
                    screen.blit(self.negro,(j*30+30,i*30+30))             
                pygame.draw.line(screen,(0,0,0),(0,j*30+30),(480,j*30+30))
                pygame.draw.line(screen,(0,0,0),(j*30+30,0),(j*30+30,480))
        pygame.draw.line(screen,(0,0,0),(0,480),(480,480))
