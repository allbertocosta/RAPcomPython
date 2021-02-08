import pyautogui as p

p.doubleClick(x=115, y=28)
p.sleep(4)
p.write('www.udemy.com')
p.press('enter')
p.sleep(3)

localPesq = None
while localPesq is None:
      localPesq = p.locateOnScreen('Pesquisa.png', confidence=0.8)
print(localPesq)


#p.sleep(2)
#print(p.position())