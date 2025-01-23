from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sound import *

janela = Window(1300,700)
tela = GameImage("Imagens\Fundo.jpg")
janela.set_title("Asphalt Racers")

#Imagens:

creditos_letras = GameImage("Imagens\creditos_letras.png")
creditos_letras.x = janela.width/2 - creditos_letras.width/2
creditos_letras.y = janela.height/2 - 200

pistas_letras = GameImage("Imagens\pistas.png")
pistas_letras.x = 890
pistas_letras.y = 550

veiculos_letras = GameImage("Imagens\Veiculos.png")
veiculos_letras.x = 250
veiculos_letras.y = 550

jogador_verde = GameImage("Imagens\jogador_verde.png")
jogador_verde.x = 280
jogador_verde.y = 300

jogador_azul = GameImage("Imagens\jogador_azul.png")
jogador_azul.x = 280
jogador_azul.y = 350

jogador_amarelo = GameImage("Imagens\jogador_amarelo.png")
jogador_amarelo.x = 280
jogador_amarelo.y = 400

icone_pplay = GameImage("Imagens\icone_pplay.png")
icone_pplay.x = 0
icone_pplay.y = janela.height / 2 + 250

chegada_imagem = GameImage("Imagens\chegada.png")
chegada_imagem.x = janela.width / 4 - chegada_imagem.width/ 2
chegada_imagem.y = janela.height / 2 - 20

infinito_imagem = GameImage("Imagens\infinito_imagem.png")
infinito_imagem.x = janela.width / 4 + infinito_imagem.width / 2 + 435
infinito_imagem.y = janela.height / 2 - 20

logo = GameImage("Imagens\Logo.png")
logo.x = janela.width/2 - logo.width/2
logo.y = janela.height/2 - 350

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

#Musicas e sons:

musica_menu = Sound("Musicas e sons\musica_menu_inicial.ogg")
#musica_rodovia = Sound("Musicas e sons\musica_rodovia.ogg")
#musica_inverno = Sound("Musicas e sons\musica_inverno.ogg")
som_botao = Sound("Musicas e sons\som_botao.ogg")

#Botões:

botao_play = GameImage("Imagens\jogar.png")
botao_play.x = janela.width/4 - botao_play.width/2 - 150
botao_play.y = janela.height/2 - 140

botao_normal = GameImage("Imagens\ok.png")
botao_normal.x = janela.width / 4 - botao_normal.width / 2
botao_normal.y = janela.height / 2 + 150

botao_infinito = GameImage("Imagens\infinito.png")
botao_infinito.x = janela.width / 4 - botao_infinito.width / 2 + 660
botao_infinito.y = janela.height / 2 + 150

botao_extra = GameImage("Imagens\extra.png")
botao_extra.x = janela.width/4 - botao_extra.width/2 - 150
botao_extra.y = janela.height/2 - 20

botao_creditos = GameImage("Imagens\creditos.png")
botao_creditos.x = janela.width/4 - botao_creditos.width/2 - 150
botao_creditos.y = janela.height/2 + 60

botao_concept_art = GameImage("Imagens\concept.png")
botao_concept_art.x = janela.width/4 - botao_concept_art.width / 2 - 150
botao_concept_art.y = janela.height/2 - 120

botao_saida = GameImage("Imagens\sair.png")
botao_saida.x = janela.width / 4 - botao_saida.width / 2 - 150
botao_saida.y = janela.height / 2 + 100

botao_saida_menor = GameImage("Imagens\sair_menor.png")
botao_saida_menor.x = janela.width / 2 - 650
botao_saida_menor.y = janela.height / 2 - 350