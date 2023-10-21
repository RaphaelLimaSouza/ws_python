from time import sleep
import sys

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    print('Necessário modulo SELENIUM instalado.')
    sys.exit(0)

contatos =["Raphael Souza"] #Nomes das pessoas que quero enviar a msg.
msg = input("Mensagem: ")

def start_robo():
    drive = webdriver.Chrome()
    drive.get("https://web.whatsapp.com")
    input("Aguardando Ler QR Code") #Ler QR Code manual, 
    sleep(1)


    for contato in contatos:
        cx_pesquisa = drive.find_element('//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
        cx_pesquisa.send_keys(contato)
        cx_pesquisa.send_keys(Keys.ENTER)
        cx_msg = drive.find_element_by_class_name("matched-text _11JPr")
        cx_msg.send_keys(msg)
        bt_enviar = drive.find_element_by_class_name('_35EW6')
        bt_enviar.click()


start_robo()