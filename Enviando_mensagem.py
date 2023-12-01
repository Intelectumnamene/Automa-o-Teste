import pyautogui
import pyperclip


def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')


# Mover mouse até o campo digitar
pyautogui.moveTo(1500, 117, duration=1)
# Clicar no campo digitar
pyautogui.click()
# Digitar minha mensagem
escrever_frase("Automação é incrível!")
# Clicar no botão enviar
pyautogui.click(1500, 117, duration=1)
