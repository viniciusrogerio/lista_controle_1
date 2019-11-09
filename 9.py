from random import randint

lista = []
lista_nova = []

for i in range(50):
    lista.append(randint(0,20))

for i in range (len(lista)):
    if lista[i] == max(lista):
        lista_nova.append(str(i))
    string = ', '.join(lista_nova)

print(lista)
print()
print('Soma dos elementos: ',sum(lista))
print('Ocorrências do número 7: ',lista.count(7))
print('Maior valor gerado na lista: ',max(lista))
print('Posições onde ocorrem o maior valor ({}): {}'.format(max(lista),string))
        
    

