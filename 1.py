#1. Faça uma função que dado uma entrada de número de dias, exiba esses dias na forma x anos y
#meses e z dias. Por exemplo: exibir_ano_mes_dia(634) retorna '1 ano, 8 meses e 29 dias '

def transforma_dia_mes_ano(dias_informados):
    dias=dias_informados
    i=0
    j=0
    k=0
    while dias>=365:
        dias=dias-365
        i=i+1
    while dias>=30:
        dias=dias-30
        j=j+1
    k=(dias)
    print("{} dias correspondem a {} ano(s), {} mes(es) e {} dia(s)".format(dias_informados,i,j,k))
