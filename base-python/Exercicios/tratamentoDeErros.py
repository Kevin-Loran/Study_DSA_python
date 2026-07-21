lista = []
contador = 0
while True:
    try:
      valor = int(input("Digite um valor: "))
    except IndexError:
        print("Erro, indice invalido")
        break
    except ValueError:
        print("Erro, valor invalido")
        break
    except KeyboardInterrupt:
        print("Erro, usuário interrompeu o programa")
        break
    else:
        lista.append(valor)
        contador += 1
        if contador == 2:
            break

print(lista)