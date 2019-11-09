def bin(n):
    resto=[]
    while n >= 2:
        resto.append(str(n%2))
        n = n // 2
        if n < 2:
            resto.append('1')
    resto.reverse()
    resto = ''.join(resto)
    return resto