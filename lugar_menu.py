import pygame
import modo_menu
from modo_menu import *
musica_menu.loop = True
modo_menu.musica_menu.set_volume(80)
modo_menu.musica_menu.stop()
modo_menu.musica_menu.play()

def lugar_menu(janela, mouse, teclado):
    modo = 1
    while True:
        #Ilustração do menu
        if modo == 1:
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
            if mouse.is_over_object(botao_extra):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 3
            if mouse.is_over_object(botao_saida):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    janela.close()

        #Ilustração das fases

        if modo == 2:
            janela.set_background_color([255,255,255])
            modo_menu.botao_normal.draw()
            modo_menu.botao_infinito.draw()
            modo_menu.botao_saida_menor.draw()

            if mouse.is_over_object(botao_normal):
                modo_menu.chegada_imagem.draw()

            if mouse.is_over_object(botao_infinito):
               modo_menu.infinito_imagem.draw()

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
            modo_menu.tela.draw()
            modo_menu.logo.draw()
            modo_menu.botao_creditos.draw()
            modo_menu.botao_concept_art.draw()
            modo_menu.botao_saida_menor.draw()

            # Ilustração dos creditos:

            if mouse.is_over_object(botao_creditos):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 6

            # Ilustração do Concept Art:

            if mouse.is_over_object(botao_concept_art):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 4

            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 1

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 1

        if modo == 4:
            janela.set_background_color([255, 255, 255])
            modo_menu.botao_saida_menor.draw()
            modo_menu.pistas_letras.draw()
            modo_menu.veiculos_letras.draw()
            modo_menu.jogador_verde.draw()
            modo_menu.jogador_azul.draw()
            modo_menu.jogador_amarelo.draw()
            modo_menu.pista_rodovia.draw()
            modo_menu.pista_inverno.draw()
            modo_menu.pista_deserto.draw()
            modo_menu.pista_ponte.draw()


            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 3

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 3


        if modo == 6:
            janela.set_background_color([255,255,255])
            modo_menu.icone_pplay.draw()
            modo_menu.botao_saida_menor.draw()
            modo_menu.creditos_letras.draw()

            if mouse.is_over_object(botao_saida_menor):
                if mouse.is_button_pressed(1):
                    pygame.time.wait(100)
                    modo_menu.som_botao.set_volume(30)
                    modo_menu.som_botao.stop()
                    modo_menu.som_botao.play()
                    modo = 3

            if teclado.key_pressed("ESC"):
                pygame.time.wait(100)
                modo_menu.som_botao.set_volume(30)
                modo_menu.som_botao.stop()
                modo_menu.som_botao.play()
                modo = 3

        if teclado.key_pressed("M"):
            modo_menu.musica_menu.stop()
        if teclado.key_pressed("N"):
            modo_menu.musica_menu.set_volume(80)
            modo_menu.musica_menu.stop()
            modo_menu.musica_menu.play()

        janela.update()
