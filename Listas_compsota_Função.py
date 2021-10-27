'''Criando uma lista composta com função'''

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    #print(p) #printa todos os nome que existe na lista galera
    #print(p[0]) # printa so os nome de cada posição 
    #print(p[1]) #printa so a idade de cada posição
    print(f'{p[0]} tem {p[1]} anos de idade.' ) #print formatado 
''' Nesse print formatado aparece o nome que esta na primeira posição e a idade 
    EX: Jão tem 19 anos de idade.
    EX2: Ana tem 33 anos de idade.
    Ex3: Joaquim tem 13 anos de idade.
    Ex4: Maria tem 45 anos de idade.  '''