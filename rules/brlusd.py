import requests
import json

APIURL = 'https://economia.awesomeapi.com.br/last/USD-BRL'

try:
	DATA = requests.get(APIURL)
	NAME = DATA.json()['USDBRL']['name']
	COTA = "%.2f" % float(DATA.json()['USDBRL']['bid'])
	MAXIMUN = "%.2f" % float(DATA.json()['USDBRL']['high'])
	MINIMUN = "%.2f" % float(DATA.json()['USDBRL']['low'])

except:
	erromsg = 'Conexao com o host falhou'

if __name__ == '__main__':
	print(erromsg)