#criando uma lista composta, pedindo nome e idade
galera = list()
dado = list() # lista secundária 
for c in range (0, 3): #Criei uma função para inclusão dos dados 
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade : ')))
    galera.append(dado[:]) #incluindo os dados que foi colocado dentro da lista dado e colocando dentro da lista galera
    dado.clear()
print(galera) #Vai mostrar a galera toda 



    

