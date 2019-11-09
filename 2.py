#2. Faça uma função que dado um número n, retorne todos os seus divisores, excluído n.
def divisores(n):
    lista=[]
    for i in range (1,n,1):
        resto=n%i
        if resto==0:
            lista.append(i)
    print("O(s) divisor(es) de {} é(são) {}.".format(n,lista))