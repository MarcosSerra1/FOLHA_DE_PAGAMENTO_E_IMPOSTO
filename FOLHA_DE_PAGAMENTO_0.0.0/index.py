 
# Dados para calculo da folha

salario_bruto = float(input('Digite um salario (somente numeros): ')) # Informar salario

inss_aliquota = 0  # desconto de inss
porcentagem_inss = 0 # porcentagem aplicada

# encontrando porcentagem da aliquota do inss

if salario_bruto > 0 and salario_bruto <= 1302.00:
    inss_aliquota = 0.075
    porcentagem_inss = '7,5%'

elif salario_bruto > 1302.01 and salario_bruto <= 2571.29:
    inss_aliquota = 0.09
    porcentagem_inss = '9%'

elif salario_bruto > 2571.30 and salario_bruto <= 3856.94:
    inss_aliquota = 0.12
    porcentagem_inss = '12%'

else:
    inss_aliquota = 0.14
    porcentagem_inss = '14%'

valor_inss = salario_bruto * inss_aliquota # valor do inss dado pelo valor do salario bruto * desconto do inss

base_irrf = salario_bruto - valor_inss # base irrf / ou imposto de renda


# encontrando porcentagem da aliquota do imposto de renda

ir_aliquota = 0
porcentagem_ir = 0

if base_irrf > 0 and base_irrf <= 1903.98:
    ir_aliquota = 0
    porcentagem_ir = '0'

elif base_irrf > 1903.99 and base_irrf <= 2826.65:
    ir_aliquota = 0.075
    porcentagem_ir = '7,5%'

elif base_irrf > 2826.66 and base_irrf <=  3751.05:
    ir_aliquota = 0.15
    porcentagem_ir = '15%'

elif base_irrf > 3751.06 and base_irrf <= 4664.68:
    ir_aliquota = 0.225
    porcentagem_ir = '22,5%'

else:
    ir_aliquota = 0.275
    porcentagem_ir = '27,5%'


salario_liquido = salario_bruto - valor_inss # valor do salario liquido
fgts = salario_bruto * 0.08
#total_descontos = valor_inss + 


print('>>>>>>>>>>>>>> FOLHA DE PAGAMENTO <<<<<<<<<<<<<<')
print('Salario Bruto............................: R$%.2f' %(salario_bruto))
print('(-)IR ('+porcentagem_ir+')...............: R$%.2f' %(ir_aliquota))
print('(-)INSS ('+porcentagem_inss+')...........: R$%.2f' %(valor_inss))
print('FGTS.....................................: R$%.2f' %(fgts))
#print('Total de descontos.......................: R$%.2f' %())
print('Salario Liquido...........................: R$%.2f' %(salario_liquido))

