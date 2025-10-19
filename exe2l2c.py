numero_chave = 20
num = int(input("Digite um número entre 0 e 100: "))
if 0 <= num <= 100:
    distancia = abs(num - numero_chave)
    print(f"A distância até o número chave ({numero_chave}) é {distancia}")
else:
    print("Número fora do intervalo permitido.")
