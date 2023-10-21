print("Programa para reajuste de salário")
salario = float(input("Qual o seu salário atual?"))

if salario <= 280:
    percentual = 20
elif salario > 280:
    percentual = 15
elif salario > 700:
    percentual = 10
else:
   percentual = 5
   
   valordoaumento = salario * percentual / 100

   novosalario = valordoaumento + salario
   
   print("salário antes do reajuste: R$ {:.2f}".format(salario))
   print("Percentual aplicado ao seu salário:{} %".format(percentual))
   print("Aumento aplicado ao seu salário: R$ {:.2f}".format(valordoaumento))
   print("Seu salário após o aumento é: R$ {:.2f}".format(novosalario))