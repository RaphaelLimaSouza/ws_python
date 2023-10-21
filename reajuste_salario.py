salario_atual = float(input("Por favor, insira o salário atual: "))

if salario_atual <= 280:
    percentual_aumento = 20
elif salario_atual <= 700:
    percentual_aumento = 15
elif salario_atual <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * percentual_aumento / 100

novo_salario = salario_atual + valor_aumento

print("Salário antes do reajuste: R$ {:.2f}".format(salario_atual))
print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
print("Valor do aumento: R$ {:.2f}".format(valor_aumento))
print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))
