import pyxel
import random
import math


#modos do inimigo

INVISIVEL = 0
VIVO = 1
MORTO = 2

#modos de jogo

INICIO = 0
ATIRANDO = 1
INIMIGO_MORTO = 2
GAME_OVER = 3

raio_do_heroi = 8

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bola:
    def __init__(self):
        self.pos = Vetor(0,0)
        self.size = 2
        self.speed = 3
        self.color = pyxel.frame_count % 16

    def update(self, x, y, size, color):
        self.pos.x = x
        self.pos.y = y
        
class Inimigo:
    olho = (16,0)
    boca = (32,0)
    nota = (40, 0)

    def __init__(self, larg_mundo, alt_mundo, app, posicao = None):
        self.ticks = 0
        self.larg_mundo = larg_mundo
        self.alt_mundo = alt_mundo
        self.raio_sprite = 8
        self.app = app

        if posicao:
            self.posicao = posicao
        else:
            x_inimigo = random.randint(190, self.larg_mundo - 20)
            y_inimigo = random.randint(20, self.alt_mundo - 20)
            self.posicao = Vetor(x_inimigo, y_inimigo)

        self.estado = INVISIVEL

    def resetar(self):
        self.estado = INVISIVEL
        x_inimigo = random.randint(190, self.larg_mundo - 20)
        y_inimigo = random.randint(20, self.alt_mundo - 20)
        self.posicao = Vetor(x_inimigo, y_inimigo)

        self.estado = VIVO

    def atualizar(self):
        pass

    def ativar(self):
        self.estado = VIVO
        
    def matar(self):
        self.estado = MORTO
    def desenhar(self):
        self.estado = VIVO

        aleatorio = range(1,3)

        if aleatorio == 1:
            sprite = self.olho
        elif aleatorio == 2:
            sprite = self.boca
        elif aleatorio == 3:
            sprite = self.nota

        pyxel.blt(self.posicao.x, self.posicao.y, 0, sprite[0], sprite[1], 16, 16)

class Jogo:
    def __init__(self):
        pyxel.init(255, 255, caption = 'RUOK')

        self.score = 0
        self.modo_jogo = INICIO

        pyxel.mouse(False)

        pyxel.load('RUOK.pyxel')

        self.inimigos = []

        pyxel.run(self.update, self.draw)

    def update(self):
        for inimigos in self.inimigos:
            inimigos.atualizar()

        if self.modo_jogo == INICIO and pyxel.btn(pyxel.KEY_S):
            
            inimigo = Inimigo(pyxel.widht, pyxel.height, self)
            self.inimigos.append(inimigo)
            inimigo.ativar()
            self.modo_jogo = ATIRANDO


       # if self.modo_jogo == ATIRANDO:

    def draw(self):
           
        pyxel.cls(5)
           
        for inimigo in self.inimigos:
            inimigo.desenhar()

        pyxel.text(10,10,'SCORE{}' .format(self.score), pyxel.frame_count % 16)

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 16, 16, 10)


Jogo()

    
            
            

        

        
    
    


        

