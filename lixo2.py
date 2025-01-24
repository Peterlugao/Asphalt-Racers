from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
from npcs import criar_carros_indo
from npcs import criar_carros_vindo
from objects import criar_caixas
import sys
import math
import random

clock = pygame.time.Clock()
clock.tick(120)

#Objetos de tela:
janela = Window(900, 600)
cenario1 = GameImage("Imagens\pistaneve.png")
cenario1.set_position(0,0)
cenario2 = GameImage("Imagens\pista2neve.png")
cenario2.set_position(0,-600)
cenario3 = GameImage("Imagens\pistaneve.png")
cenario3.set_position(0,-1200)
cenario4 = GameImage("Imagens\pista2neve.png")
cenario4.set_position(0,-1800)
cenario5 = GameImage("Imagens\postoneve.png")
cenario5.set_position(0,-2400)
cenarios = [cenario1,cenario2,cenario3,cenario4,cenario5]
start = GameImage ("Imagens\START (48 x 8).png")
start.set_position(306, 300)
gameover = GameImage ("Imagens\GAME_OVER (72 x 8).png")
gameover.set_position(250, 300)
menu = GameImage ("Imagens\menu.png")
level1 = GameImage ("Imagens\iconeinfinito.png")
cabine3 = GameImage ("Imagens\Vida3.png")
cabine2 = GameImage ("Imagens\Vida2.png")
cabine1 = GameImage ("Imagens\Vida1.png")
cabine0 = GameImage ("Imagens\Vida0.png")
tanquecheio = GameImage ("Imagens\Tanquecheio.png")
tanquemedio = GameImage ("Imagens\Tanchemedio.png")
tanquemediano = GameImage ("Imagens\Tanquemediano.png")
tanquelow = GameImage ("Imagens\Tanquelow.png")
tanquevazio = GameImage ("Imagens\Tanqueteia.png")
item = GameImage ("Imagens\Box.png")
item.set_position(0,600-item.height)
tirobox = GameImage ("Imagens\Rocket.png")
tirobox.set_position(0,600-item.height)
nitrobox = GameImage ("Imagens\Turbo.png")
nitrobox.set_position(0,600-item.height)
fuelbox = GameImage ("Imagens\Fuel.png")
fuelbox.set_position(0,600-item.height)
lifebox = GameImage ("Imagens\Tresxbonus.png")
lifebox.set_position(0,600-item.height)
specialbox = GameImage ("Imagens\special.png")
specialbox.set_position(0,600-item.height)
itens = Sprite ("Imagens\Boxaleatorio1.jpg", 5)
itens.set_position(0,600-itens.height)
itens.set_total_duration(500)
level1.set_position(580,-150)
tanquecheio.set_position(700, 400)
tanquemedio.set_position(700, 400)
tanquemediano.set_position(700, 400)
tanquelow.set_position(700, 400)
tanquevazio.set_position(700, 400)
menu.x = 550
cabine3.set_position(600, 100)
cabine2.set_position(600, 100)
cabine1.set_position(600, 100)
cabine0.set_position(600, 100)

#Objetos de Gameplay:
carro = Sprite("Imagens\carro maior.png")
carroleft = Sprite("Imagens\carroesquerda.png")
carroright = Sprite("Imagens\carrodireita.png")
carroespecial = Sprite("Imagens\carroespecial.png")
carromorto = Sprite("Imagens\carromorto.png", 4)
carromorto.set_total_duration(750)
carrogirando = Sprite("Imagens\Player_red (16 x 16).png",8)
carrogirando.set_total_duration(1000)
npc1 = GameImage("Imagens\Bot1.png")
npc2 = GameImage("Imagens\Bot2.png")
npc3 = GameImage("Imagens\Bot3.png")
npc4 = GameImage("Imagens\Bot4.png")
policia1 = GameImage ("Imagens\policia1.png")
policia0 = GameImage ("Imagens\policia-1.png")
fuel = GameImage ("Imagens\galao.png")
explosao = Sprite("Imagens\Explosion (16 x 16).png",6)
explosao.set_total_duration(500)
carregar = Sprite("Imagens\Sparkle (16 x 16).png",5)
carregar.set_total_duration(500)
caixotado = Sprite("Imagens\carregado.png",5)
caixotado.set_total_duration(600)
sinal = Sprite ("Imagens\sinalperigo.png",4)
sinal.set_total_duration(500)
sinal.set_position(336,20)

def infinit_loop (janela, mouse, teclado):
    carros = [[0 for i in range(15)] for j in range(4)]
    criar_carros_indo(janela, carros)
    sorrac = [[0 for i in range(15)] for j in range(4)]
    criar_carros_vindo(janela, sorrac)
    caixas = []
    criar_caixas(janela,caixas)

    angulo1 = 0
    angulo = 0  # Ângulo para o balanço
    fuel.x = 320
    fuel.y = 18000
    fuel_speed = 0.12
    max_speed = 0.22
    min_speed = 0.02
    acceleration = 0.001
    moving_right = True
    combustivel = False
    tanque = 75
    morto = False
    posmorte = False


    positionx = 336
    positiony = janela.height/1 - 3 * carro.height - 150
    positioncrash = 366
    policia0.set_position(336,-50)
    policia1.set_position(336, 650)
    policiavel = 0.45

    perigo_tempo = random.randint(10,17)
    direction_perigo = random.randint (0,3)
    vidas = 3
    vellimit = 0.4
    velcar = 0
    acelerar = False
    desacelerar = False
    revigorado = False
    perigo = False
    policia = False
    policia_delay = perigo_tempo + janela.delta_time() * 15
    perigo_delay = 2.5 + janela.delta_time() * 15
    perigo_tick = 0
    morto_tick = 0
    revigorado_delay = 1.2 + janela.delta_time() * 15
    revigorado_tick = 0
    batido = False
    batido_delay = 2 + janela.delta_time() * 15
    batido_tick = 0
    aleatorio = False
    item_delay = 1.7 + janela.delta_time() * 15
    item_tick = 0
    itemaleatorio = random.randint(1,9)
    teclado = Window.get_keyboard()

    #Itens:

    tiro = GameImage ("Imagens\missel.png")
    rocket = False
    ROCKET = False
    nitro = False
    NITRO = False
    nitro_delay = 3 + janela.delta_time() * 15
    carronitro = Sprite("Imagens\Turbocarro.png",2)
    carronitro.set_total_duration(250)
    vida = False
    especial = False
    ESPECIAL = False
    abastecer = False
    CAIXA = False
    tiro.set_position(positionx - 6, positiony)
    ultimox = 0

    inicio = True
    inicio_delay = 5 + janela.delta_time() *15
    inicio_tick = 0
    carro.set_position(positionx, 600 + carro.height)
    fim = False

    contcaixa= 0
    while True:
        if not (inicio == True):
            carro.set_position(positionx, positiony)
        carroleft.set_position(positionx, positiony)
        carroright.set_position(positionx, positiony)
        carrogirando.set_position(positionx - 6, positiony)
        carromorto.set_position(positionx, positiony)
        carronitro.set_position(positionx, positiony)
        carroespecial.set_position(positionx, positiony)
        explosao.set_position(positionx - 6, positiony)
        carregar.set_position(positionx - 6, positiony)
        caixotado.set_position(positionx - 6, positiony)
        tiro.x = positionx
        if not (inicio == True):
            if velcar > 0 and morto == False:
                if teclado.key_pressed("right") and carro.x < 360:
                    positionx += 100 * janela.delta_time()
                if teclado.key_pressed("left") and carro.x > 245:
                    positionx -= 100 * janela.delta_time()
                if carro.x <= 245:
                    batido = True
                    morto = True
                    ESPECIAL = False
                    NITRO = False
                    positioncrash = 255
                    velcar = 0
                if carro.x >= 360:
                    batido = True
                    morto = True
                    ESPECIAL = False
                    NITRO = False
                    positioncrash = 345
                    velcar = 0


        #START:
        if inicio == True:
            inicio_tick += janela.delta_time()
            if carro.y > positiony:
                carro.y -= 0.35
            else:
                carro.y = positiony
            if inicio_tick >= inicio_delay:
                inicio = False
                inicio_tick = 0
        #GAMEOVER:
        if fim == True:
            inicio_tick += janela.delta_time()
            if inicio_tick >= inicio_delay:
                fim = False
                inicio_tick = 0
                return
        if inicio == False and fim == False:
            if teclado.key_pressed("esc"):
                return

        #Movimento de acelerar
        if not (inicio == True):
            if morto == False:
                if teclado.key_pressed("up") and carro.y > 0:
                    acelerar = True
                    desacelerar = False

                if acelerar == True:
                    if velcar < vellimit:
                        velcar += 0.1 * janela.delta_time()
                    elif velcar >= vellimit:
                        velcar = vellimit

        #Movimento de desacelerar
        if not (teclado.key_pressed("up")):
            acelerar = False
            desacelerar = True

        if desacelerar == True:
            if velcar != 0:
                if teclado.key_pressed("down"):
                    velcar -= 0.4 * janela.delta_time()
                else:
                    velcar -= 0.15 * janela.delta_time()
            if velcar < 0:
                velcar = 0
            if velcar == 0:
                desacelerar = False

    #Movimento Geral:

        #Policia:
        if policia == True:
            if direction_perigo == 0 or direction_perigo == 1:
                policia0.y += policiavel *janela.delta_time() * 1000/2
            if direction_perigo == 2 or direction_perigo == 3:
                policia1.y -= (policiavel*1.5) *janela.delta_time() * 1000/2
            if batido == False and morto == False:
                if not (posmorte == True):
                    if not (fim == True):
                        if carro.collided(policia0) or carro.collided(policia1):
                            if not (ESPECIAL == True):
                                batido = True
                                morto = True
                                positioncrash = 336
                                velcar = 0
                            policia0.y = -50
                            policia1.y = 650
                            policia = False
                            perigo_tempo = random.randint(7, 15)
                            direction_perigo = random.randint(0, 3)
            if direction_perigo == 0 or direction_perigo == 1:
                if policia0.x < carro.x:
                    policia0.x += 15 * janela.delta_time()
                if policia0.x > carro.x:
                    policia0.x -= 15 * janela.delta_time()
            if direction_perigo == 2 or direction_perigo == 3:
                if policia1.x < carro.x:
                    policia1.x += 15 * janela.delta_time()
                if policia1.x > carro.x:
                    policia1.x -= 15 * janela.delta_time()

        if policia0.y > 900:
            policia0.y = -50
            policia = False
            perigo_tempo = random.randint(7, 15)
            direction_perigo = random.randint(0, 3)
        if policia1.y < 0:
            policia1.y = 650
            policia = False
            perigo_tempo = random.randint(7, 15)
            direction_perigo = random.randint(0, 3)

    #Movimento cenario:
        #CENARIO
        for i in range (5):
            cenarios[i].y += velcar * janela.delta_time() * 1000
        for i in range (5):
            if cenarios[i].y >= 600:
                cenarios[i].y = -2400
                break
            else:
                continue
        fuel.y += velcar *janela.delta_time() * 1000
        tanque -= velcar*janela.delta_time() * 7.5
        if policia == True:
            if direction_perigo == 0 or direction_perigo == 1:
                policia0.y += velcar*janela.delta_time() * 1000/2
            if direction_perigo == 2 or direction_perigo == 3:
                policia1.y += velcar*janela.delta_time() * 1000/2
        for i in range (4):
            for j in range(15):
                if carros[i][j] != 0:
                    carros[i][j].y += velcar*janela.delta_time() * 1000
                if sorrac[i][j] != 0:
                    sorrac[i][j].y += velcar*janela.delta_time() * 1000
        for i in range (4):
            if caixas[i] != 0:
                caixas[i].y += velcar *janela.delta_time() * 1000
        for i in range (4):
            for j in range(15):
                if carros[i][j] != 0:
                    if carros[i][j].y >= 600:
                        carros[i][j].y = -15000
                if sorrac[i][j] != 0:
                    if sorrac[i][j].y >= 600:
                        sorrac[i][j].y = -15000

        #NPCs:
        for i in range(4):
            for j in range(15):
                if carros[i][j] != 0:
                    carros[i][j].y -= 0.25
                    if batido == False or morto == False:
                        if not (posmorte == True):
                            if (not (fim == True)):
                                if not (inicio == True):
                                    if carros[i][j].collided(carro):
                                        carros[i][j] = 0
                                        if not (ESPECIAL == True):
                                            velcar = 0
                                            positioncrash = 336
                                            morto = True
                                            batido = True
                if sorrac[i][j] != 0:
                    sorrac[i][j].y += 0.2
                    if batido == False or morto == False:
                        if not (posmorte == True):
                            if not (fim == True):
                                if not (inicio == True):
                                    if sorrac[i][j].collided(carro):
                                        sorrac[i][j] = 0
                                        if not (ESPECIAL == True):
                                            velcar = 0
                                            positioncrash = 336
                                            morto = True
                                            batido = True

        #Combustível
        if combustivel == False:
            if -350 < cenarios[4].y < -300:
                fuel.x = random.randint(210,370)
                fuel.y = -70
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


    #Caixa de Itens:

        angulo1 += 0.005
        box_x_offset = math.sin(angulo1) * 0.1
        for i in range (4):
            if caixas[i] != 0:
                caixas[i].x -= box_x_offset

        for i in range(4):
            if caixas[i] != 0:
                if caixas[i].collided(carro):
                    caixas[i] = 0
                    aleatorio = True

        for i in range(4):
            if caixas[i] == 0:
                contcaixa += 1
            else:
                if caixas[i].y >= 600:
                    contcaixa += 1

        if contcaixa == 4:
            criar_caixas(janela,caixas)
            contcaixa = 0

        if aleatorio == True:
            item_tick += janela.delta_time()
            if item_tick >= item_delay:
                itemaleatorio = random.randint(1,10)
                aleatorio = False
                item_tick = 0
                CAIXA = True
        if CAIXA == True:
            if itemaleatorio == 1 or itemaleatorio == 2:
                rocket = True
            if itemaleatorio == 3 or itemaleatorio == 4:
                nitro = True
            if itemaleatorio == 5 or itemaleatorio == 6:
                abastecer = True
            if itemaleatorio == 7 or itemaleatorio == 8:
                vida = True
            if itemaleatorio == 9 or itemaleatorio == 10:
                especial = True

        #ESPECIAL
        if especial == True:
            if teclado.key_pressed("space"):
                especial = False
                ESPECIAL = True
                CAIXA = False
        if ESPECIAL == True:
            item_tick += janela.delta_time()
            if item_tick >= nitro_delay+0.5:
                ESPECIAL = False
                item_tick = 0
        #BONUS
        if vida == True:
            if teclado.key_pressed("space"):
                if vidas < 3:
                    vidas += 1
                vida = False
                CAIXA = False
        #ABASTECER
        if abastecer == True:
            if teclado.key_pressed("space"):
                if tanque > 70:
                    tanque = 100
                else:
                    tanque += 30
                abastecer = False
                CAIXA = False
                revigorado = True
        #NITRO
        if nitro == True:
            if teclado.key_pressed("space"):
                NITRO = True
                nitro = False
                CAIXA = False
        if NITRO == True:
            vellimit = 0.6
            item_tick += janela.delta_time()
            if item_tick >= nitro_delay:
                NITRO = False
                item_tick = 0
                vellimit = 0.4
        #ROCKET
        if rocket == True:
            if teclado.key_pressed("space"):
                ultimox = positionx
                ROCKET = True
                rocket = False
                CAIXA = False
        if ROCKET == True:
            tiro.x = ultimox
            tiro.y -= 0.5 * janela.delta_time()*1000
            if tiro.y >= 700:
                tiro.y = positiony
                ROCKET = False
            if tiro.collided(policia0):
                tiro.y = positiony
                ROCKET = False
                policia = False
                policia0.y = -50
            if tiro.collided(policia1):
                tiro.y = positiony
                ROCKET = False
                policia = False
                policia1.y = 650
            for i in range(4):
                for j in range(15):
                    if carros[i][j] != 0:
                        if carros[i][j].collided(tiro):
                            carros[i][j] = 0
                            tiro.y = positiony
                            ROCKET = False
                            policia0.y = 650

    #Efeitos:

        if revigorado == True:
            revigorado_tick += janela.delta_time()
            if revigorado_tick >= revigorado_delay:
                revigorado_tick = 0
                revigorado = False
        if batido == True:
            batido_tick += janela.delta_time()
            carro.y = -100000
            if batido_tick >= batido_delay:
                batido_tick = 0
                tanque -= 10
                batido = False
                morto = False
                carro.y = positiony
                positionx = positioncrash
                vidas -= 1
                if vidas > 0:
                    posmorte = True
        if posmorte == True:
            morto_tick += janela.delta_time()
            if morto_tick >= perigo_delay:
                    posmorte = False
                    morto_tick = 0

        if tanque <= 0:
            morto = True
            desacelerar = True
            acelerar = False
            fim = True

        if vidas <= 0:
            morto = True
            fim = True

    #Perigo = Teste!
        if perigo == False and policia == False:
            perigo_tick += janela.delta_time()
            if perigo_tick >= policia_delay:
                perigo = True
                perigo_tick = 0

        if perigo == True:
            perigo_tick += janela.delta_time()
            if perigo_tick >= perigo_delay:
                perigo = False
                perigo_tick = 0
                policia = True



    #DRAW:
        for i in range (5):
            cenarios[i].draw()
        menu.draw()
        level1.draw()

        for i in range(4):
            for j in range(15):
                if carros[i][j] != 0:
                    carros[i][j].draw()
                if sorrac[i][j] != 0:
                    sorrac[i][j].draw()
        if policia == True:
            policia0.draw()
            policia1.draw()

        if perigo == True:
            if direction_perigo == 0:
                sinal.set_position(265, 20)
                policia0.set_position(255, -50)
            if direction_perigo == 1:
                sinal.set_position(336, 20)
                policia0.set_position(336, -50)
            if direction_perigo == 2:
                sinal.set_position(265, 520)
                policia1.set_position(255, 620)
            if direction_perigo == 3:
                sinal.set_position(336, 520)
                policia1.set_position(336, 620)
            sinal.draw()
            sinal.update()

        if posmorte == False:
            if (velcar > 0 and morto == False):
                if teclado.key_pressed("right"):
                    if not (NITRO == True):
                        if not (ESPECIAL == True):
                            carroright.draw()
                if teclado.key_pressed("left"):
                    if not (NITRO == True):
                        if not (ESPECIAL == True):
                            carroleft.draw()
            if not (ESPECIAL == True):
                if not (fim == True):
                    if ((not (teclado.key_pressed("right")) and not (teclado.key_pressed("left"))) or (
                            (velcar == 0) and (batido == False))):
                        carro.draw()
        else:
            carromorto.draw()
            carromorto.update()
        if morto == True and tanque <= 0:
            carro.y = -10000
        if combustivel == True:
            fuel.draw()
        if 100 >= tanque >= 75:
            tanquecheio.draw()
        if 75 >= tanque >= 50:
            tanquemedio.draw()
        if 50 >= tanque >= 25:
            tanquemediano.draw()
        if 25 >= tanque >= 0:
            tanquelow.draw()
        if tanque <= 0:
            tanquevazio.draw()
        if vidas == 3:
            cabine3.draw()
        if vidas == 2:
            cabine2.draw()
        if vidas == 1:
            cabine1.draw()
        if vidas <= 0:
            cabine0.draw()

        for i in range (4):
            if caixas[i] != 0:
                caixas[i].draw()
        itens.draw()
        itens.update()
        if aleatorio == False:
            item.draw()
        else:
            caixotado.draw()
            caixotado.update()
        if rocket == True:
            tirobox.draw()
        if ROCKET == True:
            tiro.draw()
        if nitro == True:
            nitrobox.draw()
        if NITRO == True:
            carronitro.draw()
            carronitro.update()
        if abastecer == True:
            fuelbox.draw()
        if vida == True:
            lifebox.draw()
        if especial == True:
            specialbox.draw()
        if ESPECIAL == True:
            carroespecial.draw()

        if revigorado == True:
            carregar.draw()
            carregar.update()
        if batido == True:
            carrogirando.draw()
            carrogirando.update()
            explosao.draw()
            explosao.update()
        if (3 < inicio_tick < inicio_delay) and inicio == True:
            start.draw()
        if fim == True:
            gameover.draw()
        janela.update()