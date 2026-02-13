Masculino = []
Feminino = []


maior_altura = 0.0
menor_altura = 3.0  # Começamos com um valor alto para que qualquer altura digitada seja menor
soma_alturas_homens = 0.0
cont_homens = 0
cont_mulheres = 0


for i in range(1, 16):
    print(f"--- Dados da {i}ª pessoa ---")


    altura = float(input("Digite a altura (ex: 1.75): "))
    genero = input("Digite o gênero (M para Masculino / F para Feminino): ").strip().upper()


    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura


    if genero == "M":
        soma_alturas_homens += altura
        cont_homens += 1
    elif genero == "F":
        cont_mulheres += 1
    else:
        print("Gênero inválido! Esta entrada não será contabilizada para as médias.")


if cont_homens > 0:
    media_homens = soma_alturas_homens / cont_homens
else:
    media_homens = 0


print("\n" + "=" * 30)
print("      RESULTADOS FINAIS")
print("=" * 30)
print(f"Maior altura do grupo: {maior_altura}m")
print(f"Menor altura do grupo: {menor_altura}m")
print(f"Média de altura dos homens: {media_homens:.2f}m")
print(f"Número de mulheres no grupo: {cont_mulheres}")