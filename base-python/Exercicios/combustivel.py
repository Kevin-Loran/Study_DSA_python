tempo = float(input("Digite tempo total da viagem: "))
velocidadeMedia = float(input("Qual a velocidade media da viagem: "))
distancia = tempo * velocidadeMedia
kmPorLitro = 12
litros_usados = distancia / kmPorLitro

print(f"\n distancia percorrida: {distancia}KM"
      f"\n litros usados na viagem: {litros_usados:.2f}L "
      f"\n Tempo de viagem: {tempo} "
      f"\n velocidade media da viagem: {velocidadeMedia} ")