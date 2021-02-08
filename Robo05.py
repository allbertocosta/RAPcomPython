import pyautogui as p

p.hotkey('win','r')
p.sleep(1)
p.write('C:\RPA.pbix')
p.sleep(1)
p.press('enter')
p.sleep(59)
p.click(x=700, y=92)
p.sleep(20)
p.click(x=1344, y=11)
p.sleep(20)
p.click(x=694, y=404)

#p.sleep(3)
#print(p.position())


