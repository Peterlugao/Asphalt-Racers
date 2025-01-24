import pygame
import random
import modo_menu
from lixo2 import infinit_loop
from modo_menu import *
from carro import game_loop
from lixo2 import infinit_loop
musica_menu.loop = True
modo_menu.musica_menu.set_volume(80)
modo_menu.musica_menu.stop()
modo_menu.musica_menu.play()

def lugar_menu(janela, mouse, teclado, bloqueado):
    angulo1 = 0
    angulo2 = 0
    modo = 1
    modo_menu.logo.x = janela.width / 2 - logo.width / 2 - 200
    modo_menu.logo.y = janela.height / 2 - 275
    capa = random.randint(0,5)
    tela.x = -20
    while True:
        #Ilustração do menu
        angulo1 += 0.004
        logo_x_offset = math.sin(angulo1) * 0.05 * 1000 * janela.delta_time()
        angulo2 += 0.003
        capa_x_offset = math.sin(angulo1) * 0.01 * 1000 * janela.delta_time()
        tela.x += logo_x_offset
        logo.x += logo_x_offset
        modo_menu.botao_play_pressed.x += logo_x_offset
        modo_menu.botao_extra_pressed.x += logo_x_offset
        modo_menu.botao_extra.x += logo_x_offset
        modo_menu.botao_creditos.x += logo_x_offset
        modo_menu.botao_saida_pressed.x += logo_x_offset
        modo_menu.botao_creditos_pressed.x += logo_x_offset
        modo_menu.botao_play.x += logo_x_offset
        modo_menu.botao_tutorial.x += logo_x_offset
        modo_menu.botao_tutorial_pressed.x += logo_x_offset
        modo_menu.botao_saida.x += logo_x_offset
        modo_menu.creditos.x += logo_x_offset
        modo_menu.icone_pplay.x += logo_x_offset
        if modo == 1:
            modo_menu.capas[capa].draw()
            modo_menu.tela.draw()
            modo_menu.logo.draw()
            modo_menu.botao_play.draw()
            modo_menu.botao_extra.draw()
            modo_menu.botao_saida.draw()
            if mouse.is_over_object(botao_play):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 2
                    capa = random.randint(0, 5)
            if mouse.is_over_object(botao_extra):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 3
                    capa = random.randint(0, 5)
            if mouse.is_over_object(botao_saida):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    janela.close()

            modo_menu.botao_saida.draw()
            if mouse.is_over_object(botao_play):
                modo_menu.botao_play_pressed.draw()
            if mouse.is_over_object(botao_extra):
                modo_menu.botao_extra_pressed.draw()
            if mouse.is_over_object(botao_saida):
                modo_menu.botao_saida_pressed.draw()
        #Ilustração das fases

        if modo == 2:
            modo_menu.fundo.draw()
            modo_menu.fasenormal.draw()
            modo_menu.faseinfinita.draw()
            if bloqueado == False:
                modo_menu.fase2.draw()
            modo_menu.botao_normal.draw()
            modo_menu.botao_saida_menor.draw()
            if mouse.is_over_object(botao_normal):
                modo_menu.botao_normal_pressed.draw()
                if mouse.is_button_pressed(1):
                    bloqueado = game_loop (janela,mouse,teclado)
            if bloqueado == False:
                modo_menu.botao_infinito.draw()
                if mouse.is_over_object(botao_infinito):
                    modo_menu.botao_infinito_pressed.draw()
                    if mouse.is_button_pressed(1):
                        infinit_loop(janela,mouse,teclado)
            else:
                if not(mouse.is_over_object(cadeado1)):
                    modo_menu.cadeado1.draw()
                if mouse.is_over_object(cadeado1):
                    modo_menu.cadeado2.draw()

            modo_menu.level.draw()

           #if mouse.is_over_object(botao_rodovia):
               #modo_menu.imagem_rodovia.draw()

           #if mouse.is_over_object(botao_inverno):
               #modo_menu.imagem_inverno.draw()

            #Caso queira voltar ao menu:

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 1

            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 1

        #Ilustração do Extra:

        if modo == 3:
            modo_menu.capas[capa].draw()
            modo_menu.tela.draw()
            modo_menu.logo.draw()
            modo_menu.botao_creditos.draw()
            modo_menu.botao_tutorial.draw()
            modo_menu.botao_saida_menor.draw()

            # Ilustração dos creditos:

            if mouse.is_over_object(botao_creditos):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 6
                    capa = random.randint(0, 5)

            # Ilustração do Concept Art:

            if mouse.is_over_object(botao_tutorial):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 4
                    capa = random.randint(0, 5)

            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 1
                    capa = random.randint(0, 5)

            if mouse.is_over_object(botao_tutorial):
                modo_menu.botao_tutorial_pressed.draw()
            if mouse.is_over_object(botao_creditos):
                modo_menu.botao_creditos_pressed.draw()

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 1
                capa = random.randint(0, 5)

        if modo == 4:
            modo_menu.controles.draw()

            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 3
                    capa = random.randint(0, 5)

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 3
                capa = random.randint(0, 5)


        if modo == 6:
            modo_menu.capas[capa].draw()
            modo_menu.tela.draw()
            modo_menu.logo.draw()
            modo_menu.icone_pplay.draw()
            modo_menu.botao_saida_menor.draw()
            modo_menu.creditos.draw()
            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 3
                    capa = random.randint(0, 5)

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 3
                capa = random.randint(0, 5)

        if teclado.key_pressed("M"):
            modo_menu.musica_menu.stop()
        if teclado.key_pressed("N"):
            modo_menu.musica_menu.set_volume(80)
            modo_menu.musica_menu.stop()
            modo_menu.musica_menu.play()


        janela.update()
