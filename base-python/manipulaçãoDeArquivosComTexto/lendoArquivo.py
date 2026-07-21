with open('frases1.txt', 'r') as texto:
    r = texto.readlines()
    print(r)

    # não roda o for por causa do cursor que já está no fim do arquivo.
    for linha in texto:
        print(linha)

# esse comando aqui cria um arquivo:
with open('frases2.txt', 'w') as texto:
    texto.writelines('Olá a todos')