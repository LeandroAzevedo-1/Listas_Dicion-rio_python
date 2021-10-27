'''Mostre so as pessoas que tem mais de 21 anos'''
galera = list()
dado = list() # lista secundária 
totmai = totmen = 0
for c in range (0, 3): #Criei uma função para inclusão dos dados 
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade : ')))
    galera.append(dado[:]) #incluindo os dados que foi colocado dentro da lista dado e colocando dentro da lista galera
    dado.clear()

'''Essa Função vai mostrar quantos  são maiores e quanto são menores'''

for p in galera: # para cada pessoa em galera
    if p[1] >= 21: #Se a pessoa for maior que 21 anos 
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menor de idade.')

'''Nesse caso vai pedir para colar o nome e a idade e pois aparecer todos os resultados 
Nome: pedro 
Idade : 23
Nome: maria
Idade : 11
Nome: jose 
Idade : 23
pedro  é maior de idade.
maria é menor de idade.
jose  é maior de idade.
Temos 2 maiores e 1 menor de idade.'''