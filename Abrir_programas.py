import pyautogui
import time

def abrir_programa(programa):
    # Abre o menu Iniciar (ou pressiona a tecla do Windows)
    pyautogui.hotkey('win')
    time.sleep(1)  # Aguarda um segundo para o menu Iniciar aparecer

    # Digita o nome do programa no menu Iniciar
    pyautogui.typewrite(programa)
    time.sleep(1)  # Aguarda um segundo para o resultado da pesquisa aparecer

    # Pressiona "Enter" para abrir o programa
    pyautogui.press('enter')

# Substitua 'notepad' pelo nome do programa que você deseja abrir
abrir_programa('notepad')
