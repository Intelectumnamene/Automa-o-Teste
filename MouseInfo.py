import pyautogui
from time import sleep
#usa atalho
pyautogui.hotkey('win','r')
#escreve
pyautogui.write('cmd')
#usa a tecla
pyautogui.press('enter')
sleep(1)
pyautogui.write('python')
pyautogui.press('enter')
sleep(1)
pyautogui.write('from mouseinfo import mouseInfo')
pyautogui.press('enter')
sleep(1)
pyautogui.write('mouseInfo()')
pyautogui.press('enter')