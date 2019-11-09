def ebisexto(ano):
    if ano%400 == 0 or (ano%4 == 0 and ano%100 != 0):
        return True
    else:
        return False