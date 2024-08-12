def promedio(x):
    sum = 0
    for i in x:
        sum = i + sum

    pro = sum/(len(x))
    print("El promedio de la suma de las dos arreglos de reales es:",pro)