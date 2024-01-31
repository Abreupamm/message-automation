from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import urllib
import tkinter as tk
from tkinter import filedialog
import time

def import_data(path: str):
    if path.endswith('.csv'):
        with open(path) as file:
            archive = csv.DictReader(file, delimiter=',', quotechar='"')
            return list(archive)
    else:
        raise ValueError('Arquivo inválido. Selecione um arquivo CSV.')

def send_messages(message, contacts_list):
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('https://web.whatsapp.com/')
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'side')))
    except TimeoutError:
        print("Tempo limite atingido ao aguardar o carregamento da página inicial.")

    for phone_number in contacts_list:
        number = phone_number['Telefone']
        link = f'https://web.whatsapp.com/send?phone=55{number}&text={message}'
        driver.get(link)
        while len(driver.find_elements(By.CSS_SELECTOR, '._3E8Fg')) < 1:
            time.sleep(1)

        time.sleep(5)
        button_element = driver.find_element(By.CSS_SELECTOR, 'button.tvf2evcx')
        button_element.click()

    driver.close()
    print('FIM')

def on_submit():
    message = entry_message.get()
    
    try:
        contacts_list = import_data('src/aqr_exemple.csv')
    except ValueError as e:
        print(e)
        return
    
    send_messages(message, contacts_list)

# Interface Gráfica
root = tk.Tk()
root.title('Envio de Mensagens WhatsApp')

# Elementos da Interface
label_message = tk.Label(root, text='Digite sua mensagem:')
entry_message = tk.Entry(root, width=50)
button_send = tk.Button(root, text='Enviar Mensagens', command=on_submit)

# Posicionamento dos Elementos
label_message.grid(row=0, column=0, padx=10, pady=10)
entry_message.grid(row=0, column=1, padx=10, pady=10)
button_send.grid(row=2, column=0, columnspan=2, pady=10)

# Execução da Interface
root.mainloop()
