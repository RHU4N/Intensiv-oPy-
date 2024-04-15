import pyautogui
import pyperclip
import time
import pandas as pd


pyautogui.PAUSE=1
#abrir navegador
pyautogui.press("winleft")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(7.5)
# pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://fatecspgov-my.sharepoint.com/:f:/r/personal/alexandre_hashimoto_fatec_sp_gov_br/Documents/algoritmo/aulas%20de%20python%20gravadas/aula1/Aula%201?csf=1&web=1&e=AA2tOF")
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(x=420, y=328)
time.sleep(5)
pyautogui.click(x=420, y=328)
time.sleep(0.2)
pyautogui.click(x=613,y=337)
time.sleep(5)
pyautogui.click(x=736,y=501)
# a=pyautogui.position()
# pyautogui.alert(a)
time.sleep(5)
table=pd.read_excel(r"C:\Users\rhuan\Downloads\Vendas - Dez.xlsx")
faturamento = table['Valor Final'].sum()
qt_prod=table["Quantidade"].sum()
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl","v")
pyautogui.press('enter')
time.sleep(7.5)
pyautogui.click(x=188, y=171)
time.sleep(7.5)
pyperclip.copy("rhuan3003@gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")
time.sleep(2.5)
pyperclip.copy("teste")
pyautogui.hotkey("ctrl","v")
time.sleep(2.5)
pyautogui.press("tab")
pyperclip.copy(f"""
    teste
               
    teste
               
               e mais teste

               teste
               quantidade:{qt_prod}
valor:{faturamento}
""")
pyautogui.hotkey("ctrl","v")
time.sleep(2.5)
pyautogui.hotkey("ctrl","enter")