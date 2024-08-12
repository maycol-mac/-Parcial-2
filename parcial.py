from punto1 import numeros_respetidos
from punto2 import vocales_repetidas_palabra
from punto3 import diferencias_listas
from punto4 import promedio
from punto5 import mediana
 
def main():

    lista1 = [1,2,3,4,5,6,7,9,1]
    lista2 = [1,1,2,3,4,5,6,8,0]
    lista3 = [4,7,1,3,5,6,2]
    parrafo = ["Antonio", "Maria", "Mabel", "Barry", "John", "Guttag"]

    numeros_respetidos(lista1)
    vocales_repetidas_palabra(parrafo)
    diferencias_listas(lista1,lista2)
    promedio(lista1)
    mediana(lista3)

main()