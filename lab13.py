import requests

def requst_for_currency():
    r = requests.get(url='http://data.fixer.io/api/latest', params={
                'access_key': '11175c5d0af6451a488d6788875e8d2b'})
    rates = r.json()['rates']
    return rates
def request_for_date():
    r = requests.get(url='http://data.fixer.io/api/latest', params={
        'access_key': '11175c5d0af6451a488d6788875e8d2b'})
    date = r.json()[ 'date' ]
    return date
date = request_for_date()
print(f'Last updated exchange rates was {date}, exchange rate against euro')
my_dict = requst_for_currency()
for key, value in my_dict.items():
        print(key, value)
