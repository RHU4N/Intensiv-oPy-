from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Edge()
navegador.get("https://www.google.com.br/?hl=pt-BR")

#dolar
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys("cotação dólar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)

cotacao_dolar=navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

navegador.get("https://www.google.com.br/?hl=pt-BR")

#euro
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys("cotação euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys(Keys.ENTER)

cotacao_euro=navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

#ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,é%20de%20caráter%20exclusivamente%20informativo.')
cotacao_ouro=navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')
cotacao_ouro=cotacao_ouro.replace(',','.')
print(cotacao_ouro)

navegador.quit()

tabela = pd.read_excel("Aula3-Meu/Produtos.xlsx")

tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = float(cotacao_dolar)
           
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacao_euro)
           
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacao_ouro)

tabela['Preço de Compra']= tabela["Preço Original"] * tabela["Cotação"]
tabela["Novo Preço de Venda"] = tabela["Preço de Venda"] * tabela["Margem"]


print(tabela)
tabela.to_excel("Aula3-Meu/Produtos.xlsx", index=False)

