print("--Exemplos de funções big-O--")

print("=" * 30)
print("\ncontante-O(1):")
lista = [1, 2, 3, 4, 5]
def constante(n):
    return print(n[0])

constante(lista)

print("=" * 30)
print("\nlinear-O(n):")
def linear(n):
    for i in range(n+1):
        print(i)

linear(11)

print("=" * 30)
print("\nquadratica-O(n^2):")
def quadratic(n):
    for i in range(n+1):
        for j in range(n+1):
            print(i, j)
        print("---")

quadratic(5)

#calculando função:

print("=" * 30)
print("\ncombination:")
def combination(n):
    #o(1)
    print(n[0])

    #o(5)
    for i in range(5):
        print("test", i)

    #o(n)
    for i in n:
        print(i)

    #o(n)
    for i in n:
        print(i)

    #o(3)
    print("python")
    print("python")
    print("python")

#resultado:
#o(1) + o(5) + o(3) + o(n) + o(n)
#o(9) + o(2n) -> o(n)