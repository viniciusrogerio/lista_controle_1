def substitui(string):
    lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lista_pares = []
    lista_string = list(string)
    
    for i in range(len(lista)):
        if i%2==0:
            lista_pares.append(lista[i])
    
    for i in range(len(lista_string)):
        if lista_string[i] in lista_pares:
            lista_string[i] = ' '
    
    string = ''.join(lista_string)
    
    return string
            
print(substitui('hoje é dia de aula'))
