lista = []
contador = 0
while True:
    try:
      valor = int(input("Digite um valor: "))
    except:
        print("valor invalido. Digite um numero inteiro.")
    else:
        lista.append(valor)
        contador += 1
        if contador == 2:
            break

print(lista)