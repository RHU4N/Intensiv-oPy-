import pygetwindow as gw
import pyautogui

# Obtém todas as janelas abertas
windows = gw.getAllTitles()

# Lista de navegadores suportados
browsers = ["Chrome", "Firefox", "Opera", "Edge"]  # Adicione outros navegadores conforme necessário

# Procura por uma janela de navegador
browser_window_title = None
for window_title in windows:
    for browser in browsers:
        if browser in window_title:
            browser_window_title = window_title
            break
    if browser_window_title:
        break

# Verifica se uma janela de navegador foi encontrada
if browser_window_title:
    # Encontra a janela do navegador pelo título
    browser_window = gw.getWindowsWithTitle(browser_window_title)[0]

    # Traz a janela do navegador para o foco
    browser_window.activate()

    # Aguarde um curto período de tempo para garantir que o navegador tenha tempo de se tornar o aplicativo ativo
    pyautogui.sleep(1)

    # Agora você pode prosseguir com suas interações no navegador usando o PyAutoGUI
    # Por exemplo, pressionando Ctrl+T para abrir uma nova aba
    pyautogui.hotkey("ctrl", "t")
else:
    print("Nenhuma janela de navegador encontrada.")
