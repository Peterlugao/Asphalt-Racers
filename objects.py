from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import random

def criar_caixas(janela,caixas):
    y_positions = [-15000 + i * (3000 - (-15000)) // 5 for i in range(5)]
    y_positions = [pos + random.randint(-500, 500) for pos in y_positions]
    random.shuffle(y_positions)
    for i in range(4):
        caixa = GameImage ("Imagens\caixa.jpg")
        caixa.y = y_positions.pop()
        caixa.x = random.randint(265, 340)
        caixas.append(caixa)
