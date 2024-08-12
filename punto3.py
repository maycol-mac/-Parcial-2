def diferencias_listas(x,y):
    for i in x:
        if i not in y:
            print("El cracter",i,"no esta en ambas listas")
    for i in y:
        if i not in x:
            print("El cracter",i,"no esta en ambas listas")
