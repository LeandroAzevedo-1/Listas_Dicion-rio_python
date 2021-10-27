teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #introduzi a lista teste dentro da lista galera, com [:]faço uma cópia
teste[0] = 'Maria' 
teste[1] = 22   
galera.append(teste[:]) # print, vai aparecer os dois resultado 
print(galera)

'''Criando outra lista composta '''

galeras = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeras[0]) #print na posição 0, aparece todos os dados João 19
print(galeras[0][0]) # Nesse print aparece so o dado João
print(galeras[2][1]) # Aparece o dados na posição 2 mais o dado 13
