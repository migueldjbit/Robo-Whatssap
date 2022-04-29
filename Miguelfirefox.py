from selenium import webdriver
import time
from webdriver_manager.firefox (executable_path=r'C:\Users\djmig\Desktop\Python\geckodriver.exe')
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(FirefoxDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)


contato = ['Mirtes Alugue','Amanda Alugue Flat', 'jiih Silva','Flávia Alugue','Jiji Silva Corporativo','Jose carlos','Aline AFT','Alugue Flat Temporadas','Ingrid','Carlos Jose','Mãe','Ana Paula AFT']
mensagem = ' Olá tudo bem? Venho aqui da Alugue Flat Temporada te Mostrar nossas novas promoçôes. www.alugueflattemporadas.com.br  '

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    
    
for contato in contato:
    buscar_contato(contato)
    enviar_mensagem(mensagem)