from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time


def import_data(path: str):
    mesage = input('Digite sua mensagem:')
    if '.csv' in path:
        with open(path) as file:
            archive = csv.DictReader(file, delimiter=',', quotechar='"')
            print(mesage)
            return list(archive)
    else:
        raise ValueError('Arquivo inválido')


def execut_driver():
    driver = webdriver.Chrome(executable_path=r'src/chromedriver')
    driver.get('https://web.whatsapp.com/')


print(import_data('src/aqr.csv'))
