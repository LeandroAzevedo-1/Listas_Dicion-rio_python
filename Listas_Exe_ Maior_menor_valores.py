'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o MAIOR e MENOR valor digitado e as suas respectivas posições na lista.'''

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:                               
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30) #Vai pedir para digitar os valores em suas respectivas posições
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='') # para mostrar as posições onde está o maior e o menor valor
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print() #printe de quebra de linha
print(f'O menor valor digitado foi {men} nas posições ', end='') 
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print() # print quebra de linha

''' No primeiro for temos o programa que vamos inseri os numeros,
    no segundo for temos o programa que vai dizer se é maior ou menor
    e no terfeiro for temos o programa que nos diz as posições '''