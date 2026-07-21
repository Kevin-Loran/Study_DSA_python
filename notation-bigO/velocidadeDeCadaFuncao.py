import timeit
#função 1:
# 11 passos
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i

#função 2:
# 3 passos
def soma2(n):
    return (n * (n + 1) / 2)

#comparando velocidade de cada função:
tempo_soma1 = timeit.timeit(lambda: soma1(10), number=1000000)
tempo_soma2 = timeit.timeit(lambda: soma2(10), number=1000000)

print(f"--tempo de cada função-- "
      f"\n tempo da função 1: {tempo_soma1}"
      f"\n tempo da função 2: {tempo_soma2}")