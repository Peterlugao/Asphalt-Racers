from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *
import math

janela = Window(900,600)
tela = GameImage("Imagens\MENU1.png")
janela.set_title("Asphalt Racers")
capa1 = GameImage("Imagens\capa1.jpg")
capa1.x = 340
capa2 = GameImage("Imagens\capa2.jpg")
capa2.x = 340
capa3 = GameImage("Imagens\capa3.jpg")
capa3.x = 340
capa4 = GameImage("Imagens\capa4.jpg")
capa4.x = 340
capa5 = GameImage("Imagens\capa5.jpg")
capa5.x = 340
capa6 = GameImage("Imagens\capa6.jpg")
capa6.x = 340
capas = [capa1,capa2,capa3,capa4,capa5,capa6]

#Imagens:

controles = GameImage("Imagens\controles.png")

creditos = GameImage("Imagens\creditos.png")
creditos.y = janela.height/2 - 180
creditos.x = -15

icone_pplay = GameImage("Imagens\icone_pplay.png")
icone_pplay.x = 0
icone_pplay.y = janela.height - icone_pplay.height

logo = GameImage("Imagens\LOGO.png")
logo.x = janela.width/2 - logo.width/2 - 200
logo.y = janela.height/2 - 275

fundo = GameImage ("Imagens\Back.jpeg")

fasenormal = GameImage ("Imagens\LEVELNORMAL.png")
fasenormal.x = 25

faseinfinita = GameImage ("Imagens\LEVELINFINITO.jpg")
faseinfinita.x = janela.width - 25 - faseinfinita.width
fase2 = GameImage ("Imagens\LEVEL2.png")
fase2.x = janela.width - 25 - faseinfinita.width

pista_rodovia = GameImage("Imagens\Summer_road.png")
pista_rodovia.x = 1050
pista_rodovia.y = 300

pista_inverno = GameImage("Imagens\Winter_road.png")
pista_inverno.x = 840
pista_inverno.y = 90

pista_ponte = GameImage("Imagens\Highway_road.png")
pista_ponte.x = 1050
pista_ponte.y = 90

pista_deserto = GameImage("Imagens\Desert_road.png")
pista_deserto.x = 840
pista_deserto.y = 300

level = GameImage("Imagens\level.png")
level.x = 2
level.y = 5

#Musicas e sons:

musica_menu = Sound("Musicas e sons\musica_menu_inicial.ogg")
#musica_rodovia = Sound("Musicas e sons\musica_rodovia.ogg")
#musica_inverno = Sound("Musicas e sons\musica_inverno.ogg")
som_botao = Sound("Musicas e sons\som_botao.ogg")

#Botões:

botao_play = GameImage("Imagens\jogar.png")
botao_play_pressed = GameImage("Imagens\jogar1.png")
botao_play.x = janela.width/4 - botao_play.width/2 - 50
botao_play.y = janela.height/2 - 100 + 20
botao_play_pressed.x = janela.width/4 - botao_play.width/2 - 50
botao_play_pressed.y = janela.height/2 - 100 + 20

botao_normal = GameImage("Imagens\ok.png")
botao_normal_pressed = GameImage("Imagens\ok1.png")
botao_normal.x = 25 + fasenormal.width/4 - 10
botao_normal.y = janela.height - janela.height/4
botao_normal_pressed.x = 25 + fasenormal.width/4 - 20
botao_normal_pressed.y = janela.height - janela.height/4

botao_infinito = GameImage("Imagens\infinito.png")
botao_infinito_pressed = GameImage("Imagens\infinito1.png")
botao_infinito.x = janela.width - 25 - faseinfinita.width + faseinfinita.width/4 + 20
botao_infinito.y = janela.height - janela.height/4
botao_infinito_pressed.x = janela.width - 25 - faseinfinita.width + faseinfinita.width/4 - 10 + 20
botao_infinito_pressed.y = janela.height - janela.height/4

cadeado1 = GameImage("Imagens\cadeado1.png")
cadeado1.x = faseinfinita.x + faseinfinita.width/2 - cadeado1.width/2 + 30
cadeado1.y = janela.height - janela.height/3
cadeado2 = GameImage("Imagens\cadeado2.png")
cadeado2.x = faseinfinita.x + faseinfinita.width/2 - cadeado2.width/2 + 30
cadeado2.y = janela.height - janela.height/3 - 20

botao_extra = GameImage("Imagens\extra.png")
botao_extra_pressed = GameImage("Imagens\extra1.png")
botao_extra.x = janela.width/4 - botao_play.width/2 - 50
botao_extra.y = janela.height/2 + 20
botao_extra_pressed.x = janela.width/4 - botao_play.width/2 - 50
botao_extra_pressed.y = janela.height/2 + 20

botao_creditos = GameImage("Imagens\Credito.png")
botao_creditos_pressed = GameImage("Imagens\creditos1.png")
botao_creditos.x = janela.width/4 - botao_play.width/2 - 50
botao_creditos.y = janela.height/2 + 110
botao_creditos_pressed.x = janela.width/4 - botao_play.width/2 - 50
botao_creditos_pressed.y = janela.height/2 + 110

botao_tutorial = GameImage("Imagens\Tutorial.png")
botao_tutorial_pressed = GameImage("Imagens\Tutorial1.png")
botao_tutorial.x = janela.width / 4 - botao_play.width / 2 - 50
botao_tutorial.y = janela.height / 2 - 50
botao_tutorial_pressed.x = janela.width / 4 - botao_play.width / 2 - 50
botao_tutorial_pressed.y = janela.height / 2 - 50

botao_saida = GameImage("Imagens\sair.png")
botao_saida_pressed = GameImage("Imagens\sair1.png")
botao_saida.x = janela.width/4 - botao_play.width/2 - 50
botao_saida.y = janela.height / 2 + 100 + 20
botao_saida_pressed.x = janela.width/4 - botao_play.width/2 - 50
botao_saida_pressed.y = janela.height / 2 + 100 + 20

botao_saida_menor = GameImage("Imagens\sair_menor.png")
botao_saida_menor.x = janela.width / 2 - 650
botao_saida_menor.y = janela.height / 2 - 350