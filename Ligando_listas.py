a = [2, 3, 4, 7] # lista a 
b = a # a lista b vai receber os valores da lista a
b[2] = 8 #As duas lista vai receber o mesmo valor adicionado na posição 2 
print(f'Lista A: {a}')
print(f'Lista B: {b}')

"""Outro exemplo é, criar uma cópia da lista a na lista b, mais quando mudo valor de b, o 
valor de a não muda.
Exemplo:
        a = [2, 3, 4, 7]
        b= a [:]
        b[2] = 8
        aqui cria uma copia mais altera o valor de a"""