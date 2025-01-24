from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from carro import *



cenario.draw()
menu.draw()
level1.draw()

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

for i in range(4):
    for j in range(5):
        carros[i][j].draw()
if policia == True:
    policia0.draw()
    policia1.draw()
if velcar > 0 and morto==False:
    if teclado.key_pressed("right"):
        carroright.draw()
    if teclado.key_pressed("left"):
        carroleft.draw()
if ((not(teclado.key_pressed("right")) and not(teclado.key_pressed("left"))) or ((velcar==0) and (batido == False))):
    carro.draw()
if morto == True:
    carro.draw()
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

if revigorado == True:
    carregar.draw()
    carregar.update()
if batido == True:
    carrogirando.draw()
    carrogirando.update()
    explosao.draw()
    explosao.update()
if vidas == 3:
    cabine3.draw()
if vidas == 2:
    cabine2.draw()
if vidas == 1:
    cabine1.draw()
if vidas == 0:
    cabine0.draw()
janela.update()