import os
import pyautogui
import time

def limpar_arquivos_temporarios(diretorio_temporario):
    # Abre o Explorador de Arquivos
    pyautogui.hotkey('win', 'e')
    time.sleep(1)

    # Digita o caminho do diretório temporário
    pyautogui.typewrite(diretorio_temporario)
    time.sleep(1)
    
    # Pressiona "Enter" para abrir o diretório
    pyautogui.press('enter')
    time.sleep(1)

    # Seleciona todos os arquivos no diretório
    pyautogui.hotkey('ctrl', 'a')
    
    # Deleta os arquivos selecionados
    pyautogui.press('delete')
    time.sleep(1)

    # Confirma a exclusão (pressiona "Enter")
    pyautogui.press('enter')

# Substitua 'C:\\Caminho\\para\\o\\diretorio\\temporario' pelo caminho do seu diretório temporário
diretorio_temporario = r'C:\Users\Pedrinho\AppData\Local\Temp'

limpar_arquivos_temporarios(diretorio_temporario)
