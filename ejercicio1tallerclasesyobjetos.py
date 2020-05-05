from Criptomonedas import Criptomoneda
bitcoin = Criptomoneda ("BTC", 0.34, 5000.00)
print (bitcoin.mostrarNombre())
bitcoin.calcularSaldo("USD")
bitcoin.indicarSaldo(0.5)
bitcoin.calcularSaldo("USD")
print (bitcoin.mostrarSaldo)