import math

print("Digite dois valores: ")
a = int(input())
b = int(input())

print(f" valores digitados: "
      f"\n a = {a} "
      f"\n b = {b} "
      f"\n a soma dos valores digitados: {a + b}"
      f"\n a subtração dos valores digitados: {a - b}"
      f"\n a divisão dos valores digitados: {a / b}"
      f"\n a divisão inteira dos valores digitados: {a // b}"
      f"\n o resto dos valores digitados: {a % b} "
      f"\n {a} elevado a {b}: {a ** b} "
      f"\n a raiz quadrada de {a}: {math.sqrt(a)} "
      f"\n número quebrado e voce e voce quer arredondar: {round(0.897466, 3)}")
