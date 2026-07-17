def calcula_energia_potencial_gravitacional(m, h, g = 10):
    e = g * m * h
    return e

resposta = calcula_energia_potencial_gravitacional(30, 12, 9.8)

print(f"a resposta do calculo é {resposta}")