#"Rascunho" do jogo, aonde foi testado varias funções e ideias aleatorias.

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import random

janela = Window(900, 600)
janela.set_title("PongBol")
cenario = GameImage("campo (1).jpg")
bola = GameImage("bolaa.png")
gol1 = Sprite("goleiro (5).png")
gol2 = GameImage("goleiro (4).png")

gol1.x= -50
gol1.y = janela.height/2 - gol1.height

gol2.x= janela.width - 200
gol2.y = janela.height/2 - gol2.height

bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2

velx = 0.5
vely = 0.5

vegx = 0.6
vegy = 0.7

ale= random.randint(0,1)
ato= random.randint(2,3)
while True:
    gol1.move_key_y(0.6)

    if ale==1:
        bola.x += velx
    elif ale==0:
        bola.x -= velx
    if ato==2:
        bola.y += vely
    elif ato==3:
        bola.y -= vely

    if (bola.y<0 or bola.y>546):
        vely = -vely

    gol2.y += vegy
    if (gol2.y<0 or gol2.y>380):
        vegy = -vegy

    if bola.collided(gol1):
        velx = velx * -1.1

    if bola.collided(gol2):
        velx = -velx * -1.1

    cenario.draw()
    gol1.draw()
    gol2.draw()
    bola.draw()
    janela.update()


    if teclado.key_pressed("up") and carro.y > 0:
        acelerar = True

    if acelerar == True:
        if velcar < vellimit:
            velcar -= 0.03
            carro.y -= velcar
        elif velcar >= vellimit:
            carro.y -= vellimit
        if teclado.key_pressed("down") and carro.y < janela.height - carro.height:
            acelerar = False
            desacelerar = True

    if desacelerar == True:
        if velcar < 0:
            velcar += 0.03
            carro.y += velcar
        elif velcar >= 0:
            desacelerar = False


    npc1.draw()
    npc2.draw()
    npc3.draw()
    npc4.draw()
    policia0.draw()
    policia1.draw()


    if teclado.key_pressed("right") and carro.x < janela.width/2 + 30:
        carro.x += 100 * janela.delta_time()
    if teclado.key_pressed("left") and carro.x > janela.width/2 - 44:
        carro.x -= 100 * janela.delta_time()

336
358
244
10100
4800
morto_delay = 2 + janela.delta_time() * 15

360
245
sinal.set_position(336,20)

304 e 354

x_position = random.randint(304, 354)

# Posição Y retirada da lista baralhada
y_position = y_positions.pop()

# Definindo o carro com suas posições
carros[i][j] = {"type": i, "x": x_position, "y": y_position}

for i in range(4):
    for j in range(12):
        if carros[i][j] != 0:
            if carros[i][j].collided(policia0):
                policia0.y = -50
                policia = False
                perigo_tempo = random.randint(7, 15)
                direction_perigo = random.randint(0, 3)
                carros[i][j] = 0
            if carros[i][j].collided(policia1):
                policia1.y = -650
                policia = False
                perigo_tempo = random.randint(7, 15)
                direction_perigo = random.randint(0, 3)
                carros[i][j] = 0
        if sorrac[i][j] != 0:
            if sorrac[i][j].collided(policia0):
                policia0.y = -50
                policia = False
                perigo_tempo = random.randint(7, 15)
                direction_perigo = random.randint(0, 3)
                sorrac[i][j] = 0
            if sorrac[i][j].collided(policia1):
                policia1.y = -650
                policia = False
                perigo_tempo = random.randint(7, 15)
                direction_perigo = random.randint(0, 3)
                sorrac[i][j] = 0


    if combustivel == False:
        if -15700 > cenario.y > -15750:
            fuel.x = random.randint(210,370)
            fuel.y = -70
            combustivel = True
    if combustivel == False:
        if -10300 > cenario.y > -10350:
            fuel.x = random.randint(210, 370)
            fuel.y = -80
            combustivel = True
    if combustivel == False:
        if -4800 > cenario.y > -4850:
            fuel.x = random.randint(210, 370)
            fuel.y = -80
            combustivel = True
    if carro.collided(fuel):
        tanque = 100
        combustivel = False
        revigorado = True
    if fuel.y > 630:
        combustivel = False
    if moving_right:
        fuel.x += fuel_speed
        fuel_speed += acceleration
        if fuel.x >= 370:
            fuel_speed = min_speed
            moving_right = False
    else:
        fuel.x -= fuel_speed
        fuel_speed += acceleration
        if fuel.x <= 210:
            fuel_speed = min_speed
            moving_right = True
    fuel_speed = min(fuel_speed, max_speed)
    angulo += 0.01
    galao_y_offset = math.sin(angulo) * 0.085
    fuel.y += galao_y_offset
