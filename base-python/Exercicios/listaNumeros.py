numero = int(input("Digite quantos numeros vai na lista: "))
lista = []

for i in range(numero):
    valor = int(input(f"Digite o valor {i+1}: "))
    lista.append(valor)

soma = 0
for i in range(numero):
    soma += lista[i]

print(f"a soma dos valores da lista é de: {soma}")
