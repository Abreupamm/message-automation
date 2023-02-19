from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import csv
import time
import urllib


def import_data(path: str):
    if '.csv' in path:
        with open(path) as file:
            archive = csv.DictReader(file, delimiter=',', quotechar='"')
            return list(archive)
    else:
        raise ValueError('Arquivo inválido')


contacts_list = import_data('src/aqr.csv')

mesage = input('Digite sua mensagem:')
text = urllib.parse.quote(mesage)

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get('https://web.whatsapp.com/')


while len(driver.find_elements(By.ID, 'side')) < 1:
    time.sleep(2)


for phone_number in contacts_list:
    number = phone_number['Telefone']
    link = f'https://web.whatsapp.com/send?phone=55{number}&text={text}'
    driver.get(link)
    while len(driver.find_elements(By.CSS_SELECTOR, '._3E8Fg')) < 1:
        time.sleep(1)

    
    time.sleep(5)
    button_element = driver.find_element(By.CSS_SELECTOR, 'button.tvf2evcx')
    button_element.click()

driver.close()
print('FIM')