from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando o robô...\n")
arq = open("C:\\Users\\caio.figueiredo\\Projetos\\robos\\Disponibilidade de domínios\\resultado.txt", "w")
dominios = []
####Lendo do excel####
workbook = xlrd.open_workbook('C:\\Users\\caio.figueiredo\\Projetos\\robos\\Disponibilidade de domínios\\dominios.xlsx')
sheet =  workbook.sheet_by_index(0)
for linha in range(0, sheet.nrows):
    for coluna in range(0, sheet.ncols): #itera pelas colunas da linha
        dominios.append(sheet.cell_value(linha, coluna))

driver = webdriver.Chrome('C:\\Users\\caio.figueiredo\\Projetos\\robos\\chromedriver')

driver.get("https://registro.br") #abre o site

for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear() #Limpa  abarra de pesquisa caso tenha texto
    pesquisa.send_keys(dominio) #escreve na barra
    pesquisa.send_keys(Keys.RETURN) #aperta ENTER na barra
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name("strong")
    print("Domínio %s %s" % (dominio, resultados[4].text)) #é o 4º elemento 'strong' na lita resultados
    texto = "Domínio %s %s\n" % (dominio, resultados[4].text)
    arq.write(texto)


arq.close()
time.sleep(2) #para não ir tão rápido e podermos visualizar

driver.close()
