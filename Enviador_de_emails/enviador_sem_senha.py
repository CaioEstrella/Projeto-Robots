from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




email = "caio.estrella@gmail.com"
senha = " " ##INSERIR SENHA
destinatario = "caio.figueiredo@fgv.br"
assunto = "E-mail enviado pelo robo"
mensagem = "Mensagem enviada com sucesso"

driver = webdriver.Chrome('C:\\Users\\caio.figueiredo\\Projetos\\robos\\chromedriver')

print("Iniciando o robo...\n")
print("Acessando o e-mail...")
driver.get("https://www.gmail.com/")add

###LOGIN###
print("Fazendo Login...")
login = driver.find_element_by_id("identifierId")
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN) #APERTA ENTER
time.sleep(2)

password = driver.find_element_by_name("password")
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login Realizado!")
##### destinatario
driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
dest = driver.find_element_by_name("to")
dest.send_keys(destinatario)
##### assunto###
assun = password = driver.find_element_by_name("subjectbox")
assun.send_keys(assunto)

# MENSAGEM
mess = driver.find_element_by_xpath("//div[@role='textbox']")
mess.send_keys(mensagem)
mess.send_keys(Keys.RETURN)

# apertando o botão Enviar/Send
env = driver.find_element_by_xpath("//div[@aria-label='Send ‪(Ctrl-Enter)‬']")
env.click()
time.sleep(2)


driver.close()
