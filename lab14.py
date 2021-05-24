import requests
from bs4 import BeautifulSoup
import sys

symbol = input('Enter symbol: ')
    # Ссылка на нужную страницу
URL1 = f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}'
URL2 = f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
# Метод для получения курса валюты
def get_company_stats():
    full_page = requests.get(URL1, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    ShortPercent = soup.find('td', attrs={"data-reactid": "222"}).text
    SharesShort = soup.find('td', attrs={"data-reactid": "229"}).text
    DilutedEPS = soup.find('td', attrs={"data-reactid": "429"}).text
    return ShortPercent, SharesShort, DilutedEPS
def get_company_details():
    full_page = requests.get(URL1, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    Name = soup.find('h1', attrs={"data-reactid": "7"}).text
    Address = soup.find(attrs={"data-reactid": "8"}).text
    Employees  = soup.find(class_ = "Fw(600)", attrs={"data-reactid": "29"}).text
    CompanyDescription = soup.find('section').find(attrs={"data-reactid": "217"})
    return Name, Address, Employees, CompanyDescription
company_info = get_company_details()
company_info = list(company_info)
print("Name " + str(company_info[0]))
print("Address " + str(company_info[1]))
print("Employees " + str(company_info[2]))
print("CompanyDescription " + str(company_info[3]))
company_stats = get_company_stats()
company_stats = list(company_stats)
print('Short % of Shares Outstanding = ' + str(company_stats[0]))
print('Shares Short = ' + str(company_stats[1]))
print('Diluted EPS = ' + str(company_stats[2]))