print("--CALCULADOR DE VIAGEM--\n")
def ler_valores():
    tempo_gasto = float(input("informe o tempo gasto na viagem: "))
    velocidade_media = float(input("informe a velocidade media da viagem: "))
    calcular_distancia(tempo_gasto, velocidade_media)

def calcular_distancia(tempo_gasto, velocidade_media):
    distancia = tempo_gasto * velocidade_media
    calcular_litros(distancia)

def calcular_litros(distancia):
    litros = distancia / 12
    mostrar_resultado(distancia, litros)

def mostrar_resultado(distancia, litros):
    print("\n" + "="*30)
    print(f"distancia percorrida: {distancia:.2f}KM")
    print(f"litros usados de gasolina: {litros:.2f}L")
    print("="*30)

ler_valores()