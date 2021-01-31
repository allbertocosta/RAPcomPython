import pyautogui as p

p.hotkey('win','r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(2)
p.press('enter')
p.sleep(2)
p.typewrite('Ola mundo!!! Eu sou o primeiro Bot do Alberto')
p.sleep(2)
valor = p.getActiveWindow()
valor.close()
p.press('right')
p.sleep(2)
p.press('enter')


#p.sleep(2)
#print(p.position())