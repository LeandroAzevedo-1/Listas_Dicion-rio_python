# Criando uma lista, Lembrando que lista é mutável.
num = [2, 5, 9, 1] #criei uma lista 
num[2] = 3 # Acrescentei o número 3 na posição 2 que é o número 9
num.append(7) #num.append adiciona o valor 7 no final da lista 
#num.sort() #coloca em ordem crescente os valors 
num.sort(reverse=True) # Coloca os valores da lista em ordem decrescente 
num.insert(2, 0) #Adcionando um valor na posição 2 
                                #num.pop()#Removendo elemento, sem parâmetro, elimina o valor 1
                                #num.pop(2) #Remove o elemento na posição 2
                                #num.remove(2), elimina o valor 2 que está na primeira posição

if 5 in num: #Função para elimar o valor que existe na lista
    num.remove(5) #Como o número 5 tem na lista, vamos eliminar!
else:
    print("Não encontrei o número 5")
print(num)
print(f'Essa lista tem {len(num)} elementos.') #Printe formatado com uma messagem usando afunção len 
