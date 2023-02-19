from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get('https://web.whatsapp.com/')
