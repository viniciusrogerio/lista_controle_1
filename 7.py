def eprimo(n):
    contdiv = 0
    i = 1
    while i <= n:
        if n%i == 0:
            contdiv+=1
        i+=1
    if contdiv > 2:
        return False
    else:
        return True