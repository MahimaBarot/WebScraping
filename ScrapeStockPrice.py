import requests
from bs4 import BeautifulSoup
import json

mystocks = ['%5EIXIC','GC%3DF', 'BTC-USD', '%5ECMC200','%5ERUT']
stockdata = []

def getPrice(symbol):

  headers = {'User-Agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
  url = f'https://finance.yahoo.com/quote/{symbol}'

  r = requests.get(url,headers=headers)
  print(r.status_code)

  soup = BeautifulSoup(r.text, 'html.parser')
 
  stock = {
    'symbol': soup.find('div',{'class':'D(ib) '}).find_all('h1')[0].text,
    'price' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
  }
  return stock

for item  in mystocks:
  stockdata.append(getPrice(item))
  print('Getting: ', item)

with open('stockdata.json', 'w') as f:
  json.dump(stockdata, f)
