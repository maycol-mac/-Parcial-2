def numeros_respetidos(x):

    for i in x:
        d = x.count(i)
        if d > 1:
            print("El caracter",i,"Se repite",d,"veses")
