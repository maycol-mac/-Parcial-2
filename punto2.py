def vocales_repetidas_palabra(x):
    vocales = ["a","e","i","o","u"]

    for i in vocales:
        for j in x:
            if i in j:
                vo = j.count(i)
                if vo > 1:
                    print("La vocal",i,"se repite",vo,"veces en la palabra",j)
