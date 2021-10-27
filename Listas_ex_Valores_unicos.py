'''Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-se
em uma LISTA. Caso o número já exista lá desntro, ele não será adcionado. No final
,serão exibidos todos os VALORES ÚNICOS digitados, em ordem CRESCENTE'''

'''Vamos criar uma lista que não sabemos quantos valores podem serem acrescentados'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adcionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)  # linhas de resultados 30vezes
numeros.sort() #Esse comando coloca na ordem crescente  
print(f'Você digitou os valores {numeros} ')

'''  Respostas 

Digite um valor: 9
Valor adcionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 2
Valor adcionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 3
Valor adcionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 9
Valor duplicado! Não vou adcionar...
Quer continuar? [S/N] s
Digite um valor: 40
Valor adcionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 15
Valor adcionado com sucesso...
Quer continuar? [S/N] s
Digite um valor: 10
Valor adcionado com sucesso...
Quer continuar? [S/N] n
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Você digitou os valores [2, 3, 9, 10, 15, 40]'''
