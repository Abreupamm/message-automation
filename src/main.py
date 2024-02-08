from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import csv
import time
import urllib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import filedialog

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

def format_number(n):
    number_formatted = f"+55 {n[:2]} {n[2:7]}-{n[7:]}"

    return number_formatted

def import_data(path: str):
    if '.csv' in path:
        with open(path) as file:
            archive = csv.DictReader(file, delimiter=',', quotechar='"')
            return list(archive)
    else:
        raise ValueError('Arquivo inválido')

def save_number(number):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{number}']")))
    link_number = driver.find_element(By.XPATH, f"//a[text()='{number}']")
    link_number.click()
    number_formatted = format_number(number)

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{number_formatted}']")))
    time.sleep(2)
    button_link_number = driver.find_element(By.XPATH, f"//span[text()='{number_formatted}']")
    button_link_number.click()

def send_message(message, number):
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, '_3Uu1_')))
    input_mensage = driver.find_elements(By.CLASS_NAME, '_3Uu1_')[0]
    input_mensage.click()
   
    for m in message:
        input_mensage.send_keys(m)
    

    button_element = driver.find_element(By.CSS_SELECTOR, 'button.tvf2evcx')
    button_element.click()


def main():
    contacts_list = import_data('src/aqr_exemple.csv')

    mesage = entry_message.get()
    # text = urllib.parse.quote(mesage)
    driver.get('https://web.whatsapp.com/')


    while len(driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(2)


    for phone_number in contacts_list:
        element_group = driver.find_elements(By.CSS_SELECTOR, 'span[title=TESTE]')
        element_group[0].click()
        number = phone_number['Telefone']

        send_message(number, True)
        save_number(number)
        time.sleep(10)
        send_message(mesage, False)

    # driver.close()
    print('FIM')

# Interface Gráfica
root = tk.Tk()
root.title('Envio de Mensagens WhatsApp')

# Elementos da Interface
label_message = tk.Label(root, text='Digite sua mensagem:')
entry_message = tk.Entry(root, width=50)
button_send = tk.Button(root, text='Enviar Mensagens', command=main)

# Posicionamento dos Elementos
label_message.grid(row=0, column=0, padx=10, pady=10)
entry_message.grid(row=0, column=1, padx=10, pady=10)
button_send.grid(row=2, column=0, columnspan=2, pady=10)

# Execução da Interface
root.mainloop()