# R01235
import requests
from bs4 import BeautifulSoup
from datetime import datetime


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, features='xml')

def get_course():
    return soup.find('Valute', ID = 'R01235').Value.text
