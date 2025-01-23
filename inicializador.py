from PPlay.mouse import *
from PPlay.keyboard import *
from lugar_menu import lugar_menu
from modo_menu import janela

mouse = Mouse()
teclado = Keyboard()

while True:
    lugar_menu(janela,mouse,teclado)