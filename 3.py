altura = float(input('Informe a altura em metros: '))
peso = float(input('Informe o peso em kg: '))

imc = peso/altura**2

if imc < 18.5 and imc > 0:
    print('Classificação: Magreza')

elif imc >= 18.5 and imc <= 24.9:
    print('Classificação: Normal')

elif imc >= 25 and imc <= 29.9:
    print('Classificação: Sobrepeso')

elif imc >= 30 and imc <= 39.9:
    print('Classificação: Obeso')

elif imc >= 40:
    print('Classificação: Obesidade grave')

else:
    print("Altura ou peso inválidos!")