import request
_ENDPOINT = "http://api.binance.com"

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticket/price?symbol="+cripto))

def esmoneda(cripto):
    criptos = ["BTC", "BBC","LTC","ETH","ETC","XRP" ]
    return  cripto in criptos

def esnumero(numero):
    return numero.replace('.','',1).isdigit()

monedas=[]
cantidades=[]
cotizaciones=[]
while i<3:
    moneda=input("Ingrese el nombre de la moneda: ")
    while not esmoneda (moneda):
        print("Moneda Invalida")
        monedas=input("Ingrese el nombre de la moneda:")
    else:
        monedas.append(moneda)
        data = get_price(moneda+"USD")
        cotizaciones.append(float(data["price"]))