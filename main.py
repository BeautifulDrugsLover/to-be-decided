import pandas as pd
with open('av_key.txt','r') as f:
    key=f.read()

from urllib import request,parse
url = 'https://www.alphavantage.co/query?'

para = {
    'function':'TIME_SERIES_INTRADAY',
    'symbol':'MSFT',
    'interval':'5min',
    'outputsize':'full',
    'stock_ticker':'NSE',
    'datatype':'csv',

}

preq= parse.urlencode(para)
query = url+preq+'&'+'apikey='+key

data = pd.read_csv(query)
print(data)


import csv
import requests
#resp = request.urlopen(query)

#response = requests.get(query)
#print(response.content)
#data = csv.reader(response.content.split('\n'))
#with open('text_txt.txt','wt') as f:
    #f.write(data)
