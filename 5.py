def remove(s):
    caracteres_indesejados = [['á','à','ã','â','ä'],
                              ['é','è','ê','ë'],
                              ['í','ì','î','ï'],
                              ['ó','ò','õ','ô','ö'],
                              ['ú','ù','û','ü'],
                              'ç']
    caracteres_sub = ['a','e','i','o','u','c']
    
    string=list(s)
    
    for i in range (len(string)):
        for j in range (len(caracteres_indesejados)):
            if string[i].lower() in caracteres_indesejados[j]:
                if string[i].islower():
                    string[i] = caracteres_sub[j]
                else:
                    string[i] = caracteres_sub[j].upper()
    string = ''.join(string)
    return string
