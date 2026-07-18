def ler_celsius():
    celsius = float(input("Digite a temperatura[C]: "))
    calcula_Fahrenheit(celsius)

def calcula_Fahrenheit(celsius):
    F = (9 * celsius + 160) / 5
    mostra_resultado(F, celsius)

def mostra_resultado(F, celsius):
    print("\n" + "="*30)
    print(f"o valor da leitura: {celsius}C "
          f"\nconversão para Fahrenheit: {F}F")
    print("="*30)

ler_celsius()
