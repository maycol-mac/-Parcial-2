def mediana(arreglo_desordenado ):


    arreglo_ordenado = [None]*(len(arreglo_desordenado))
    for i in range (10):
        p = min(arreglo_desordenado)
        arreglo_ordenado[i]=p
        arreglo_desordenado.remove(p)
        if arreglo_desordenado == []:
            break

    me = len(arreglo_ordenado)
    me = me/2

    print("El arreglo ordenado es:",arreglo_ordenado)
    print("La mediana es:",arreglo_ordenado[int(me)])


