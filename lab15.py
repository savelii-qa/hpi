import requests
import csv
import pandas as pd
from csv import DictWriter
import matplotlib.pyplot as plt


timestamp = "2020-05-24"


def requst_for_currency():
    r = requests.get(url=f'http://api.exchangeratesapi.io/v1/{timestamp}', params={
        'access_key': 'daaeebfb8c12feda79e4b311399025f1', 'symbols': 'UAH'})

    rates = r.json()[ 'rates' ]
    return rates


print(f'Last updated exchange rates was {timestamp}, exchange rate against euro')

my_dict = requst_for_currency()
currency = list(my_dict.values())
currency = currency[ 0 ]
dict_to_csv = {'date': timestamp, 'value': currency}
print(dict_to_csv)


for key, value in my_dict.items():
      print(key, value)

with open('event.csv', 'a') as csvfile:

     dictwriter_object = DictWriter(csvfile, fieldnames= {"date", "value"})
     dictwriter_object.writerow(dict_to_csv)


csv_columns = ['date','value']
csv_file = "test.csv"
try:
    with open(csv_file, 'a') as csvfile:
         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
         writer.writerow(dict_to_csv)
except IOError:
     print("I/O error")


df = pd.read_csv("test.csv", header=None, names =['date', 'value'])
df['date'] = pd.to_datetime(df['date'], format = '%Y/%m/%d')
df.plot('date', 'value')
plt.show()