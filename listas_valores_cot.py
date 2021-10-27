valores = list()
for cont in range (0, 5):# vamos digitar valor ate chegar a posição 5
    valores.append(int(input("Digite um valor: ")))
# Vai pedir para digitar um valor cada vez


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} !')
print("Cheguei ao final da lista.")
