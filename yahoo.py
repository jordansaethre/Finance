# scraping data from yahoo finance

from lxml import html
import requests
import numpy as np

def stock_data(query):
	res = requests.get('https://finance.yahoo.com/quote/'+query+'/history?p='+query);
	s_data = html.fromstring(res.text)
	return s_data;

def print_stock_data(s_data, ticker):
	s_data_list = []
	s_data_list.append(ticker)
	for i in range(0,7):
		data_pt = s_data.cssselect('td span')[i]
		data = data_pt.text
		s_data_list.append(data)
		s_data_array = np.asarray(s_data_list)
		print(s_data_array)
	return s_data_array

def main():
	ticker=input('Enter stock ticker:')
	print()
	try:
	  query = ticker;
	  s_data = stock_data(query);
	  print_stock_data(s_data, ticker)
	  print()
	except:
	  print('Ticker not found...')

if __name__=='__main__':
	main()







