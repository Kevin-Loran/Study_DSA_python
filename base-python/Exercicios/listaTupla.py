numero = int(input("quantos elementos vai lista: "))
lista = [None] * numero

for i in range(numero):
    lista[i] = input("Digite um elemento: ")

print("\nlista digitada: ")
for elementos in lista:
    print(elementos)

# o mesmo serve para tuplas. Mas com um adendo que elas não podem ser modificadas depois de criadas.