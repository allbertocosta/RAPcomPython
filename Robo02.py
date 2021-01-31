import rpa as r
import pyautogui as p

r.init()
r.url('http://google.com')
janela = p.getActiveWindow()
janela.maximize()
r.wait(2.0)
r.type('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input', 'RPA[enter]')
r.wait(2.0)
r.snap('page', 'rpa_page.png')
r.wait(2.0)
r.close()