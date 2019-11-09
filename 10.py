def mdc(a,b):
    lista = []
    cont = 1
    
    if a > b:       
        while cont <= a:
            if a%cont == 0 and b%cont == 0:
                lista.append(cont)
                cont = cont + 1
            else:
                cont = cont + 1
    else:
        while cont <= b:
            if a%cont == 0 and b%cont == 0:
                lista.append(cont)
                cont = cont + 1
            else:
                cont = cont + 1
    return max(lista) 