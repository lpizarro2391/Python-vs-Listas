import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]
COINMARKET_API_KEY = "7dc3eb05-b9ca-401e-835e-1eaceaef62cf"
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7dc3eb05-b9ca-401e-835e-1eaceaef62cf'
}

data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=headers).json()
for cripto in data["data"]:
        monedas_list.append(cripto["symbol"])

monedas=tuple(monedas_list) 

moneda=input("Indique el nombre de la moneda a verificar:")
while not esmoneda(moneda):
    print("Moneda Inválida.")
    moneda=input("Ingrese el nombre de la moneda")
else: 
    print("La moneda," ,moneda,"es válida porque existe en coinmarketcap.com")
