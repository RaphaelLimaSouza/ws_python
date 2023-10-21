def valorPagamento(valor, dias_atraso):
    if dias_atraso > 0:
        multa = valor * 0.03
        juros = valor * (dias_atraso * 0.001)
        return valor + multa + juros
    else:
        return valor

total_pago = 0
quantidade_prestacoes = 0

while True:
    valor = float(input("Insira o valor da prestação (0 para encerrar): "))
    if valor == 0:
        break

    dias_atraso = int(input("Insira o número de dias em atraso: "))
    valor_a_pagar = valorPagamento(valor, dias_atraso)

    print("Valor a ser pago: R$ {:.2f}".format(valor_a_pagar))

    total_pago += valor_a_pagar
    quantidade_prestacoes += 1

print("\nRelatório do dia:")
print("Quantidade de prestações pagas: ", quantidade_prestacoes)
print("Valor total pago: R$ {:.2f}".format(total_pago))
