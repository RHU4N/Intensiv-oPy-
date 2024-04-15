import random
import time
import pyautogui
import pygetwindow as gw
import pyperclip

# listTempo=[1,3,5,10,15,30,60,100,180]
listTempo=[10] #teste

# Obtém todas as janelas abertas
windows = gw.getAllTitles()
# Lista de navegadores suportados
browsers = ["Chrome", "Firefox", "Opera", "Edge"]
# continuar="s"
browser_title = None  # Inicializa a variável

# Itera sobre cada navegador
for navegador in browsers:
    # Testa se há alguma janela aberta com algum navegador da lista
    if any(navegador.lower() in janela.lower() for janela in windows):
        browser_title = navegador
        break

# Testa se existe algum dado em browser_title
if browser_title:
    # Encontra a janela do navegador pelo título
    browser_window = gw.getWindowsWithTitle(browser_title)[0]
    # Verifica se está minimizado
    if browser_window.isMinimized:  
        browser_window.restore()  # Abre se tiver minimizado
        browser_window.maximize() #Maximiza 
    # Traz a janela do navegador para o foco
    browser_window.activate()
    browser_window.maximize() #maximiza

    pyautogui.hotkey("ctrl","t")
    
else:
    pyautogui.PAUSE=1
    pyautogui.press("winleft")
    pyautogui.write("edge")
    pyautogui.press("enter")
    edge = "edge"
    edge.maximize()

time.sleep(2.5)
pyperclip.copy("https://www.arealme.com/click-speed-test/pt/")
pyautogui.hotkey("ctrl","v")
pyautogui.press('enter')
time.sleep(7.5)
pyautogui.click(x=1261, y=243)
time.sleep(0.5)
pyautogui.scroll(-250)
time.sleep(2.5)

# while continuar=="s":
while True:
    if len(listTempo)==0:
        break
    tempo=random.choice(listTempo)
    listTempo.remove(tempo)
    if tempo==1:
        pyautogui.click(x=356, y=282)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==3:
        pyautogui.click(x=432, y=280)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==5:
        pyautogui.click(x=493, y=289)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==10:
        pyautogui.click(x=582, y=289)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==15:
        pyautogui.click(x=659, y=286)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==30:
        pyautogui.click(x=736, y=284)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==60:
        pyautogui.click(x=825, y=287)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==100:
        pyautogui.click(x=902, y=292)
        pyautogui.click(x=743, y=511)
        print(tempo)
    elif tempo==180:
        pyautogui.click(x=993, y=283)
        pyautogui.click(x=743, y=511)
        print(tempo)

    # pyautogui.click(x=728, y=510)
    time.sleep(5)
    tempo_inicial=time.time()
    while True:
        pyautogui.click(x=725, y=230,clicks=1000000)
        if time.time() - tempo_inicial >= tempo:
            print("Tempo limite atingido. Saindo do loop.")
            break

    time.sleep(2.5)
    pyautogui.click(x=706, y=281)
    time.sleep(15)
    pyautogui.click(x=599, y=414)

    # while True:
    #     continuar=str(input("Deseja continuar?(S/N):").lower().split())
    #     if continuar[0]=="s":
    #         break
    #     elif continuar[0]=="n":
    #         break
    #     else:
    #         print("Não é uma opção válida")

    time.sleep(3.5)
    pyautogui.click(x=1261, y=243)
    time.sleep(2.5)
    pyautogui.scroll(-250)
    time.sleep(2.5)
pyautogui.alert("Acabou")
