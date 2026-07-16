palavra = "CASACO"
maiuscula = palavra.upper()
minuscula = palavra.lower()
capital = palavra.capitalize()
metade_palavra = palavra[0:3]
final_palavra = palavra[3:]
nova_palavra = minuscula.replace('aco', 'inha')
tamanho = len(palavra)
sem_espaco = palavra.strip()
procura_letra = palavra.find('A')

print(f" essa é a palavra: {palavra} "
      f"\n agora ela maiuscula: {maiuscula} "
      f"\n agora ela minuscula: {minuscula} "
      f"\n agr com a primeira letra em maiusculo: {capital} "
      f"\n a metade da string: {metade_palavra} "
      f"\n o final da palavra: {final_palavra} "
      f"\n modificando a palavra: {nova_palavra} "
      f"\n aqui esta o tamanho: {tamanho}  "
      f"\n a String sem nenhum espaçamento:  {sem_espaco} "
      f"\n agr onde está a primeira letra 'A': {procura_letra}"
      )
