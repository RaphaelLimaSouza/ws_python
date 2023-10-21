'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso 
e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
Neste momento o programa deverá ser encerrado, 
exibindo o relatório do dia, 
que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso. 
'''

def valorPagamento(valorPrestacao, diasAtraso):
    if diasAtraso == 0:
        return valorPrestacao
    else:
        multa = valorPrestacao * 0.03
        juros = valorPrestacao * (0.001 * diasAtraso)
        return valorPrestacao + multa + juros

total_prestacoes = 0
quantidade_prestacoes = 0

while True:
    valor_prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))
    if valor_prestacao == 0:
        break
    dias_atraso = int(input("Digite o número de dias em atraso: "))
    valor_total = valorPagamento(valor_prestacao, dias_atraso)
    print(f"O valor total a ser pago é R$ {valor_total:.2f}")
    total_prestacoes += valor_total
    quantidade_prestacoes += 1

print(f"\nRelatório do dia:\nQuantidade de prestações pagas: {quantidade_prestacoes}\nValor total de prestações pagas: R$ {total_prestacoes:.2f}")