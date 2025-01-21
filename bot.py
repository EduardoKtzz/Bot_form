#ESTUDOS DE PYAUTOGUI

import pyautogui
import time

# Para pegar a informação vamos utlizar a biblioteca mouseinfo, é só ir no CMD e colocar python -m mouseinfo

# Funções do mouse - clicar, arrastar
# button - você escolhe com qual botão do mouse quer clicar
# clicks -  você escolhe a quantidade de cliques que você quer

# Comando para configurar o tempo  de execução de cada linha do codigo
pyautogui.PAUSE = 0.5

# Simular scroll do mouse
# Número negativo - Baixo
# Número positivo - Cima

#SCROLL
pyautogui.scroll(-100)
time.sleep(5)

# Simular clique somente com coordenada
# CLICK
pyautogui.click(x=967,y=242)

#clicar em um local com o mouse esquerdo
#CLICK
pyautogui.click(x=1003,y=5, button='left', clicks=1)

# arrastar o mouse para alguma área, sem executar um click
#ARRASTAR
time.sleep(0.5)
pyautogui.moveTo(x=1050,y=48, duration=0.5)  #duration - mover o mouse lentamente

# Clica em salvar 
#CLICK
pyautogui.click(x=1264,y=350, button='left', clicks=1)
time.sleep(5)

pyautogui.click(x=297,y=18, button='left', clicks=1)
pyautogui.click(x=354,y=63)
#FUNÇÔES TECLADO
#print(pyautogui.KEYBOARD_KEYS) - Mostra o nome de todas teclas do teclado

pyautogui.write('Programador')  #Vai passar um texto para você escrever
pyautogui.press('enter')  #Clica em uma tecla

pyautogui.hotkey("ctrl", "v")  # Simula varias teclas
