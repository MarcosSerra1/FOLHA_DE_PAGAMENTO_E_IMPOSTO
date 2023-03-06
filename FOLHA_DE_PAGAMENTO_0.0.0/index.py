

valor_hora = float(input('Digite o valor da hora de trabalho (somente numeros): '))
horas_trabalhadas = float(input('Digite quantas horas trabalhada no mes (somente numeros): '))
salario_bruto = valor_hora*horas_trabalhadas

desc_ir = 0
porcentagem_ir = 0

if salario_bruto > 0 and salario_bruto <= 1903.98:
    desc_ir = 0
    porcentagem_ir = '0'

elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
    desc_ir = 0.075
    porcentagem_ir = '7,5%'

elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
    desc_ir = 0.15
    porcentagem_ir = '15%'

elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
    desc_ir = 0.225
    porcentagem_ir = '22,5%'

else:
    desc_ir = 0.275
    porcentagem_ir = '27,5%'

ir = salario_bruto * desc_ir

fgts = salario_bruto * 0.08

inss = salario_bruto * 0.075

total_descontos = inss + ir

salario_liquido = salario_bruto - total_descontos

print('>>>>>>>>>>>>>>> FOLHA DE PAGAMENTO <<<<<<<<<<<<<<<')
print('Salario Bruto..................................: R$%.2f' %(salario_bruto))
print('(-)IR ('+porcentagem_ir+').....................: R$%.2f' %(ir)) # +porcentagem_ir+ é para aparecer a procentagem do imposto de renda
print('(-)INSS (10%%).................................: R$%.2f' %(inss))
print('FGTS (11%%)...........................................: R$%.2f' %(fgts))
print('Total de descontos.............................: R$%.2f' %(total_descontos))
print('Salario Liquido................................: R$%.2f' %(salario_liquido))


