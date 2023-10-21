numero = int(input("Por favor, insira um número inteiro entre 1 e 10: "))

if 1 <= numero <= 10:
    print("Tabuada de {}:".format(numero))
    for i in range(1, 11):
        print("{} X {} = {}".format(numero, i, numero * i))
else:
    print("Número inválido. Por favor, insira um número inteiro entre 1 e 10.")
