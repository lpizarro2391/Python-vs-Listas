from Criptomonedas import Criptomoneda
litecoin = Criptomoneda ("LTC", 1.67, 124.00)
print (litecoin.mostrarNombre())
litecoin.calcularSaldo("USD")
print (litecoin.calcularSaldo("USD"))
litecoin.indicarCotizacion(154.45)
litecoin.calcularSaldo("USD")
print (litecoin.calcularSaldo("USD"))