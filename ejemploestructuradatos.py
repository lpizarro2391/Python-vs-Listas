nombre_archivo = input("ingrese el nombre del archivo que contiene las palabras: ")
archivo = open(nombre_archivo,"r")

texto = archivo.read()
palabras = texto.split()
ocurrencias = {}

for palabra in palabras:
    if ocurrencias.get(palabra):
        ocurrencias[palabra]+=1
    else:
        ocurrencias[palabras]=1

maxpar = None,0
for palabra, cantidad in ocurrencias.items():
    if maxpar[1]<cantidad:
        maxpar=palabra,cantidad
print("La palabra con mayor cantidad de repeticion es",maxpar[0],"repetida",maxpar[1],"veces")    
