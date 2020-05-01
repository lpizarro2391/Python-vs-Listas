import requests

def esmoneda(cripto):
    return cripto in monedas

monedas=()
monedas_dict={}

data=requests.get("http://api.coinmarketcap.com/v2/ticker/").json()
for id in data["data"]:
    monedas_dict[data["data"][id]["symbol"]]=data["data"][id]["quotes"]["USD"]["Price"]

monedas=monedas_dict.keys()

moneda=input("Indique el nombre de la moneda a obtener el precio")
while not esmoneda(moneda):
        print("Moneda Inválida")
        moneda=input("Ingrese el nombre de la moneda")

else:
    print("La moneda con symbol:",moneda,
         "tiene un precio de : ",monedas_dict.get(moneda),"USD")