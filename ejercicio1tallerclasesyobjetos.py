from Criptomonedas import Criptomoneda
bitcoin = Criptomoneda ("BTC", 0.34, 5000.00)
print (bitcoin.mostrarNombre())
print (bitcoin.calcularSaldo("USD"))
bitcoin.indicarSaldo(0.5)
bitcoin.calcularSaldo("USD")
print (bitcoin.calcularSaldo("USD"))