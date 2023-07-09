import requests
from bs4 import BeautifulSoup
import json

# Adding stock names to extract information from
mystocks = ['%5EIXIC','GC%3DF', 'BTC-USD', '%5ECMC200','%5ERUT']
stockdata = []

'''
getrPrice(symbol)
input:  string form of stock name
output: dictionary containing stock name , stock price, price change
'''
def getPrice(symbol):

  headers = {'User-Agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
  url = f'https://finance.yahoo.com/quote/{symbol}'

  r = requests.get(url,headers=headers)
  print(r.status_code)

  soup = BeautifulSoup(r.text, 'html.parser')
 
  stock = {
    'symbol': soup.find('h1',{'class':'D(ib) Fz(18px)'}).text,
    'price' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
  }
  return stock

#iterate on list of stock names and append information in stockdata
for item  in mystocks:
  stockdata.append(getPrice(item))
  print('Getting: ', item)

#save information in JSON file
with open('stockdata.json', 'w') as f:
  json.dump(stockdata, f)
