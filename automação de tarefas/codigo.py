import pyautogui 
import time

pyautogui.PAUSE = 0.5

# 1 passo abrir o windows,digitar navegador, 
# precionar Enter, digitar endereço da empresa, pressionar enter
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("Enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")
#tempo para abrir o sistema
time.sleep(3)

#clicar e digitar login
pyautogui.click(x=487, y=376)
pyautogui.write("alexnicolasrangel@gmail.com")

#precionar tecla tab e digitar login
pyautogui.press("tab")
pyautogui.write("lam123456")

#precionar tecla tab e clicar no botão
pyautogui.press("tab")
pyautogui.press("enter")

#importar base de dados para cadastrar

import pandas

tabela = pandas.read_csv("produtos.csv")

#usando laço de repetição 
for linha in tabela.index:
    
    #casdastrar produtos 
    codigo = str(tabela.loc[linha,"codigo"]) #tranformando numero em texto 

    #clicar na barra para digiar
    pyautogui.click(x=551, y=252)

    #escrever na barra o codigo do produto
    pyautogui.write(codigo)

    #pressionar a tecla tab
    pyautogui.press("tab")

    #marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))

    #pressionar a tecla tab
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))

    #pressionar a tecla tab
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))

    #pressionar a tecla tab
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    #pressionar a tecla tab
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    #pressionar a tecla tab
    pyautogui.press("tab")

    #obs junto com uma condição if 
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
    
        pyautogui.write(obs)

    #pressionar a tecla tab
    pyautogui.press("tab")


    #apertar botao e voltar no topo da tela
    pyautogui.press("enter")
    pyautogui.scroll(5000)