#pip install pyautogui
import pyautogui
import time #biblioteca para realizar pausas em lugar especificos
import pandas

#configurar para cada comando possuir pausa de 1 segundo
pyautogui.PAUSE = 0.5 

#pyautogui.click > clicar (X: >  Y: ⬇️)
#pyautogui.press > pressionar uma tecla
#pyautogui.write > escrever
#pyautogui.hotkey > atalho de teclado

#Passo 1: Abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win") #apertar a tecla windows
pyautogui.write("chrome") #digitar "chrome"
pyautogui.press("enter") #apertar enter

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #digitar a URL
pyautogui.press("enter") #pressionar enter

time.sleep(3) #pausa em um ponto em especifico

#Passo 2: Fazer o login

pyautogui.click(x=659, y=375) #selecionar primeiro grid de e-mail
pyautogui.write("joaoedhansen@gmail.com") #digital e-mail

pyautogui.press("tab") #proxímo grid de senha
pyautogui.write("tobias") #digitar senha

pyautogui.press("tab") #selecionar o botão "Logar"
pyautogui.press('enter') #entrar

#Passo 3: Importar a base de dados dos produtos
#pip install pandas openpyxl

tabela = pandas.read_csv("../produtos.csv")
print(tabela)

#Passo 4: Cadastrar 1 produto

# Passo 5: Reetir o passo 4 até acabat todos os produtos