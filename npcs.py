from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
import random

def criar_carros_indo (janela, carros):
    y_positions = [-15000  + i * ( 600 - (-15000 )) // (4 * 15) + random.randint(-350, 350) for i in range(4 * 15)]
    random.shuffle(y_positions)
    for i in range (4):
        for j in range (15):
            if i == 0:
                carro = Sprite("Imagens\Bot-1.png")
            if i == 1:
                carro = Sprite("Imagens\Bot-2.png")
            if i == 2:
                carro = Sprite("Imagens\Bot-3.png")
            if i == 3:
                carro = Sprite("Imagens\Bot-4.png")
            carro.y = y_positions.pop()
            carro.x = random.randint(310, 354)
            carros[i][j] = carro

def criar_carros_vindo (janela, sorrac):
    y_positions = [-5500 + i * (-21500 - -5500) // (4 * 15) for i in range(4 * 15)]
    random.shuffle(y_positions)
    for i in range (4):
        for j in range (15):
            if i == 0:
                carro = Sprite("Imagens\Bot1.png")
            if i == 1:
                carro = Sprite("Imagens\Bot2.png")
            if i == 2:
                carro = Sprite("Imagens\Bot3.png")
            if i == 3:
                carro = Sprite("Imagens\Bot4.png")
            carro.y = y_positions.pop()
            carro.x = random.randint(245, 285)
            sorrac[i][j] = carro